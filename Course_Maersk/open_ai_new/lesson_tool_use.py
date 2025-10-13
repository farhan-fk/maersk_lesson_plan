# According to OpenAI, the following tool types are supported directly in the Responses API:
# web_search_preview
# web_search_preview_2025_03_11
# file_search
# code_interpreter
# image_generation
# mcp (Model Context Protocol)
# computer_use_preview
# function (for defining your own API/tools)

from openai import OpenAI
import os
import base64
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()




client = OpenAI()

# response = client.responses.create(
#     model="gpt-5-nano",
#     tools=[{"type": "web_search"}],
#     input="What was breaking news story from  India Yesterday?"
# )

# print(response.output_text)
# Below Codes work but Saving Image is an issue
# few of the Inbuilt tools
response = client.responses.create(
    model="gpt-5-nano",
    tools=[
        {"type": "web_search"},                                   # optional if you want fresh data
        {"type": "code_interpreter", "container": {"type": "auto"}}
    ],
    input=("Fetch global container shipping volume data from reliable public sources (e.g., World Shipping Council or UNCTAD).\
            Cite the exact URLs used. Then use Python with pandas and matplotlib to plot a labeled line chart \
           showing shipping volumes by year, save it as chart.png, and return the file along with a short summary of the data."),
)



# --- Inspect what actually came back
print("\n=== OUTPUT ITEMS ===")
for i, item in enumerate(response.output):
    print(i, getattr(item, "type", None), getattr(item, "tool_name", None))
    # Debug: Print more details about each item
    if hasattr(item, '__dict__'):
        print(f"   Item {i} attributes:", list(item.__dict__.keys()))

# # --- Enhanced file extraction for Responses API
# saved = []
# print("\n=== ATTEMPTING FILE EXTRACTION ===")

# # Method 1: Look for code_interpreter_call items with files
# for i, item in enumerate(response.output):
#     print(f"Processing item {i}: {getattr(item, 'type', None)}")
#
#     if getattr(item, "type", None) == "code_interpreter_call":
#         print(f"  Found code_interpreter_call at index {i}")
#
#         # Check for files in the result
#         if hasattr(item, 'result') and hasattr(item.result, 'files'):
#             print(f"  Found {len(item.result.files)} files in result")
#             for file_obj in item.result.files:
#                 try:
#                     file_id = getattr(file_obj, 'id', None) or getattr(file_obj, 'file_id', None)
#                     filename = getattr(file_obj, 'filename', 'downloaded_file')
#
#                     if file_id:
#                         print(f"  Downloading file: {filename} (ID: {file_id})")
#                         content = client.files.content(file_id)
#                         local_filename = filename if filename.endswith(('.png', '.jpg', '.jpeg', '.csv', '.txt')) else f"{file_id}.bin"
#
#                         with open(local_filename, "wb") as out:
#                             out.write(content.read())
#                         saved.append(local_filename)
#                         print(f"  ✅ Successfully saved: {local_filename}")
#                     else:
#                         print(f"  ❌ No file ID found for {filename}")
#                 except Exception as e:
#                     print(f"  ❌ Error downloading file: {e}")

# # Method 2: Look for files in any tool output
# for i, item in enumerate(response.output):
#     if hasattr(item, 'files'):
#         print(f"  Found files attribute in item {i}")
#         for file_obj in item.files:
#             try:
#                 file_id = getattr(file_obj, 'id', None)
#                 filename = getattr(file_obj, 'filename', 'output_file')
#
#                 if file_id:
#                     print(f"  Downloading: {filename}")
#                     content = client.files.content(file_id)
#                     with open(filename, "wb") as out:
#                         out.write(content.read())
#                     saved.append(filename)
#                     print(f"  ✅ Saved: {filename}")
#             except Exception as e:
#                 print(f"  ❌ Error: {e}")

# # Method 3: Check response object for files
# if hasattr(response, 'files') and response.files:
#     print(f"Found {len(response.files)} files in response object")
#     for file_obj in response.files:
#         try:
#             file_id = file_obj.id
#             filename = getattr(file_obj, 'filename', 'response_file.png')
#
#             print(f"Downloading response file: {filename}")
#             content = client.files.content(file_id)
#             with open(filename, "wb") as out:
#                 out.write(content.read())
#             saved.append(filename)
#             print(f"✅ Saved: {filename}")
#         except Exception as e:
#             print(f"❌ Error downloading response file: {e}")

# # Fallback: Search for base64 images in text output
# print("\n=== CHECKING FOR BASE64 IMAGES ===")
# import re
# for item in response.output:
#     if hasattr(item, 'content'):
#         text = str(getattr(item, "content", ""))
#         matches = re.findall(r"data:image/(png|jpeg);base64,([A-Za-z0-9+/=]+)", text)
#         for i, (ext, b64_data) in enumerate(matches):
#             try:
#                 filename = f"chart_base64_{i}.{ext}"
#                 with open(filename, "wb") as f:
#                     f.write(base64.b64decode(b64_data))
#                 saved.append(filename)
#                 print(f"✅ Extracted base64 image: {filename}")
#             except Exception as e:
#                 print(f"❌ Error extracting base64 image: {e}")

# print(f"\n🎯 FINAL RESULT:")
# print(f"Saved files: {saved}")
# if saved:
#     print(f"✅ Successfully saved {len(saved)} file(s) to current directory!")
#     for file in saved:
#         import os
#         if os.path.exists(file):
#             size = os.path.getsize(file)
#             print(f"   📁 {file} ({size} bytes)")
# else:
#     print("❌ No files were saved. The chart might be in OpenAI's sandbox only.")
#     print("💡 Try checking the response text for download links or file references.")

# print("\nFinal text:")
# print(response.output_text)




# print("\n" + "="*60)
# print("🔍 FILE SEARCH TOOL - OpenAI's Built-in RAG")
# print("="*60)




