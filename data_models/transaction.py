from dataclasses import dataclass
from command_types import OperationsEnum
from typing import Any

@dataclass
class Transaction:

    username:str
    password:str
    target_table:str
    target_columns:list[str]
    target_database:str
    target_types:list[str]
    operation_type:int
    values:list[Any]
    authenticated:bool

    def __str__(self) -> str:
        
        return f'''
                Target Database: {self.target_database}
                Target Table: {self.target_table}
                Target Columns: {','.join(self.target_columns) if self.target_columns is not None else 'None'}
                Target Types: {','.join(self.target_types) if self.target_types is not None else 'None'}
                Operation Type: {OperationsEnum.get_description(self.operation_type)}
                Values: {','.join(self.values) if self.values is not None else 'None'}
                Authenticated: {self.authenticated}
                Username: {self.username}
                Password: {self.password}
                '''