"""
    Branch management class

    This class permits:
        - change settings
        - do scan
        - create issue
"""
from githubapi import GithubAPI
from database import Database
from flask_restful import Resource

class BranchAPI(Resource):
    def post(self, action, name):
        self.__api = GithubAPI()
        json_org = self.__api.orgs.get(name)
        branch = Branch(json_org)
        if(action == 'init_settings'):
            branch.initSettings()
        if(action == 'setProtected'):
            branch.setProtected()
        if(action == 'scan'):
            branch.scan()
        if(action == 'fix'):
            branch.fixAutoIssue()


class Branch:
    def __init__(self, _jsondata):
        self.__jsondata = _jsondata
        self.__api = GithubAPI()
        self.__name = self.__jsondata['name']
        self.__id = self.__jsondata['id']
        self.data = self.__jsondata
        self.__db = Database()

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def initSettings(self):
        """
        Function initialise the fact that issue with mention will be created if outlines the protections that were added.
        :return:
        """
        pass

    def setProtected(self):
        pass

    def scan(self):
        pass

    def fixAutoIssue(self):
        pass