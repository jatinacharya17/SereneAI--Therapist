SereneAI – AI Mental Health Therapist

SereneAI is an AI-powered mental wellness assistant built using Streamlit and OpenAI. It provides supportive, real-time conversations, safety monitoring, and an optional emergency-call workflow through Twilio.

Key Features:
• AI therapist chat with streaming responses
• Safety and emotion detection
• Optional Twilio emergency calling
• Clean and responsive UI with custom CSS

Tech Stack:
• Python
• Streamlit
• OpenAI API
• Twilio API

Setup:
Install dependencies
pip install -r requirements.txt
Add .env with required keys

Run the app - streamlit run app.py

Project Structure:
• app.py – Main application
• utils/ – Chat, safety, and Twilio logic
• assets/style.css – UI styling
• requirements.txt – Dependencies

Deployment:
• Streamlit Cloud supports the chat interface
• Twilio calling requires backend hosting such as Render

SereneAI is a supportive tool and not a substitute for licensed mental-health professionals.
