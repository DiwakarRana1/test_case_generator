from google import genai
from google.genai import types
import json


def generate(user_input):
    # Initialize Vertex AI client
    client = genai.Client(
        vertexai=True,
        project="rare-inquiry-458506-b1",
        location="us-central1",
    )

    model = "gemini-2.0-flash-001"

    system_prompt = """You are a helpful test case generation assistant.

Your job is to generate test cases from:
- Feature descriptions
- Code snippets
- User stories
- API specs
- PDFs
- JIRA Tickets
- App Url

Use the following format for each test case:

**Test Case Title**:  
**Description**:  
**Preconditions**:  
**Test Steps**:  
**Expected Result**:  
**Test Type**: (Unit, Functional, Integration, Edge, etc.)

Only generate test cases unless the user explicitly asks for something else.
"""

    contents = [
        types.Content(role="user", parts=[types.Part(text=system_prompt)]),
        types.Content(role="user", parts=[types.Part(text=user_input)])
    ]

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain"
    )

    response = ""
    for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
    ):
        response += chunk.text

    # Try to beautify the JSON response
    try:
        parsed = json.loads(response)
        pretty_response = json.dumps(parsed, indent=4)
    except json.JSONDecodeError:
        pretty_response = response  # Fallback if response is not valid JSON

    return pretty_response

if __name__ == "__main__":
    user_input = input("Enter feature/code/url to generate test cases: ")
    print(generate(user_input))
