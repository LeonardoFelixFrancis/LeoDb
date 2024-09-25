from column_types.base_type import BaseType

class varChar(BaseType):

    def __init__(self, max_length=255, is_primary_key=False):
        super().__init__(is_primary_key=is_primary_key)
        self.max_length = max_length
