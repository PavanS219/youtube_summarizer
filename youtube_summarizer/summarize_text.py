import os
import google.generativeai as genai

def summarize_text(text, lang='en'):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel("gemini-pro")
    
    prompt = f"""
        The following text is in its original language. Provide the output in this language: {lang}. 
        Format the output as follows:

        Summary:
        short summary of the video

        Key Takeaways:
        succinct bullet point list of key takeaways

        input text: {text}
    """
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    text_to_summarize = input("Enter the text to summarize: ")
    lang = input("Enter the language for the summary: ")
    summary = summarize_text(text_to_summarize, lang)
    print("Summary:")
    print(summary)
