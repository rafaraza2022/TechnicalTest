"""
    Github API management class
"""
import json
from exceptions import FormatConfigException, ConfigFileException
from ghapi.all import GhApi

class GithubAPI:
    def __init__(self):
        self.__filename = "configGithub.json"
        try:
            file = open(self.__filename)
        except FileNotFoundError:
            raise ConfigFileException
        else:
            try:
                config = json.load(file)
            except Exception:
                raise FormatConfigException
            else:
                if (len(config["github_token"]) == 0):
                    raise ValueError("Can you verify the github token ? ")
                if (len(config["organizations"]) == 0):
                    raise ValueError("You don't have organizations ! ")
                if (len(config["login"]) == 0):
                    raise ValueError("You don't have login for github ")
                self.__token = config["github_token"]
                self.__organizations = config["organizations"]
                self.__login = config["login"]
                self.__api = GhApi(owner=self.__login, token=self.__token)

    @property
    def organizations(self):
        """
        Get organizations
        :return: List of organizations associated to the login
        """
        result = []
        for elt in self.__organizations:
            result.append(self.__api.orgs.get(elt))
        return result

