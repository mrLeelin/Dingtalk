from datetime import datetime


class GitLogObject(object):

    def __init__(self, name: str, msg: str, time: datetime):
        self.name: str = name
        self.msg: str = msg
        self.time: datetime = time
        pass

    def check_today_time(self) -> bool:
        """
        is today
        :return:
        """
        return True
        return self.time.date() == datetime.today().date()


pass
