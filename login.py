import pyodbc
import os
from random import randrange
from datetime import timedelta
from datetime import datetime
import re
import uuid
try:
    conn = pyodbc.connect('Driver={Sql server};'
                          'server=DESKTOP-AOE0JS4\SQLEXPRESS;'
                          'Database=LMS;'
                          'Trusted_connection = yes;')
    cursor = conn.cursor()
    cursor.execute('Drop table if EXISTS Library_management')
    cursor.execute('CREATE  table   Library_management'
                   ' (username VARCHAR(50),password VARCHAR(10),email VARCHAR (30)UNIQUE )')
except Exception as e :
    print(e)



def begin():
    global option


print('Welcome to LMS')
option = input('Login or signup(login,signup):')


def login():
    if option == login:
        email = input('Enter email: ').strip()
        password = input('Enter password:').strip()
        cursor.execute('SELECT * FROM Library_management WHERE email=?, and password=?,'
                       ,  email, password)
        if cursor.fetchone() is not None:
            print('Login Successful')

    else:
        print('Login error')
        begin()


def signup():
    if option == signup:
        print('signup ')
        email: str = input('Enter email:').rstrip()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            print('valid email')
            password = input('Enter password:').rstrip()
            password2 = input('confirm password').rstrip()
            if password != password2:
                print('wrong password')
        password = input('Enter password:').rstrip()
        username = input('Username:').rstrip()
        cursor.execute('INSERT INTO Library_management VALUES(?,?,?)', (username, password, email))
        conn.commit()
        print('Signup successful,\n Login: ')
        signup()
        issue_books()



    def issue_books(self):
    id = input('Enter book id: ')
    current_date = datetime.now().strftime('%Y-%M_d% H%:M%:%S')
    if id in self.books_dict.keys():
        if not self.books_dict[id]['status'] == 'Available':
            print(f'This book is issued to {self.books_dict[id]["Lender_name"]} '
                  f'on {self.books_dict[id]["issue_date"]}')
            return self.issue_books()
        elif self.books_dict[id]['Status'] == 'Available':
            your_name = input('Enter your name: ')
            self.books_dict[id]['Lender name '] = your_name
            self.books_dict[id]['Issue date  '] = current_date
            self.books_dict[id]['Status '] = 'Already issued '
            print('Book issue successfully')
    else:
        print('Book not found .....')
        return self.issue_books()
def add_books(self):
        new_books = input('Enter book title:')
        if new_books == '':
            return self.add_books()
        else:
            with open(self.list_of_books, 'a') as bk:
                bk.writelines(f"{new_books}\n")

                def add_book():
                    cursor = conn.cursor()
                    id=input('Enter book id :')
                    Book_name =input('Enter Book Name :')
                    Book_author =input('Enter Book Author : ')
                    cursor.execute('insert into Author_Details(id,Book_name, Book_author,status) values ( "' + \
                        id,''',''' + Book_name + '","' + Book_author + '",'  '","available");')
                    conn.close()
                    print('\n\nNew Book added successfully')
                    wait =input('\n\n\n Press any key to continue....')


def search_book(field):
    cursor = conn.cursor()
    msg = 'Enter ' + field + ' Value :'
    title =input(msg)
    cursor.execute('select * from library_books where ' + field + ' like "%' + title + '%"')
    records = cursor.fetchall()
    print('Search Result for :', field, ' :', title)
    for record in records:
        print(record)
    conn.close()
    wait =input('\n\n\n Press any key to continue....')


