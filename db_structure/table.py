from db_structure.row import Row
from db_structure.column import Column
from exceptions import TableBuildingError, InsertOperationError
from row import RowBuilder

class Table: 

    row_builder = RowBuilder()

    def __init__(self, name:str, heading_cols:list[Column]):

        self.rows = []
        self.heading_cols = heading_cols
        self.name = name

        self.required_cols = [col for col in self.heading_cols if col.required == True]

        self.heading_cols_hash = {}

        for col in heading_cols:

            self.heading_cols_hash[col.name] = col

    def insert_into(self, columns:list[Column]):
        
        row = self.row_builder.add_columns(columns, self.heading_cols).build()

        self.rows.append(row)

class TableBuilder:

    def __init__(self):
        self.heading_cols = []
        self.cols_names = []

    def add_heading_cols(self, column:Column):

        if column.name in self.cols_names:
            raise TableBuildingError(f'Cannot have duplicate tables')

        self.heading_cols.append(column) 
        self.cols_names.append(column.name)

    def build(self):
        return Table(heading_cols=self.heading_cols)


    




