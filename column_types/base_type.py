class BaseType:

    def __init__(self, is_primary_key=False):
        self.is_primary_key = False

    def validate_self(self):
        pass

    def validate_value(self):
        pass 
