import socket
import threading

from parser.command_parser import CommandParser
from db_structure.database import DataBase
from persistence.persistence_handler import DbPersistenceHandler
from data_models.transaction import Transaction
from authentication.db_authentication import DbAuthenticator
from data_engine.db_engine import DataEngine

def main():

    persisten_handler = DbPersistenceHandler()
    db_authenticator = DbAuthenticator()
    

    command = f'CREATE TABLE PERSON (NAME VARCHAR(50), NUMBER(18) INT, SURNAME VARCHAR(50))'

    message = f'''DATABASE:LEODB
                  USERNAME:LEONARDO
                  PASSWORD:123
                  COMMAND_LENGTH:{len(command)}
                  COMMAND:{command}
               '''

    message = message.upper()
    command_parser = CommandParser(message)
    
    connection = command_parser.get_db_connection(message)

    print(connection)

    command_parser.define_command_type()

    target_table = command_parser.get_target_table(connection.command)
    target_columns = command_parser.get_target_columns(connection.command)
    values = command_parser.get_values(connection.command)
    target_types = command_parser.get_target_types(connection.command)

    transaction = Transaction(target_table=target_table,
                              target_columns=target_columns,
                              target_database=connection.database_name,
                              target_types=target_types,
                              values=values,
                              authenticated=False,
                              operation_type=command_parser.command_type,
                              username=connection.username,
                              password=connection.password)
    

    
    print(transaction)

    data_engine = DataEngine(transaction)

    database = data_engine.retrieve_db_from_name()
    target_table = data_engine.retrieve_table_from_db(database)

    print(target_table)

    #message = input('Please inform a SQL command: ')

    # command = 'SELECT NAME, AGE, SURNAME FROM PERSON'

    

    # print(connection)

    # message = connection.get('command')

    # command_parser.define_command_type()
    
    # print(f'Target table: {command_parser.get_target_table(message)}')
    
    # columns_names = command_parser.get_target_columns(message)
    # columns_names = [column_name.name for column_name in columns_names]

    # print(f'Target columns: {columns_names}')

# IP = '0.0.0.0'
# PORT = 9999

# def main():

#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((IP,PORT))
#     server.listen(5)

#     print(f'[*] Ouvindo em {IP}:{PORT}')

#     while True:
#         client,address = server.accept()
#         print(f'Conexão recebida de: {address[0]}:{address[1]}')
#         client_handler = threading.Thread(target=handle_client, args=(client,))
#         client_handler.run()

# def handle_client(client):

#     with client as sock:

#         buffer_size = 1024
#         message = b''

#         while True:
#             packet = sock.recv(buffer_size)
#             message += packet
#             if len(packet) < buffer_size:
#                 break

#         # treated_command = command_parser(message)

#         # raw_response = command_engine(treated_command)

#         # response response_builder(raw_response)

#         sock.send()

main()