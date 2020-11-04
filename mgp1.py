import os
os.system('cls' if os.name == 'nt' else 'clear')
#https://stackoverflow.com/questions/2084508/clear-terminal-in-python
import sqlite3
conn = sqlite3.connect('practice.sql')

c = conn.cursor()

def main():

    loop = True
    while loop == True:
        print('Please choose one ')
        login = input('Registered (R) or Unregistered (U): ')
        if login.upper() == 'R':
            username = input('Enter your username: ')
            from getpass import getpass
            password = getpass(prompt = 'Enter your password: ', stream=None)
            #https://docs.python.org/3/library/getpass.html#getpass.getpass
            loop = False

        elif login.upper() == 'U':
            username = input('Enter a username: ')
            name = input('Enter your name: ')
            city = input('Enter your city: ')
            password = input('Enter your password: ')
            from datetime import datetime
            # date = strftime("%m%d%Y", 'now')
            #import today's date
            loop = False
        
        else:
            loop = True

        
   
    
    c.execute(""" INSERT INTO member (username, password, name, address) VALUES (:username, :password, :name, :address);
""", {'uid': username, 'pwd': password,'name': name, 'city': city, })

    return 

if __name__ == "__main__":
    main()                                                                                                                                         
