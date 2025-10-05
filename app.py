import streamlit as st
from resume_parser import parse_resume
from feedback_generator import generate_feedback
from utils import save_uploaded_file

st.set_page_config(page_title="AI Resume Builder & Reviewer", layout="wide")

st.title("AI-Powered Resume Review and Builder Tool")

uploaded_file = st.file_uploader("Upload your resume (PDF/Word)", type=["pdf", "docx"])
if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)
    
    st.subheader("Original Resume Text")
    resume_text = parse_resume(file_path)
    st.text_area("Resume Content", resume_text, height=300)
    
    st.subheader("AI Suggestions")
    suggestions = generate_feedback(resume_text)
    st.text_area("Improved Resume Suggestions", suggestions, height=300)
    
    if st.button("Download Improved Resume"):
        output_path = f"outputs/improved_{uploaded_file.name}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(suggestions)
        st.success(f"Improved resume saved: {output_path}")
