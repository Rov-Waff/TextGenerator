import requests,json,pprint


def do_request(api_key):
    r=requests.request(
        method="POST",
        url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        headers={"Authorization": api_key,"Content-Type":"applitaction/json"},
        data=json.dumps({
            "model":"qwen-plus",
            "messages": [
                {"role": "system", "content": "你是一个初中生写作文助手，用户将会给你作文的主题和字数要求，请根据用户的要求写出一篇初中满分作文，不许使用Markdown和emoji"},
                {"role": "user", "content": "你是谁？"},
            ]
        }),
    )
    return json.loads(r.content)

def main():
    api_key = input("输入你的阿里百炼 api-key: ")
    pprint.pprint(do_request(api_key))


if __name__ == "__main__":
    main()
