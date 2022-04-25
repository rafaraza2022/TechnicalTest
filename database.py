import  datetime

class Database:
    """
        Database management class
        We assume that we have database class with some functions : connect, save, get, update
    """
    def __init__(self):
        self.__filename = "configDatabase.json"


    def connect(self):
        """
        Function to connect to database
        """
        pass

    def save(self, _id, _objectName, _action, _codeResult, _comment, _date=datetime.datetime.now()):
        """
            Function to save data in database 
        """
        print("Saved:", _id, _objectName, _action, _codeResult, _comment)
        pass


