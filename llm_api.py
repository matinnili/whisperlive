import openai
import fastapi

app = fastapi.FastAPI()
@app.post("/chat/completion")
def chat_completion(message : dict):
    # Set your API key
    user_query=message["text"]
    openai.api_key = "YOUR_API_KEY"

    # Example: Chat Completion (GPT-4)
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system","content":"you are assistant who edit the words which are recieved from asr. the words belong to "
            "the recorded conversation between the customer and person who works at the CRM of company. The company business field"
            "is making car batteries. In major cases, the customers call to report  their car battery malfunctioning"
            "due to this context, edit the wrong words."},
            {"role": "user", "content": user_query}
        ]
    )

    print(response.choices[0].message.content)