from db_structure.database import DataBase

class DbManagement:

    def __init__(self):

        self.databases = {}

    def add_db(self, database:DataBase):
        self.databases[database.schema_name] = f'{database.schema_name}.leodb'

    def remove_db(self, database:DataBase):
        del self.databases[database.schema_name] 