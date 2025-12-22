from openai import OpenAI

client = OpenAI(api_key="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")

def get_sketch_features(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}],
        tools=tools,
        tool_choice="auto"
    )
    return response.choices[0].message.content