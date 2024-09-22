from db_structure.database import DataBase
from db_structure.table import Table
from db_structure.row import Row
from persistence.persistence_handler import DbPersistenceHandler
from authentication.db_authentication import DbAuthenticator
from data_models.connection import Connection

class DataEngine:
    
    def __init__(self, connection):
        self.connection = connection

    db_persistence_handler = DbPersistenceHandler()
    db_authenticator = DbAuthenticator()

    def retrieve_db_from_name(self, connection:Connection):

        database = self.db_persistence_handler.retrieve_db(connection.database_name)
        self.db_authenticator.authenticate(database, connection.username, connection.password)

        return database

    def retrieve_table_from_db(self, target_table:str, db:DataBase) -> Table:
        table = db.get_table(target_table)
        return table
    
    def retrieve_row_from_table(self, table:Table, columns_to_select:list[str], conditional=None) -> list[Row]:

        rows:Row = table.rows

        return_rows = []

        for row in rows:
            return_rows.append(row.get_slice(columns_to_select))

        return return_rows

        

