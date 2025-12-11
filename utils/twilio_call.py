from twilio.rest import Client

# DIRECT TWILIO CREDENTIALS CONFIGURATION
TWILIO_SID = "YOUR_TWILIO_SID_HERE"
TWILIO_AUTH = "YOUR_TWILIO_AUTH_TOKEN_HERE"
TWILIO_PHONE = "YOUR_TWILIO_PHONE_NUMBER"

def trigger_emergency_call(user_number: str):
    client = Client(TWILIO_SID, TWILIO_AUTH)

    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to=user_number,
        from_=TWILIO_PHONE
    )
    return call.sid
