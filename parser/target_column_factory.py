from db_structure.column import Column
from command_types import OperationsEnum
from parser.parser_utils import ParserUtils
from typing import Union



class TargetColumnFactory:

    def __init__(self, operation_type:int):
        self.operation_type = operation_type

    def get_target_columns(self, message:str):

        if self.operation_type == OperationsEnum.SELECT:
            return SelectGetTargetColumns()
        
        if self.operation_type == OperationsEnum.INSERT:
            return InsertGetTargetColumns()
        
        if self.operation_type == OperationsEnum.DELETE:
            return DeleteGetTargetColumns()
        
        if self.operation_type == OperationsEnum.UPDATE:
            return UpdateGetTargetColumns()
        
class BaseGetTarget:

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

            column = Column(col)

            columns.append(column)

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

            column = Column(col_name)
            columns_list.append(column)

        return columns_list

