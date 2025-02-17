import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBcWXn8BnzvbwQsxKcQuz30clByoNEJXJM")

def review_code(code):
    prompt = f"Review the following Python code for potential bugs and suggest fixes:\n```python\n{code}\n```\nProvide the corrected code separately."
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    return response.text if response else "No response received."

st.title("AI Code Reviewer")
code_input = st.text_area("Enter your Python code:")
if st.button("Review Code") and code_input.strip():
    review_result = review_code(code_input)
    st.subheader("Review and Suggestions")
    st.write(review_result)
    
    # Extract fixed code if available
    if "```python" in review_result:
        fixed_code = review_result.split("```python")[1].split("```", 1)[0].strip()
        st.subheader("Fixed Code")
        st.code(fixed_code, language="python")
