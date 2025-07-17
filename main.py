import requests,json,pprint


def do_request(api_key,subject,n_words):
    r=requests.request(
        method="POST",
        url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        headers={"Authorization": api_key,"Content-Type":"applitaction/json"},
        data=json.dumps({
            "model":"deepseek-r1",
            "messages": [
                {"role": "system", "content": "你是一个初中生写作文助手，用户将会给你作文的主题和字数要求，请根据用户的要求写出一篇初中满分作文，不许使用Markdown和emoji"},
                {"role": "user", "content": f"请写一篇主题为{subject}的作文，字数在{n_words}左右"},
            ]
        }),
    )
    return json.loads(r.content)

def main():
    api_key = input("输入你的阿里百炼 api-key: ")
    subject=input("请输入主题: ")
    n_words=int(input("请输入字数: "))
    print("AI生成中...")
    print(do_request(api_key,subject,n_words)['choices'][0]['message']['content'])


if __name__ == "__main__":
    main()
