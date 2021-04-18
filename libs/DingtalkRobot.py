import requests


class Robot(object):
    def __init__(self, token: str):
        self.__token = token
        self.__url = "https://oapi.dingtalk.com/robot/send?access_token=" + token
        self.__values_template = """{
      "msgtype":"text",
      "text":{
        "content": "%s"
      }
      }"""
        pass

    def send(self, msg: str):
        """
        发送数据
        :param msg:
        :return:
        """
        send_msg = self.__values_template % msg
        headers = {
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
        return requests.post(self.__url, data=send_msg.encode('utf-8'), headers=headers, )

    pass
