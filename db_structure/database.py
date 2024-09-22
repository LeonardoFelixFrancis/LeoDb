from db_structure.table import Table
from exceptions import NonExistentRegister, DuplicationError


class DataBase():

    def __init__(self, username:str, password:str, tables:list[Table], db_name:str):

        self.username = username
        self.password = password
        self.tables = tables
        self.name = db_name

        self.table_hash = {}

        for table in tables:

            if table.name in self.table_hash:
                raise DuplicationError(f'Table with the name {table.name} already exists in the databse')
            
            self.table_hash[table.name] = table

    def get_table(self, table_name:str):

        if table_name not in self.table_hash:
            raise NonExistentRegister(f'The informed table does not exists in the database')

        return self.table_hash.get(table_name)

    def add_table(self, table:Table):

        if table.name in self.table_hash:
            raise DuplicationError(f'Table with the name {table.name} already exists in the databse')

        self.table_hash[table.name] = table
        self.tables = table

    def delete_table(self, table:Table): 

        if table.name not in self.table_hash:
            raise NonExistentRegister(f'Table with the name {table.name} does not exists in the databse')
        
        del self.table_hash[table.name]

    