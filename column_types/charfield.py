from exceptions import InvalidTypeError, TypeValidationError, InvalidValueError
from column_types.base_type import BaseType

class Charfield(BaseType):

    ROOF_MAX_LENGTH = 255

    def __init__(self, max_length=255, is_primary_key=False): 
        self.max_length = max_length
        self.validate_self()

        super().__init__(is_primary_key=is_primary_key)

    def validate_self(self):

        if self.max_length > self.ROOF_MAX_LENGTH:
            raise TypeValidationError(f'Charfield type cannot have a max_legth larger than 255')
        
    def validate_value(self, value):

        if len(value) > self.max_length: 
            raise InvalidValueError(f'Value cannot have a length larger than {self.max_length}, and the informed value have a length of: {len(value)}')
    