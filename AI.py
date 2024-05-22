import erniebot
import json


def AutoGrading(student):
    erniebot.api_type = "aistudio"
    erniebot.access_token = "e919322b04a840a0b629d58312a9334b9a8c3d18"
    # Create a chat completion
    response = erniebot.ChatCompletion.create(model="ernie-3.5", messages=[
        {"role": "user", "content":
         "你现在当老师帮我批阅学生的回答，我会给你正确答案，要求你给出这个学生的回答的得分与批阅建议，其中批阅建议要求简洁明了，我给你的数据是一个Json格式数组，其中StudentId未学生的id不需要你管，Question为题目，answer为题目的标准回答，StudentAnswer为学生的回答，answerScore为这题的总分,AIAnswer为你的批阅建议，你需要将你的批阅建议写在这里，其中score为你批阅的分数，分数必须为整数，你需要将你批阅的分数写在这里，待你全部批阅完后，按照我给你的Json格式返回你的结果，不要给出多余的内容，只需要一个标准json，按照我给你的Json格式,不要有第一行的```json与最后一行的```，这是数据："+str(student)}])
    s = response.get_result()
    # 去除字符串中的包裹 ```json
    s = s.strip('```json').strip()
    s = s.replace('\n', '').replace('\r', '')
    # 解析JSON字符串为Python字典
    data = json.loads(s)
    return data


if __name__ == "__main__":
    # List supported models
    models = erniebot.Model.list()

    # print(models)
    # ernie-3.5               文心大模型（ernie-3.5）
    # ernie-3.5-8k            文心大模型（ernie-3.5-8k）
    # ernie-lite              文心大模型（ernie-lite）
    # ernie-4.0               文心大模型（ernie-4.0）
    # ernie-speed             文心大模型（ernie-speed）
    # ernie-speed-128k        文心大模型（ernie-speed-128k）
    # ernie-tiny-8k           文心大模型（ernie-tiny-8k）
    # ernie-char-8k           文心大模型（ernie-char-8k）
    # ernie-text-embedding    文心百中语义模型
    # ernie-vilg-v2           文心一格模型

    # Set authentication params
    erniebot.api_type = "aistudio"
    erniebot.access_token = "e919322b04a840a0b629d58312a9334b9a8c3d18"
    studentAnswer = [
        {
            "StudentId": "1",
            "Question": "请简述软件测试的目的。",
            "answer": "软件测试的目的是为了发现软件中的错误而执行程序的过程。它包括了验证和确认两方面的活动，即验证软件是否满足规定的要求和确认软件是否满足用户实际的需要。软件测试的主要目的是找出软件中存在的错误，并评估软件的质量和可靠性。",
            "StudentAnswer": "软件测试的目的是确保软件可以正常运行，并且没有错误。",
            "AIAnswer": "",
            "answerScore": "10",
            "score": ""

        }, {
            "StudentId": "2",
            "Question": "请简述软件测试的目的。",
            "StudentAnswer": "软件测试的目的是为了确保软件满足用户的需求，并且运行正常。同时，也是为了找出并修复软件中的错误。",
            "answer": "软件测试的目的是为了发现软件中的错误而执行程序的过程。它包括了验证和确认两方面的活动，即验证软件是否满足规定的要求和确认软件是否满足用户实际的需要。软件测试的主要目的是找出软件中存在的错误，并评估软件的质量和可靠性。",
            "answerScore": "10",
            "AIAnswer": "",
            "score": ""
        },
    ]
    # Create a chat completion
    response = erniebot.ChatCompletion.create(model="ernie-3.5", messages=[
        {"role": "user", "content":
         "你现在当老师帮我批阅学生的回答，我会给你正确答案，要求你给出这个学生的回答的得分与批阅建议，其中批阅建议要求简洁明了，我给你的数据是一个Json格式数组，其中StudentId未学生的id不需要你管，Question为题目，answer为题目的标准回答，StudentAnswer为学生的回答，answerScore为这题的总分,AIAnswer为你的批阅建议，你需要将你的批阅建议写在这里，其中score为你批阅的分数，分数必须为整数，你需要将你批阅的分数写在这里，待你全部批阅完后，按照我给你的Json格式返回你的结果，不要给出多余的内容，只需要一个标准json，按照我给你的Json格式,不要有第一行的```json与最后一行的```，这是数据："+str(studentAnswer)}])

    print(response.get_result())
    print(json.load(response.get_result()))
