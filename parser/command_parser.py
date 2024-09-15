from command_types import OperationsEnum
from exceptions import InvalidOperation, InvalidCommand
from parser.target_table_factory import TargetTableFactory
from parser.target_column_factory import TargetColumnFactory

class CommandParser():

    valid_command_types = [
        'SELECT',
        'INSERT',
        'UPDATE',
        'DELETE'
    ]

    def __init__(self, message:str):
        self.message = message
    
    def define_command_type(self):

        first_space = self.message.find(' ')

        first_word = self.message[:first_space].upper()

        if first_word.upper() not in self.valid_command_types:
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
    
    


