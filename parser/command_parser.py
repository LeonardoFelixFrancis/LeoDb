from command_types import OperationsEnum
from exceptions import InvalidOperation, InvalidCommand
from parser.target_table_factory import TargetTableFactory
from parser.target_column_factory import TargetColumnFactory
from parser.parser_utils import ParserUtils
from persistence.persistence_handler import BasePersistenceHandler, DbPersistenceHandler
from db_structure.database import DataBase
from data_models.connection import Connection
import json 

class CommandParser():

    valid_command_types = [
        'SELECT',
        'INSERT',
        'UPDATE',
        'DELETE',
        'CREATE'
    ]

    persistence_handler = BasePersistenceHandler()
    db_persistence_handler = DbPersistenceHandler()

    def __init__(self, message:str):
        self.message = message
    
    def get_field_from_connection_message(self, message:str, field:str):

        init_pivot = message.find(field) + len(field)
        end_line = message.find('\n', init_pivot)

        field = message[init_pivot:end_line]

        return field

    def command_from_connection(self, message:str, command_length:str):

        init_pivot = message.find('COMMAND:') + len('COMMAND:')

        end_pivot = init_pivot + command_length

        return message[init_pivot:end_pivot]

    def get_db_connection(self, message:str):

        database_name = self.get_field_from_connection_message(message, 'DATABASE:').strip()
        username = self.get_field_from_connection_message(message, 'USERNAME:').strip()
        password = self.get_field_from_connection_message(message, 'PASSWORD:').strip()
        command_length = int(self.get_field_from_connection_message(message, 'COMMAND_LENGTH:'))
        command = self.command_from_connection(message, command_length)

        # db_connection = {
        #     'database':database,
        #     'username':username.strip(),
        #     'password':password.strip(),
        #     'command_length':command_length,
        #     'command':command.strip()
        # }

        self.db_connection = Connection(database_name, username, password, command_length, command)

        return self.db_connection

    def define_command_type(self):

        message = self.db_connection.command

        first_space = message.find(' ')

        first_word = message[:first_space].upper()

        valid_command_types = [choice[1] for choice in OperationsEnum.choices]

        if first_word.upper() not in valid_command_types:
            return None
        
        command_type = OperationsEnum.hashed_choices.get(first_word.upper())

        if command_type is None:
            raise InvalidOperation(f'Unknown Operation Keyword: {first_word}')
        
        self.command_type = command_type

        return command_type

    def get_target_table(self, message:str):
        
        command_type = self.command_type

        target_table_factory = TargetTableFactory(command_type).get_target_table_finder()

        target_table = target_table_factory.get_target_table(message=message)

        return target_table
    
    def get_target_columns(self, message:str):
        
        command_type = self.command_type

        target_columns_factory = TargetColumnFactory(command_type).get_target_columns_checker(message=message)

        target_columns = target_columns_factory.get_target_columns(message=message)

        return target_columns
    
    


