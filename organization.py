"""
 organization management class

 When an organization is created:
    - security settings are changed
"""

from flask_restful import Resource
from githubapi import GithubAPI
from database import Database

class OrganizationAPI(Resource):
    def post(self, action, name):
        self.__api = GithubAPI()
        json_org = self.__api.orgs.get(name)
        org = Organization(json_org)
        if(action == 'init_settings'):
            org.initSettings()
        if(action == 'update'):
            org.update()
        if(action == 'fix'):
            org.fixAutoIssue()


class Organization:
    def __init__(self, _jsondata):
        self.__jsondata = _jsondata
        self.__api = GithubAPI()
        self.login = self.__jsondata['login']
        self.id = self.__jsondata['id']
        self.data = self.__jsondata
        self.__db = Database()

    def initSettings(self):
        """
        Function permits to update organization settings
        :return:
        """
        try:
            self.__api.orgs.update(self.login,
                default_repository_permission='write',
                members_can_create_repositories=True,
                members_can_create_internal_repositories=True,
                members_can_create_private_repositories=True,
                members_can_create_public_repositories=True,
                members_can_create_pages=True,
                members_can_create_private_pages=True,
                members_can_fork_private_repositories=True
            )
        except Exception as e:
            self.__db.save(self.id, 'organization', 'init_settings', e.getcode(), e.msg)
        else:
            self.__db.save(self.id, 'organization', 'init_settings', 200, 'OK')

    def update(self, _args):
        pass

    def fixAutoIssue(self):
        pass