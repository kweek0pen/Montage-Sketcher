from openai import OpenAI

client = OpenAI(api_key="")

def get_sketch_features(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content