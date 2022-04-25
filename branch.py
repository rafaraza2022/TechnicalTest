from githubapi import GithubAPI
from database import Database
from flask_restful import Resource

class BranchAPI(Resource):
    """
        Class API used for the endpoint.  
    """
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
    """
    Branch management class

    This class permits:
        - change settings
        - do scan
        - create issue
    """
    def __init__(self, _jsondata):
        self.__jsondata = _jsondata
        self.__api = GithubAPI()
        self.__name = self.__jsondata['name']
        self.__id = self.__jsondata['id']
        self.data = self.__jsondata
        self.__db = Database()

    @property
    def name(self):
        """ Getter for name """
        return self.__name

    @property
    def id(self):
        """ Getter for id """
        return self.__id

    def initSettings(self):
        """Function initialise the fact that issue with mention will be created if outlines the protections that were added."""
        pass

    def setProtected(self):
        """Function allows to set new branch protected branch """
        pass

    def scan(self):
        """Function allows to scan branch """
        pass

    def fixAutoIssue(self):
        """Function allow to fix automatic issue. """
        pass