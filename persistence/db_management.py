from db_structure.database import DataBase

class DbManagement:

    def __init__(self):

        self.databases = {}

    def add_db(self, database:DataBase):
        self.databases[database.db_name] = f'{database.db_name}.leodb'

    def remove_db(self, database:DataBase):
        del self.databases[database.db_name] 