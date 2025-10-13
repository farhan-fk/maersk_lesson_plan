# =========================================
# Minimal OpenAI RAG Demo (Vector Store)
# =========================================
# 1. Create a vector store
# 2. Upload and index a PDF file
# 3. Ask a question and get an answer using file_search
#
# This is a simple, clean example for learners.
# =========================================

from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI()

# Path to your PDF file (update as needed - use Maersk-related documents like shipping policies, bills of lading, etc.)
PDF_PATH = Path(r"C:\Users\ffarh\OneDrive\Desktop\LLM_Full_Content\Course_Maersk\open_ai_new\apmm-q2-2023-interim-report_final (1)"
".pdf")
assert PDF_PATH.exists(), f"File not found: {PDF_PATH}"

if __name__ == "__main__":
    print("\n🔍 Minimal OpenAI RAG Demo\n" + "="*40)

    # --- SHOW: List all existing vector stores ---
    print("Existing vector stores:")
    try:
        stores = client.beta.vector_stores.list()
    except AttributeError:
        stores = client.vector_stores.list()
    if not stores:
        print("(None)")
    else:
        for vs in stores:
            print(f"Name: {getattr(vs, 'name', 'N/A')}, ID: {vs.id}")

    # 1. Create a vector store (try beta, fallback to non-beta)
    try:
        vector_store = client.beta.vector_stores.create(name="maersk_docs_store")
    except AttributeError:
        vector_store = client.vector_stores.create(name="maersk_docs_store")
    vector_store_id = vector_store.id
    print(f"Vector store ID: {vector_store_id}")

    # 2. Upload and index the PDF file (try beta, fallback to non-beta)
    print("Uploading & indexing file … (this may take a moment)")
    with PDF_PATH.open("rb") as f:
        try:
            client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store_id,
                files=[f],
            )
        except AttributeError:
            client.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store_id,
                files=[f],
            )
    print("File indexed in vector store.\n")

    # 3. Conversational chat loop with memory
    print("Type your questions about the document. Type 'exit' to quit.\n")
    conversation = [
        {"role": "system", "content": "You are a helpful Maersk logistics assistant."}
    ]
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"): break
        conversation.append({"role": "user", "content": user_input})
        # Stream the AI response as it is received (if supported)
        response = None
        full_response = ""
        try:
            stream = client.responses.create(
                model="gpt-5-nano",  # or gpt-4.1 etc.
                input=user_input,
                tools=[{
                    "type": "file_search",
                    "vector_store_ids": [vector_store_id]
                }],
                stream=True
            )
            print("AI:", end=" ", flush=True)
            for chunk in stream:
                text = getattr(chunk, "output_text", None) or getattr(chunk, "text", None) or ""
                print(text, end="", flush=True)
                full_response += text
                # Save the last chunk as response for citation extraction if possible
                response = chunk
            print()
        except TypeError:
            # Fallback to non-streaming if stream param not supported
            response = client.responses.create(
                model="gpt-5-nano",  # or gpt-4.1 etc.
                input=user_input,
                tools=[{
                    "type": "file_search",
                    "vector_store_ids": [vector_store_id]
                }],
            )
            print("AI:", response.output_text)
            full_response = response.output_text

        # Print source information if available and not empty
        if response and hasattr(response, "citations") and response.citations:
            print("\nSources:")
            for c in response.citations:
                source = c.get("file", "")
                page = c.get("page", "")
                snippet = c.get("snippet", "")
                details = []
                if source:
                    details.append(f"File: {source}")
                if page:
                    details.append(f"Page: {page}")
                if snippet:
                    details.append(f"Snippet: {snippet}")
                print("  - " + ", ".join(details))
        else:
            print("\n[Note] No sources/citations shown. This answer may be from the model's general knowledge, not RAG.")
