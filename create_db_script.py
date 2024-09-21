from db_structure.database import DataBase
from exceptions import DuplicationError
from persistence.persistence_handler import DbPersistenceHandler
import json

def create_db():

    db_persistence_handler = DbPersistenceHandler()

    db_name = input('Please provide the Database name: ')
    db_username = input('Please provide the Database Username: ')
    db_password = input('Please provide the Database password: ')
    
    new_db = DataBase(db_username, db_password, [], db_name)

    db_persistence_handler.add_db_to_db_list(new_db)

    db_persistence_handler.save_db(new_db)

    print(f'Database {db_name} was succesfuly created')

if __name__ == '__main__':
    create_db()