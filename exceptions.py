class InvalidOperation(Exception):

    def __init__(self, message, errors=[]):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
            
        # Now for your custom code...
        self.errors = errors

class InvalidCommand(Exception):

    def __init__(self, message, errors=[]):

        super().__init__(message)

        self.errors = errors

class InvalidTypeError(Exception):

    def __init__(self, message, errors=[]):

        super().__init__(message)

        self.errors = errors

class TypeValidationError(Exception):

    def __init__(self, message, errors=[]):

        super().__init__(message)

        self.errors = errors

class ConfigurationError(Exception):

    def __init__(self, message, errors=[]):
        
        super().__init__(message)

        self.errors = errors

class InvalidValueError(Exception): 

    def __init__(self, message, errors=[]): 

        super().__init__(message) 

        self.errors = errors

class TableBuildingError(Exception):

    def __init__(self, message, errors=[]):
        
        super().__init__(message)

        self.errors = errors

class InsertOperationError(Exception): 

    def __init__(self, message, errors=[]): 

        super().__init__(message)

        self.errors = errors

class NonExistentRegister(Exception):

    def __init__(self, messsage, errors=[]): 

        super().__init__(messsage)

        self.errors = errors