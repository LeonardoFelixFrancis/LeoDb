from command_types import OperationsEnum
from parser.parser_utils import ParserUtils

class ValuesFactory:

    def __init__(self, operation_type:int): 

        self.operation_type = operation_type

    def get_values_checker(self): 
        
        match self.operation_type:
            case OperationsEnum.INSERT:
                return InsertValueChecker()
            case OperationsEnum.UPDATE:
                return UpdateValueChecker()
        
        return None
    
class InsertValueChecker():

    parser_utils = ParserUtils()

    def get_values(self, message:str):

        values_idx = self.parser_utils.try_to_find_keyword(message=message, start_index=0, keyword_to_check='VALUES')

        first_parenthesis = self.parser_utils.try_to_find_keyword(message=message, start_index=values_idx, keyword_to_check='(')
        last_parenthesis = self.parser_utils.try_to_find_keyword(message=message, start_index=values_idx, keyword_to_check=')')

        values = self.parser_utils.get_values_beetween(message=message, start_pivot=first_parenthesis+1, end_pivot=last_parenthesis)

        values = values.split(',')
        values = [value.strip() for value in values]

        return [value.strip('"') for value in values]

class UpdateValueChecker():

    parser_utils = ParserUtils()

    def get_values(self, message:str):

        set_idx = self.parser_utils.try_to_find_keyword(message=message, start_index=0, keyword_to_check='SET')
        where_idx = self.parser_utils.try_to_find_keyword(message=message, start_index=set_idx, keyword_to_check='WHERE')

        col_value_pairs = self.parser_utils.get_values_beetween(message=message, start_pivot=set_idx, end_pivot=where_idx)

        col_value_pairs = col_value_pairs.split(',')

        values = []

        for col_value in col_value_pairs:
            col_value = col_value.strip()
            value = col_value.split('=')[1]
            value = value.strip('"')
            values.append(value)

        return values


            
        
