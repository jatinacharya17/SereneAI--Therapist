from openai import OpenAI
client = OpenAI(api_key="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")

def stream_response(msg_list):
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=msg_list,
        stream=True,
    )
    
    full_reply = ""
    
    for chunk in stream:
        # Ensure delta and content exist
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            full_reply += token
            yield token

    return full_reply
