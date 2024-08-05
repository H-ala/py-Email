import mysql.connector
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

cnx = mysql.connector.connect(username = 'root', password = 'Hosein13811234', host = '127.0.0.1', database = 'email')
cursor = cnx.cursor()

while(True):
    email = input('email: ')
    if re.fullmatch(regex,email):
        break
    else:
        print('Invalid Email\nEmail Format Must be: expression@string.string')

password = input('password: ')

query = 'INSERT INTO userpass (username, password) VALUES (%s, %s)'

cursor.execute(query, (email, password))
cnx.commit()
cnx.close()