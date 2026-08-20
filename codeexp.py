from google import genai

import os



client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("===== AI CODE EXPLAINER =====")

language = input("Programming language: ")

print("\nPaste your code below.")
print("Type END on a new line when finished.\n")

code_lines = []

while True:
    line = input()

    if line == "END":
        break

    code_lines.append(line)

code = "\n".join(code_lines)

prompt = f"""
You are an expert programming teacher.

The programming language is: {language}

Explain the following code to a beginner.

CODE:
{code}

Provide the explanation in these sections:

1. Overview
2. Line-by-line explanation
3. Concepts used
4. Example execution

Use simple and easy-to-understand language.
Do not rewrite the entire code.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n===== CODE EXPLANATION =====\n")
print(response.text)