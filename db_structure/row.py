from db_structure.column import Column
from exceptions import InsertOperationError


class Row: 

    def __init__(self, columns:list[Column]):
        self.columns = columns
        self.columns_hash = {}

        for col in self.columns:
            self.columns_hash[col.name] = col

    def get_slice(self, columns_to_get:list[str]):
        
        cols_to_return = []

        for col in columns_to_get:
            if col in self.columns_hash:
                cols_to_return.append(col)

        return Row(cols_to_return)

