import streamlit as st
from groq import Groq
client=Groq(api_key=st.secrets["GROQ-API-KEY"])
st.title("Summurize Your Text")

text=st.text_area("Enter a paragraph or sentences:")


if st.button("Summarize"):
    if len(text.split())<10:
        st.warning("Text to short")
    else:
        with st.spinner("Summarizing....."):
            response=client.chat.completions.create(model="openai/gpt-oss-120b", messages=[{"role":"system","content":"You are a helpful assitant summurize this text in 3 or 4 sentences in the same languages"},{"role":"user","content":text}])
            
        st.success(response.choices[0].message.content)