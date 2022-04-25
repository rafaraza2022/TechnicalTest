from flask import Flask
from flask_restful import Api
from webhook import Webhook
from config import Config, ConfigFileException, FormatConfigException
from organization import OrganizationAPI, Organization
from repository import RepositoryAPI
from branch import BranchAPI

import logging

#Read configuration
try:
    conf = Config()
except ConfigFileException:
    logging.critical(" Config file not found. Please add config.json file. End of the program.")
except FormatConfigException:
    logging.critical(" Format config is not fine. Please verify data infile config. End of the program.")
except ValueError as err:
    logging.critical(err.args[0])
else:
    #Initiate flask application
    app = Flask(__name__)
    api = Api(app)

    #Webhook listener
    api.add_resource(Webhook, '/')

    #add endpoint API
    api.add_resource(OrganizationAPI, '/organizationAPI/<action>/<name>')
    api.add_resource(RepositoryAPI, '/repository/<action>/<name>')
    api.add_resource(BranchAPI, '/repository/<action>/<name>')

    #Launch server
    if __name__ == '__main__':
        app.run(port=conf.port, host=conf.ip, debug=conf.debug)