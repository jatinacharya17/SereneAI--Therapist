import streamlit as st
from utils.chat import stream_response
from utils.safety import is_dangerous
from utils.twilio_call import trigger_emergency_call
from openai import OpenAI

client = OpenAI(api_key="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")

st.set_page_config(page_title="SereneAI Therapist", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("SereneAI — Mental Health Therapist")

# Render chat history with avatars
for sender, text in st.session_state.messages:

    if sender == "user":
        st.markdown(
            f"""
            <div class="user-row">
                <div class="user-bubble">{text}</div>
                <div class="user-avatar"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div class="bot-row">
                <div class="bot-avatar"></div>
                <div class="bot-bubble">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Immediately show user's bubble
    st.session_state.messages.append(("user", user_input))

    # Emergency check
    if is_dangerous(user_input):
        st.session_state.messages.append(
            ("bot", "I’m concerned about your safety. Emergency support has been notified.")
        )
        trigger_emergency_call("+917297018580")

    else:
        # Build message list for AI
        msg_list = [{"role": "system", "content": "You are a supportive therapist."}]
        for s, m in st.session_state.messages:
            role = "assistant" if s == "bot" else "user"
            msg_list.append({"role": role, "content": m})

        # AI reply (fast, no streaming)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=msg_list
        )
        bot_reply = response.choices[0].message.content

        st.session_state.messages.append(("bot", bot_reply))

    st.rerun()
