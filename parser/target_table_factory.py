from command_types import OperationsEnum
from exceptions import InvalidOperation, InvalidCommand

class TargetTableFactory:

    def __init__(self, operation_type:int):
        self.operation_type = operation_type

    def get_target_table_finder(self):

        if self.operation_type == OperationsEnum.SELECT:
            return SelectGetTargetTable()
        
        if self.operation_type == OperationsEnum.INSERT:
            return InsertGetTargetTable()
        
        if self.operation_type == OperationsEnum.UPDATE:
            return UpdateGetTargetTable()
        
        if self.operation_type == OperationsEnum.DELETE:
            return DeleteGetTargetTable()

        raise InvalidOperation(f'No valid operation was informed to the TargetTableFactory')        
    
class BaseSelectTargetTable: 

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

    

        



        
