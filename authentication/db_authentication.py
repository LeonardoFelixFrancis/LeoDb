from db_structure.database import DataBase
from exceptions import UnauthorizedAccess, UserNotFound

class DbAuthenticator:

    def authenticate(self, db:DataBase, username:str, password:str):

        treated_username = username.lower().strip()
        treated_password = password.lower().strip()

        db_treated_username = db.username.lower().strip()
        db_treated_password = db.password.lower().strip()

        if treated_username != db_treated_username:
            raise UserNotFound(f'The username informed for the Database is not correct')
        
        if db_treated_password != treated_password:
            raise UnauthorizedAccess(f'The informed password is not correct')
        
        return True