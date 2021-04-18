from typing import List
from objects.git_log_object import GitLogObject
from lib.GitRepository import Git
from lib.DingtalkRobot import Robot

# client git path
client_dir_root = r'D:\Projects\Unity_Projects\Works\WonderfulFarm\WonderfulFarmClient'

token = '3bf0a4b0e2ab15a87a72fd714e9006b3ceaa1b3b755da9d7e602efec9caf3417'

# search author names
authors = ['dingran', 'tanx', 'lin', 'wangyujie']

git = Git(client_dir_root)
robot = Robot(token)


def __screen_info_to_dict():
    """
    筛查
    :return:
    """
    screen_dict: {str: List[GitLogObject]} = {}
    for info in git.get_all_commit_info():
        if not authors.__contains__(info.name):
            continue
        if not info.check_today_time():
            continue

        if screen_dict.__contains__(info.name):
            screen_dict.get(info.name).append(info.msg)
        else:
            screen_dict[info.name] = [info.msg]
            pass
        pass
    return screen_dict


def __list_to_str(author: str, list_obj: List[GitLogObject]) -> str:
    result = 'Author:[[[[ %s ]]] \n' % author
    for i in list_obj:
        result += i
        pass
    return result


if __name__ == '__main__':
    screen_dict = __screen_info_to_dict()
    for k, v in screen_dict.items():
        msg = __list_to_str(k, v)
        msg += 'egame'
        request = robot.send(msg)
        pass
