import streamlit as st
import requests

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
HEADERS = {"Authorization": "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"}

def query_huggingface(prompt):
    """Sends a request to Hugging Face API to generate text."""
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 500, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.json()}"

# Streamlit UI
st.title("JobSwift AI - Resume Optimizer")

st.write("Enhance your resume for better job applications with AI!")

# User inputs: Resume & Job Description
resume_text = st.text_area("Paste Your Resume Here:")
job_desc = st.text_area("Paste Job Description Here:")

if st.button("Optimize Resume"):
    if resume_text and job_desc:
        with st.spinner("Optimizing your resume..."):
            prompt = f"Improve this resume:\n{resume_text}\nFor this job:\n{job_desc}"
            optimized_resume = query_huggingface(prompt)
            
            st.subheader("Optimized Resume:")
            st.text_area("Your AI-optimized resume:", optimized_resume, height=300)
    else:
        st.warning("Please enter both Resume and Job Description!")

st.write("Powered by Hugging Face AI")