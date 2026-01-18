import openai
openai.api_key = "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"
def chat_with_GPT(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.contentstrip()

if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response = chat_with_GPT(user_input)
        print("Chatbot:",response)
    