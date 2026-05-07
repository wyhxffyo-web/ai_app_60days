from openai import OpenAI

client = OpenAI(
    api_key="sk-14f9259a4112415c9b88673aa36b1694",
    base_url="https://api.deepseek.com/v1"
)

messages = [{"role": "system","content": "你是一个言简意赅的助手"}]

while True:
    user_msg=input("您:")
    if user_msg == "exit":
        break
    messages.append({"role":"user","content":user_msg})

    response=client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
    )
    ai_msg = response.choices[0].message.content
    print("ai:",ai_msg)
    messages.append({"role":"user","content":ai_msg})