import os
from revChatGPT.ChatGPT import Chatbot
import requests

class OpenAI:

    def __init__(self):
        self.conversation_id = None
        self.endPoint = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": "Bearer {0}".format(os.environ["API_KEY"])
        }
        # self.chatbot = Chatbot({
        #     "session_token": os.environ['AI_SESSION_TOKEN']
        # }, conversation_id=None, parent_id=None)

    def ask(self, message: str):
        data= {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": message}
                ]
        }
        response = requests.post(
            url=self.endPoint,
            headers=self.headers,
            json=data
        )
        # print(response.json()['choices'][0]["message"]["content"].replace('\n', ' '));
        return Response(response.json())


class Response():
    def __init__(self, response: dict):
        self.message = response['choices'][0]["message"]["content"].replace('\n', ' ')
        # self.message_raw = response['message']
        # self.conversation_id = response['conversation_id']
        # self.parent_id = response['parent_id']

x = OpenAI()
x.ask("do u know typescript")