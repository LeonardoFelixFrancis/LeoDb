
from db_structure.database import DataBase
from exceptions import DuplicationError, NonExistentRegister
from pathlib import Path
import pickle
import json




class BasePersistenceHandler: 

    def save_obj(self, obj, file_name):

        with open(file_name, 'wb') as file:
            pickle.dump(obj, file)

    def retrieve_obj(self, file_name):

        with open(file_name, 'rb') as file:
            instance = pickle.load(file)
        
        return instance
    
class DbPersistenceHandler(BasePersistenceHandler):

    def save_db(self, db:DataBase): 
        self.save_obj(db, db.get_file_name(db.name))

    def retrieve_db(self, db_name:str) -> DataBase: 

        if self.check_if_db_exists(db_name):
            db = self.retrieve_obj(db.get_file_name(db.name))
            return db
        
        raise NonExistentRegister(f'Informed database does not exists')
    
    def read_databases_from_db_json(self) -> dict: 

        databases = {}

        if Path('databases.json').is_file():
            with open('databases.json', 'r') as f:
                databases = json.load(f)

        return databases

    def check_if_db_exists(self, db_name:str):

        databases = self.read_databases_from_db_json()

        if db_name in databases:
            return True
        
        return False
    
    def add_db_to_db_list(self, db:DataBase): 
        
        databases = self.read_databases_from_db_json()

        if self.check_if_db_exists(db.name):
            raise DuplicationError(f'Database {db.name} already exists')

        databases[db.name] = db.get_file_name(db.name)

        with open('databases.json', 'w') as f: 
            json.dump(databases, f)

        

    