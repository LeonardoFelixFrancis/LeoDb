from db_structure.database import DataBase
from db_structure.table import Table
from db_structure.row import Row
from persistence.persistence_handler import DbPersistenceHandler
from authentication.db_authentication import DbAuthenticator
from data_models.transaction import Transaction

class DataEngine:
    
    def __init__(self, transaction:Transaction):
        self.transaction = transaction

    db_persistence_handler = DbPersistenceHandler()
    db_authenticator = DbAuthenticator()
    
    def retrieve_db_from_name(self):

        database = self.db_persistence_handler.retrieve_db(self.transaction.target_database)
        is_authenticated = self.db_authenticator.authenticate(database, self.transaction.username, self.transaction.password)

        self.transaction.authenticated = is_authenticated

        return database

    def retrieve_table_from_db(self, db:DataBase) -> Table:
        table = db.get_table(self.transaction.target_table)
        return table
    
    def retrieve_row_from_table(self, table:Table, columns_to_select:list[str], conditional=None) -> list[Row]:

        rows:Row = table.rows

        return_rows = []

        for row in rows:
            return_rows.append(row.get_slice(columns_to_select))

        return return_rows

        

