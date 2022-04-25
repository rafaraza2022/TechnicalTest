from githubapi import GithubAPI
from database import Database
from flask_restful import Resource

class RepositoryAPI(Resource):
    """
        Class API used for the endpoint.  
    """
    def post(self, action, name):
        self.__api = GithubAPI()
        json_org = self.__api.orgs.get(name)
        repo = Repository(json_org)
        if(action == 'init_settings'):
            repo.initSettings()
        if(action == 'create_default_protected_branch'):
            repo.createDefaultProtectedBranch()
        if(action == 'update'):
            repo.update()
        if(action == 'fix'):
            repo.fixAutoIssue()
        if(action == 'scan'):
            repo.scan()

    def get(self):
        pass

class Repository:
    """
        Repository management class

        When a repository is created:
            - security settings are changed
            - webhook repository are changed to apply security rules on future branch
            - 2 default protected branch are created : main for deployement and develop, final version for develop
"""
    def __init__(self, _jsondata):
        self.__jsondata = _jsondata
        self.__api = GithubAPI()
        self.__db = Database()

    def initSettings(self):
        """
        Inits settings to define settings security
            endpoint : /repos/{owner}/{repo}
            security_and_analysis = {
                'advanced_security' = 'enabled',
                'secret_scanning' = 'enabled',
                'secret_scanning_push_protection' = 'enabled'
            }
        :return:
        """
        security_and_analysis = {
            'advanced_security': 'enabled',
            'secret_scanning': 'enabled',
            'secret_scanning_push_protection': 'enabled'
        }
        try:
            self.__api.repos.update(
                self.__jsondata['repository']['name'],
                owner = self.__jsondata['repository']['owner']['name']
            )
        except Exception as e:
            self.__db.save(self.id, 'repository', 'init_settings', e.getcode(), e.msg)
        else:
            self.__db.save(self.id, 'repository', 'init_settings', 200, 'OK')

    def initWebhook(self):
        """ Inits webhook for the repository. If protections are changed,  notify admin with @mention in an issue."""
        pass

    def createDefaultProtectedBranch(self):
        """
        uir : /orgs/{org}/repos
        Create 2 defaults protected branch :
            - main for the main branch
            - develop for development.
            1) Rules:
                Develop branch cannot be merged in main branch without automatized test validated
                Developper can't push without pull request validated
            settings :
                auto_init
        """

    def update(self):
        """ Function allow to update repository. Put changes in object in parameter. """
        pass

    def fixAutIssue(self):
        """Function allow to fix automatic issue. """
        pass

    def scan(self):
        """Function allow to launch scan""" 