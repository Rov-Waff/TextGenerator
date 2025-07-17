import requests,json,pprint
ARTICLE_TYPE={1:"记叙文",2:"议论文",3:"说明文"}

def do_request(api_key,subject,n_words,article_type):
    r=requests.request(
        method="POST",
        url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        headers={"Authorization": api_key,"Content-Type":"applitaction/json"},
        data=json.dumps({
            "model":"deepseek-r1",
            "messages": [
                {"role": "system", "content": f"你是一个写作文助手，用户将会给你作文的主题和字数要求，请根据用户的要求写出一篇满分{article_type}，不许使用Markdown和emoji,要求写标题"},
                {"role": "user", "content": f"请写一篇主题为{subject}的作文，字数在{n_words}左右,额外要求:"},
            ]
        }),
    )
    return json.loads(r.content)

def main():
    api_key = input("输入你的阿里百炼 api-key: ")
    subject=ARTICLE_TYPE[input("请输入主题(1.记叙文 2.议论文 3.说明文): ")]
    article_type=input("请输入文体 :")
    while(True):
        try:
            n_words=int(input("请输入字数: "))
            break
        except:
            print("好歹你输入个数字吧（")
            continue
    print("AI生成中...")
    try:
        print(do_request(api_key,subject,n_words,article_type)['choices'][0]['message']['content'])
    except:
        print("请求失败，检查你的API-Key")

if __name__ == "__main__":
    main()
