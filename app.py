import streamlit as st 
from openai import OpenAI

client=OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

st.title("📄 AI Text Summarizer")

st.sidebar.header("Summary Settings")

summary_type = st.sidebar.selectbox(
    "Choose Length",
    [10, 15, 20]
)

bullet_points = st.sidebar.checkbox("Bullet Point Summary")

input_text=st.text_area(
    "paste long text here",
    height=400
)

if st.button("generate summary"):
    if not input_text.strip():
        st.warning("please enter text")
        st.stop()

      # USER ROLE
    user_prompt = f"""
    Summarize this content into bullet points:

    {input_text}
    """

     # SYSTEM ROLE
    system_prompt = f"""
    Your name is Summarize Buddy.

    You are an expert summarizer.

    Rules:
    1. Always give summary in bullet points.
    2. give total {summary_type} bullet points.
    3. Keep only important points.
    4. Use simple and clear English.
    5. Make output neat and readable.
    """


    with st.spinner("Summarize Buddy is working..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        summary = response.choices[0].message.content

    st.subheader("📌 Bullet Point Summary")
    st.write(summary)