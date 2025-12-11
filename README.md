SereneAI – AI Mental Health Therapist

SereneAI is an AI-powered mental wellness assistant built with Streamlit and OpenAI. It provides supportive, real-time therapeutic conversations with safety monitoring and an optional emergency-call workflow using Twilio. The project includes a clean chat interface, custom styling, and modular utility files for chat handling, safety checks, and call triggers.

Features:
AI therapist chat, streaming responses, emotion/safety detection, optional Twilio emergency calling, custom UI.

Tech Stack:
Python, Streamlit, OpenAI API, Twilio API, CSS.

Setup:
Clone the repo, install requirements, add your OPENAI_API_KEY and optional Twilio keys in a .env file, then run:

streamlit run app.py


Structure:
app.py (main app), utils/ (chat, safety, Twilio logic), assets/style.css, requirements.txt.

Deployment:
Works on Streamlit Cloud for chat functionality. Twilio calling requires backend hosting (e.g., Render).

SereneAI is a supportive assistant, not a replacement for licensed mental-health professionals.
