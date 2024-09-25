from parser.parser_utils import ParserUtils
from command_types import OperationsEnum

class TargetTypeFactory:

    def __init__(self, command_type:int):
        
        self.command_type = command_type
        
    def get_target_type_finder(self):

        match self.command_type:

            case OperationsEnum.CREATE:
                return CreateGetTargetTypes()
            case _:
                return None

class BaseGetTargetTypes():

    parser_utils = ParserUtils()

class CreateGetTargetTypes(BaseGetTargetTypes):

    def get_target_types(self, message):

        col_types = self.parser_utils.get_value_beetween_parenthesis(message)

        col_types = col_types.strip()
        col_types = col_types.split(',')
        col_types_return = []
        for cols in col_types:
            cols = cols.strip()
            col, col_type = cols.split(' ')
            col_types_return.append(col_type.strip())

        return col_types_return