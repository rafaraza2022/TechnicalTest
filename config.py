import json
from exceptions import ConfigFileException, FormatConfigException

class Config(object):
    """
    Config management class
        You have to define the file config as config.json
    """
    def __init__(self):
        self.__filename = "config.json"
        self.__debug = 0
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
                if(len(config["ip"]) < 7 ):
                    raise ValueError("The ip seems not good. Can you verify your ip please? ")
                if(len(str(config["port"])) ==0 ):
                    raise ValueError("The port seems not good. Can you verify the port ?  ")
                self.__ip = config["ip"]
                self.__port = config["port"]
                self.__debug = config["debug"]

    @property
    def port(self):
        """
        Get port
        :return: Application port
        """
        return self.__port


    @property
    def ip(self):
        """
        Get ip in the format x.x.x.x
        :return: IP
        """
        return self.__ip


    @property
    def debug(self):
        """
        Get debug boolean. Yes if you want debug mode, no otherwise
        :return: Boolean debug
        """
        return self.__debug


