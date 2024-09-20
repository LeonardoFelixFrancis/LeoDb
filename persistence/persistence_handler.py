import pickle
from db_structure import database

class PersistenceHandler: 

    def save_obj(self, obj, file_name):

        with open(file_name, 'wb') as file:
            pickle.dump(obj, file)

    def retrieve_obj(self, file_name):

        with open(file_name, 'rb') as file:
            instance = pickle.load(file)
        
        return instance
    
    