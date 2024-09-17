from db_structure.database import DataBase

class User:

    def __init__(self, username:str, password:str, databases:list[DataBase]):

        self.databases = databases
        self.username = username
        self.password = password
    
    
