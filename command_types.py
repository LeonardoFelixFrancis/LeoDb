from enum import Enum

class OperationsEnum():

    SELECT = 0
    INSERT = 1
    UPDATE = 2 
    DELETE = 3
    CREATE = 4
    ALTER = 5

    choices = [
        (SELECT, 'SELECT'),
        (INSERT, 'INSERT'),
        (UPDATE, 'UPDATE'),
        (DELETE, 'DELETE'),
        (CREATE, 'CREATE'),
        (ALTER, 'ALTER')
    ]

    hashed_choices = {
        'SELECT':SELECT,
        'INSERT':INSERT,
        'UPDATE':UPDATE,
        'DELETE':DELETE,
        'CREATE':CREATE
    }
