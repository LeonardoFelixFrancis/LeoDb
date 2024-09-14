from db_structure.column import Column
from exceptions import InsertOperationError

class Row: 

    def __init__(self, columns:list[Column]):

        self.columns = columns

class RowBuilder:

    def __init__(self):
        self.columns:list[Column] = []

    def add_columns(self, columns:list[Column], heading_columns:list[Column]):

        temp_columns = []

        for head_col in heading_columns:

            col = next((c for c in columns if c == head_col), None)

            if col is None and head_col.required:
                raise InsertOperationError(f'The table {head_col.name} is required, and is not informed in the insert')
            
            if col is None:
                col = Column(head_col.name, None, head_col.type, head_col.required)

            temp_columns.append(col)

        self.columns = temp_columns

        return self

    def build(self):
        return Row(self.columns)