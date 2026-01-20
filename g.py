import streamlit as st
from google import genai
client=genai.Client(api_key="AIzaSyB3Kc6LJZj0sFYYOCFstJsTNYXPKkOIdvE")
st.title("GENERATED_TEXT_PROJECT")
text_box=st.text_input("ask any question")
button=st.button("submit")
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[text_box],
)
if button:
    st.write(response.text)