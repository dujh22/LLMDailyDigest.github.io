from openai import OpenAI
from dotenv import load_dotenv
import os
# import config
import config2 as config # 导入配置文件,注意这里的config2是一个文件名，你可以改为config,最直接的办法是复制一个config.py文件,重命名为config2.py，然后把里面的api_key改为你的api_key

# 加载 .env 文件
load_dotenv()

client = OpenAI(
    api_key=config.api_key,
    base_url=config.base_url
)

# 非流式调用
def llm_chat(prompt, model = config.model):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content

# 非流式调用
def llm_chat_with_his(messages, model = config.model):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return chat_completion.choices[0].message.content

# 带提示的对话,非流式调用
def llm_chat_with_prompt(prompt, user_str, model = config.model):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": user_str,
            }
        ],
        model=model,
    )
    return chat_completion.choices[0].message.content

# 流式调用
def llm_chat_stream(prompt, model = config.model):
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")



# 主要测试函数
def main():
    print(llm_chat("你好，请问你是谁？"))
    # llm_chat_stream("你好，请问你是谁？")
    # print(llm_chat_with_prompt("你现在是一个医生健康助手", "请问你可以做什么"))

if __name__ == "__main__":
    main()
    