from flask_restful import Resource
from flask import request
from issue import Issue
from datetime import datetime
from organization import  Organization
from repository import  Repository
from branch import Branch

"""
Webhook management class

We assume that we have function permits to analyse_webhook and returns action_object  
  
"""

def analyse_webhook(_json_data):
    """
    Function permits to analyse_webhook and returns action_object
    action can be : created, updated and deleted
    object can be : organization, repository, branch
    :param _json_data:
    :return: action_object
    """
    print("Received post and analyze json - Return action and ")
    pass

class Webhook(Resource):
    def post(self):
        json_data = request.json
        action_object = analyse_webhook(json_data)
        if(action_object == 'created_organization'):
            organization = Organization(json_data)
            organization.initSettings()
        elif(action_object == 'created_repository'):
            repository = Repository(json_data)
            repository.initSettings()
            repository.initWebhook()
            repository.createDefaultProtectedBranch()
        elif(action_object == 'created_branch'):
            branch = Branch(json_data)
            if(branch.name !=  'develop' and branch.name !=  'main'):
                branch.initSettings()
        else:
            Issue.createUnrecognizedWebhook("unrecognized_webhook", json_data, datetime.now())

