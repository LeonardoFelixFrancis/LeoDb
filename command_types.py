from enum import Enum

class OperationsEnum(Enum):

    SELECT = 0
    INSERT = 1
    UPDATE = 2 
    DELETE = 3

    choices = [
        (SELECT, 'SELECT'),
        (INSERT, 'INSERT'),
        (UPDATE, 'UPDATE'),
        (DELETE, 'DELETE')
    ]

    hashed_choices = {
        'SELECT':SELECT,
        'INSERT':INSERT,
        'UPDATE':UPDATE,
        'DELETE':DELETE
    }

