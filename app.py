import streamlit as st
import openai  

# OpenAI API Key (GitHub Secrets ya Streamlit secrets me store karo)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.title("🤖 AI Assistant - YouTube, Story & Study Helper")
st.write("Apna GPT Assistant - Hindi-English Style mein")

task = st.selectbox("Task choose karo:", ["YouTube Script", "Story", "Study Help"])
user_input = st.text_area("Apna topic ya idea yahan likho:")

if st.button("Generate"):
    if not OPENAI_API_KEY:
        st.error("⚠️ API key missing! Please add your OpenAI API key.")
    else:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # ✅ LATEST VERSION  
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7
        )
        st.write(response.choices[0].message.content)
