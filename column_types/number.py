from exceptions import InvalidTypeError,ConfigurationError

class Number:

    def __init__(self, max_digits:int=10, decimal_places:int=4, is_primary_key=False, auto_add=False, auto_add_value=1):

        self.max_digits = max_digits
        self.decimal_places = decimal_places

        self.validate_self()

        super().__init__(is_primary_key=is_primary_key)
    
    def validate_self(self): 

        try:
            self.max_digits = int(self.max_digits)
        except ValueError:
            raise InvalidTypeError(f'Max digits must be a number')            

        try:
            self.decimal_places = int(self.decimal_places)
        except ValueError:
            raise InvalidTypeError(f'Decimal places must be a number')            

    def validate_value(self, value:float):

        if not isinstance(value, float):
            raise InvalidTypeError(f'Value must be of float type')

        try:
            string_value = str(value)        
        except:
            raise InvalidTypeError(f'Cannot convert {value} to a string')
        
        try: 
            string_split = string_value.split('.')
        except:
            string_split = [string_value, '']

        if len(string_split[0]) > self.max_digits:
            raise ConfigurationError(f'Number cannot have more digits than: {value}')
        

        



