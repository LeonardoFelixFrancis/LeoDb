class Column:

    def __init__(self, name, value = None, type=None, required=False) -> None:
        self.name = name
        self.value = value
        self.required = required

    def validate_self(self):
        pass

    def __eq__(self, other):
        
        if self.name == other.name:
            return True
        
        return False