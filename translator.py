from google import genai
import os

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

while True:
    text = input("Enter text to translate : ")
    if text.lower()=="exit":
        print("Goodbye")
        break
    source_language = input("From language: ")
    target_language = input("To language: ")
    
    prompt = f"""
Translate the following text from {source_language} to {target_language}.

Text:
{text}
Return only the translated text.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nTranslation:")
    print(response.text)