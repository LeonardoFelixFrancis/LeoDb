from db_structure.column import Column
from command_types import OperationsEnum
from parser.parser_utils import ParserUtils
from typing import Union



class TargetColumnFactory:

    def __init__(self, operation_type:int):
        self.operation_type = operation_type

    def get_target_columns_checker(self):

        # if self.operation_type == OperationsEnum.SELECT:
        #     return SelectGetTargetColumns()
        
        # if self.operation_type == OperationsEnum.INSERT:
        #     return InsertGetTargetColumns()
        
        # if self.operation_type == OperationsEnum.DELETE:
        #     return DeleteGetTargetColumns()
        
        # if self.operation_type == OperationsEnum.UPDATE:
        #     return UpdateGetTargetColumns()

        match self.operation_type:

            case OperationsEnum.SELECT:
                return SelectGetTargetColumns()
            
            case OperationsEnum.INSERT:
                return InsertGetTargetColumns()
            
            case OperationsEnum.DELETE:
                return DeleteGetTargetColumns()
            
            case OperationsEnum.UPDATE:
                return UpdateGetTargetColumns()
            case OperationsEnum.CREATE:
                return CreateGetTargetColumns()

            case _:
                return None
        
class BaseGetTarget:

    parser_utils = ParserUtils()

    def get_target_columns(self, message:str) -> list[Column]:

        columns_string = ParserUtils.get_values_beetween(message, self.l_word, self.r_word)

        if columns_string is None:
            return []

        columns_string = columns_string.strip()

        column_names_list = columns_string.split(',')

        columns = []

        for col in column_names_list:

            col = col.strip()
            col = col.lower()

            columns.append(col)

        return columns
    
class SelectGetTargetColumns(BaseGetTarget):

    l_word = 'SELECT '
    r_word = ' FROM'

class InsertGetTargetColumns(BaseGetTarget):

    l_word = '('
    r_word = ')'

class DeleteGetTargetColumns(BaseGetTarget):

    def get_target_columns(self, message: str) -> list[Column]:
        return []
    

class UpdateGetTargetColumns(BaseGetTarget):

    def get_target_columns(self, message: str) -> list[Column]:
        
        set_idx = ParserUtils.try_to_find_keyword(message, 0, 'SET') + 3

        where_idx = ParserUtils.try_to_find_keyword(message, set_idx, 'WHERE')

        if where_idx is None:
            end_idx = where_idx
        
        if where_idx is not None:
            end_idx = len(message) - 1

        columns_sub_str = message[set_idx:end_idx]

        columns_sub_str = columns_sub_str.strip()

        columns_values_list = columns_sub_str.split(',')

        columns_list = []

        for col in columns_values_list:

            col = col.strip()

            col_value = col.split('=')

            col_name = col_value[0].strip().lower()

            columns_list.append(col_name)

        return columns_list

class CreateGetTargetColumns(BaseGetTarget):

    def get_target_columns(self, message:str):

        cols_types = self.parser_utils.get_value_beetween_parenthesis(message, 1)

        col_types_splited = cols_types.split(',')

        columns = []

        for col in col_types_splited:
            col = col.strip()
            got_col, col_type = col.split(' ')
            columns.append(got_col)
        
        return columns
