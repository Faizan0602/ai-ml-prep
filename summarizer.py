from google import genai
import os

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

while True:
    message = input("\nPaste text to summarize (or type 'exit'): ")

    if message.lower() == "exit":
        print("Goodbye!")
        break

    prompt = f"""
    Summarize the following text in 3-5 bullet points:

    {message}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nSummary:")
    print(response.text)
    