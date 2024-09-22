from command_types import OperationsEnum
from exceptions import InvalidOperation, InvalidCommand
from parser_utils import ParserUtils

class TargetTableFactory:

    def __init__(self, operation_type:int):
        self.operation_type = operation_type

    def get_target_table_finder(self):
        
        match self.operation_type:

            case OperationsEnum.SELECT:
                return SelectGetTargetTable()
            
            case OperationsEnum.INSERT:
                return InsertGetTargetTable()
            
            case OperationsEnum.UPDATE:
                return UpdateGetTargetTable()
            
            case OperationsEnum.DELETE:
                return DeleteGetTargetTable()
            
            case OperationsEnum.CREATE:
                return CreateGetTargetTable()
            case _:
                raise InvalidOperation(f'No valid operation was informed to the TargetTableFactory')

    
class BaseSelectTargetTable: 

    parser_utils = ParserUtils()

    pivot_keyword = ''  

    def get_target_table(self, message:str):

        pivot_index = message.rfind(self.pivot_keyword)

        pivot_first_next_space = message.find(' ', pivot_index)
        other_next_space = message.find(' ', pivot_first_next_space)
        
        i = pivot_first_next_space + 1
        while message[i - 1] == ' ':
            
            if i == len(message) - 1:
                raise InvalidCommand(f'No Table informed')
            
            other_next_space = message.find(' ', i)
            i += 1

        if other_next_space == -1:
            target_table_string = message[pivot_first_next_space + 1:].strip()
        else:
            target_table_string = message[pivot_first_next_space + 1 : other_next_space].strip()

        if target_table_string is None or target_table_string == '':
            raise InvalidCommand(f'No Table informed')

        return target_table_string

class SelectGetTargetTable(BaseSelectTargetTable):

    pivot_keyword = 'FROM'

class InsertGetTargetTable(BaseSelectTargetTable):

    pivot_keyword = 'INTO'

class UpdateGetTargetTable(BaseSelectTargetTable):

    pivot_keyword = 'UPDATE'

class DeleteGetTargetTable(BaseSelectTargetTable):

    pivot_keyword = 'FROM'

class CreateGetTargetTable(BaseSelectTargetTable):

    def get_target_table(self, message: str):
        
        table = self.parser_utils.get_values_beetween(message, 'TABLE', '(')
        
        return table.strip() 

    

        



        
