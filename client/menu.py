import socket
import os
from tkinter.filedialog import askopenfilename

from helpers import error_message, success_message, clear_screen, forced_input
from actions import login, create_account, send_file_to_server, download_file_from_server

def launchMenu():
      clear_screen()
      files_list = []
      email, username = '1', '1'
      connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      connection.connect((os.getenv('HOST'), int(os.getenv('PORT'))))
      #email, username = login(connection)
      while True:
            try:
                  connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  connection.connect((os.getenv('HOST'), int(os.getenv('PORT'))))
                  if bool(username) and bool(email):
                        print(f'Welcome {username} ({email}) to the file sharing system')
                        print('1. Upload File.')
                        print('2. Download File.')
                        print('0. Exit.')
                        option = input('What Would You Like To Do : ')
                        if option == '1':
                              file_path = askopenfilename()
                              if not file_path:
                                    error_message('File not selected')
                                    continue

                              if send_file_to_server(connection, file_path):
                                    pass
                                    # success_message('File uploaded successfully')
                              else:
                                    continue

                        elif option == '2':
                              download_file_from_server(connection, 'please-work.txt', './')
                              pass
                        elif option == '0':
                              clear_screen()
                              print('Thank you for using our system')
                              break

                        else:
                              error_message('Invalid Option, please try again')
                  else:
                        # Let's create an account
                        print('This is your first time using our system in this device')
                        print('Please Create an account first')
                        email = forced_input('Email : ')
                        username = forced_input('Username : ')
                        create_account(connection, {
                              'email': email,
                              'username': username
                        })
                  connection.close()


            except Exception as e:
                  error_message(str(e))


