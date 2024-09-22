from dataclasses import dataclass

@dataclass
class Connection:

    database_name:str
    username:str
    password:str
    command_length:int
    command:str

