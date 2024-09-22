import socket
import threading

from parser.command_parser import CommandParser
from db_structure.database import DataBase
from persistence.persistence_handler import DbPersistenceHandler

def main():

    persisten_handler = DbPersistenceHandler()

    command = f'INSERT INTO PERSON (NAME, AGE) VALUES("LEONARDO", 21)'

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

    print(f'Target table: {target_table}')
    print(f'Target columns: {target_columns}')

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