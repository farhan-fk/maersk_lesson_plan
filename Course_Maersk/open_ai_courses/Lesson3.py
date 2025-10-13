
# virtaul activation code for VS code (.\venv\Scripts\activate)
# Principle 2: Give model time to think
# Chain of thought prompting and self-evaluation

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

OpenAI.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

call_transcript = """\
Agent: Thank you for calling Maersk Logistics, this is Priya. How may I help you today?
Customer: I'm honestly very frustrated! My container was supposed to arrive three days ago, and I still don't have any updates!
Agent: I'm sorry to hear that, sir. Could you provide me the container number so I can check the status?
Customer: It's MAEU7894561. I've been calling every day, and no one gives me a clear answer!
Agent: I understand how frustrating that must be. Let me check your shipment details… yes, I can see the container is currently held at Nhava Sheva port awaiting customs clearance.
Customer: Customs clearance? Why wasn't I informed about this? My production line is stopped because of this delay!
Agent: I apologize for the lack of communication. It appears there was a documentation issue that's causing the delay.
Customer: Documentation issue? We submitted everything correctly! Are you people even checking properly or just making excuses?
Agent: I assure you, sir, we take every case seriously. I can see that our customs team is working to resolve this, but it may take 2-3 more business days.
Customer: 2-3 more days?! That's unacceptable! I'm losing thousands of rupees every day. I need this resolved immediately!
Agent: I completely understand your concern. Unfortunately, customs procedures are beyond our direct control, but I can escalate this to our port operations manager.
Customer: Escalate it then! This is ridiculous. I pay premium rates for your services and this is what I get?
Agent: I will escalate your case right away, sir. Would you like me to transfer you to my supervisor immediately?
Customer: Yes, do it now. I want to speak to someone who can actually help me, not just give me excuses.
Agent: Understood, sir. I'll transfer your call to my supervisor immediately. Please hold.
"""
# Priniciple 2: Give model time to think
# Specify step-by-step tasks also called as chain-of-thought prompting, below is an example of that

enterprise_prompt = """
You are analyzing a customer service call transcript. Follow these steps in order to produce a structured JSON report.

<transcript>
{call_transcript}
</transcript>

## Analysis Steps

**Step 1: Validate Data Sufficiency**
First, determine if the transcript contains enough information for analysis.
Return INSUFFICIENT_DATA if ANY of these conditions are true:
- Fewer than 3 meaningful exchanges between agent and customer
- Customer's issue or intent is completely unclear
- Transcript is severely garbled, incomplete, or has major language barriers

If insufficient, output ONLY:
{{
  "status": "INSUFFICIENT_DATA",
  "reason": "brief explanation of why data is insufficient"
}}

**Step 2: Analyze Sentiment & Tone**
Evaluate the emotional aspects of the interaction:
- Overall sentiment trajectory (positive/neutral/negative/mixed)
- Customer's emotional state throughout the call
- Agent's tone and approach

**Step 3: Classify the Interaction**
Identify:
- Type of interaction (complaint/inquiry/request/feedback/technical_support/other)
- Customer's primary intent
- Key topics or themes discussed
- Urgency and severity levels
- Whether escalation would be beneficial
- Presence of inappropriate language

**Step 4: Summarize Key Information**
Capture:
- The core customer issue
- What resolution or guidance was provided
- Whether follow-up action is needed

## Output Requirements

- **Confidentiality**: Exclude all PII (names, phone numbers, emails, account numbers, addresses)
- **Brevity**: Keep each text field under 100 characters
- **Format**: Return ONLY valid JSON, no markdown code blocks or extra text
- **Tone**: Professional and objective

## JSON Structure (when data is sufficient)

{{
  "sentiment": {{
    "overall": "positive|neutral|negative|mixed",
    "customerEmotion": "concise description of customer's emotional state",
    "agentTone": "concise description of agent's approach"
  }},
  "classification": {{
    "interactionType": "complaint|inquiry|request|feedback|technical_support|other",
    "customerIntent": "brief phrase describing what customer wants to achieve",
    "topics": ["topic1", "topic2", "topic3"],
    "urgency": "low|medium|high",
    "severity": "low|medium|high",
    "escalationSuggested": true|false,
    "escalationReason": "why escalation would help, or null if not suggested",
    "toxicLanguage": true|false
  }},
  "summary": {{
    "customerIssue": "concise problem statement",
    "resolution": "what was done to address the issue, or null if unresolved",
    "followUpRequired": true|false,
    "followUpDetails": "specific next steps needed, or null"
  }},
  "status": "COMPLETE",
  "ambiguities": ["list any unclear points or information gaps, empty array if none"]
}}

## Reference Examples

**Example 1 - Resolved Logistics Issue:**
{{
  "sentiment": {{
    "overall": "neutral",
    "customerEmotion": "initially concerned, then satisfied",
    "agentTone": "helpful and methodical"
  }},
  "classification": {{
    "interactionType": "inquiry",
    "customerIntent": "track delayed shipment",
    "topics": ["tracking", "delay", "port operations"],
    "urgency": "medium",
    "severity": "low",
    "escalationSuggested": false,
    "escalationReason": null,
    "toxicLanguage": false
  }},
  "summary": {{
    "customerIssue": "Container delayed at port, customer needs ETA update",
    "resolution": "Agent provided tracking details and confirmed new ETA",
    "followUpRequired": true,
    "followUpDetails": "Customer to receive proactive updates if further delays occur"
  }},
  "status": "COMPLETE",
  "ambiguities": ["exact cause of delay not specified in call"]
}}

**Example 2 - Escalated Issue:**
{{
  "sentiment": {{
    "overall": "negative",
    "customerEmotion": "frustrated and impatient",
    "agentTone": "empathetic but limited by process"
  }},
  "classification": {{
    "interactionType": "complaint",
    "customerIntent": "resolve customs clearance delay immediately",
    "topics": ["customs", "documentation", "delay", "financial impact"],
    "urgency": "high",
    "severity": "high",
    "escalationSuggested": true,
    "escalationReason": "requires port operations manager intervention for customs expediting",
    "toxicLanguage": false
  }},
  "summary": {{
    "customerIssue": "Container held at customs for 3 days, production stopped",
    "resolution": "Basic information provided; escalated to supervisor",
    "followUpRequired": true,
    "followUpDetails": "Port operations manager to expedite customs clearance"
  }},
  "status": "COMPLETE",
  "ambiguities": ["specific documentation issue not detailed"]
}}

Now analyze the transcript provided above.
"""


final_prompt = enterprise_prompt.replace("{call_transcript}", call_transcript)

response = get_completion(final_prompt)
print(response)


# Tactics 2: Ask Model to Self evaluate especially for mathematical problems

# prompt = f"""
# Determine if the student's solution is correct or not.

# Question:
# I'm setting up a new container yard and I need \
#  help working out the financials.
# - Land costs ₹5000 / square meter
# - I can set up container stacking infrastructure for ₹2000 / square meter
# - I negotiated a contract for maintenance that will cost \
# me a flat ₹500,000 per year, and an additional ₹100 / square \
# meter
# What is the total cost for the first year of operations
# as a function of the area in square meters.

# Student's Solution:
# Let x be the area in square meters.
# Costs:
# 1. Land cost: 5000x
# 2. Infrastructure cost: 2000x
# 3. Maintenance cost: 500,000 + 100x
# Total cost: 5000x + 2000x + 500,000 + 100x = 7100x + 500,000
# """
# response = get_completion(prompt)
# print(response)

# Earlier, we used to get answer as "The student's solution is correct."
# In case you encounter something similar, here is the prompting technique to get better answer

#
