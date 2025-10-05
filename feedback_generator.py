import openai

# Set your OpenAI API key (can also use Streamlit secrets)
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_feedback(resume_text):
    """
    Generate AI-powered suggestions for a resume
    """
    prompt = f"""
    You are an expert resume reviewer. Read the following resume and provide:
    1. Improved bullet points
    2. Suggested skills/certifications
    3. Formatting/style improvements

    Resume:
    {resume_text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    return response.choices[0].message.content
