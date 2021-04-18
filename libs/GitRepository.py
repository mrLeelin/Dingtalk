import os
from git.repo.fun import is_git_dir
from objects.git_log_object import GitLogObject
from typing import List
from git import Repo, Commit


class Git(object):
    def __init__(self, local_path: str):
        self.__local_path = local_path
        self.__initial()
        pass

    def __initial(self):
        """
        initialize git repository
        :return:
        """
        assert os.path.exists(self.__local_path), 'Git path ie not exist.'
        git_local_path = os.path.join(self.__local_path, '.git')
        assert is_git_dir(git_local_path), '%s is not git repository'.format(git_local_path)
        self.__repo = Repo(self.__local_path)
        pass

    def branches(self):
        """
        get all branch local and remote
        :return:
        """
        branches = self.__repo.remote().refs
        return [item.remote_head for item in branches if item.remote_head not in ['HEAD', ]]

    def checkout(self, branch: str):
        assert branch != '', 'branch name is empty.'
        self.__repo.git.checkout(branch)
        return

    def pull(self):
        #self.__repo.git.pull()
        pass

    def get_all_commit_info(self) -> List[GitLogObject]:
        """
        get all commit info
        :return:
        """
        all_commit_into: List[GitLogObject] = []
        branches = self.branches()
        for branch in branches:
            self.checkout(branch)
            self.__repo.git.reset()
            self.pull()
            master = self.__repo.head.commit
            self.__read_all_commit(master, all_commit_into)
            break
            pass
        return all_commit_into
        pass

    def __read_all_commit(self, commit: Commit, all_log: List[GitLogObject]):
        """
        read all commit by branch last commit
        :param commit:
        :param all_log:
        :return:
        """
        message = commit.message
        author = commit.author.name
        time = commit.committed_datetime
        obj = GitLogObject(author, message, time)
        all_log.append(obj)
        if not commit.parents:
            return
        self.__read_all_commit(commit.parents[0], all_log)
        pass

    pass
