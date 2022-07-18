from dataclasses import field
from logging import exception

import bcrypt
import sendgrid
import os
from sendgrid.helpers.mail import *

# a salt is a random alphanumeric value generated
# by the bcrypt package.
salt = bcrypt.gensalt()

# password = input('enter your password: ')

# encrypt the password using the generated salt above.
# bytes() - is a function that turns strings to bytes, using character encoding
# in this case we used the UTF-8 character encoding.
# hashedPassword = bcrypt.hashpw(bytes(password, 'utf-8'), salt)

# print(hashedPassword)

# decrypt the password and checks the original
# password against the decrypted password
# Use this for LOGIN only.
# step 1 - fetch the user details based on email
# step 2 - extract password from the tuple.
# currentUser = fetchone()
# print(currentUser)
# output -> (victor@gmail.com, 2b$12$97WeVRaPCrXg1XNbUjvM8Om627u1NhSOeuL.nh0UCsbCWDck3JycO)
# currentUser[1]
# bcrypt.checkpw(bytes(password, 'utf-8'), currentUser[1])
# NOTE -> password is coming from the user, currentUser[1] is from the DB
# if bcrypt.checkpw(bytes(password, 'utf-8'), hashedPassword):
#     print('match')
# else:
#     print('wrong input')
# set SENDGRID_API_KEY=YOUR_API_KEY
# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
# from_email = Email("Raheemahoyindamola@outlook.com")
# to_email = To("kofosofolahan@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)
import pypyodbc
import os
from random import randrange
from datetime import timedelta, time, datetime, date
import re
import uuid as v4
import bcrypt

conn = pypyodbc.connect('Driver={Sql server};'
                      'server=DESKTOP-AOE0JS4\SQLEXPRESS;'
                      'Database=LMS;'
                      'Trusted_connection = yes;')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE library_log
# (Book_Name varchar(70) not null ,
# Book_Author varchar(50) not null,
# Status VARCHAR(10) not null ,
# date_taken DATE not null,
# date_return DATE not null
# )
# ''')
# def issue_book():
#     cursor = conn.cursor()
#     print('\n BOOK ISSUE  ')
#     print('-' * 120)
#     Book_name = input('Enter book name:')
#     Book_author = input('Enter book author:')
#     status='Available'
#     result = status
#     date_taken = datetime.now()
#     date_return = input('Enter day of return:')
#     if result == 'available':
#         cursor.execute('''INSERT INTO library_log( Book_name, Book_Author, status,date_taken,date_return)
#                 VALUES(?,?,?,?)''', Book_name, Book_author,status, date_taken, date_return)
#         sql_book = 'update book set status="issue" where id =' + Book_name + ';'
#         cursor.execute(sql_book)
#         print('\n\n\n Book issued successfully')
#     else:
#         print('\n\nBook is not available for ISSUE... Current status :')
# issue_book()


def borrow_book():
    while True:
        cursor = conn.cursor()
        print('\n  BOOK ISSUING  ')
        Book_name = input('Enter book name:')
        Book_author = input('Enter book author:')
        cursor.execute('SELECT* from book WHERE book_name=?', [Book_name])
        book_found = cursor.fetchone()
        STATUS = 'ISSUE'
        if book_found[-1].lower() == 'available':
            DATE = 7
            today = datetime.now().date()
            return_date = today + timedelta(days=DATE)
            print(return_date)
            print(today)
            # if return_date >  :
            if today >= return_date:
                print(return_date)
            cursor.execute('''INSERT INTO library_log( Book_name, Book_Author, status,date_taken,date_return)
                    VALUES(?,?,?,?,?)''', [Book_name, Book_author, STATUS, today, return_date])
            sql_book = f"update book set status='issue' where id = '{str(book_found[0])} ' "
            cursor.execute(sql_book)
            print('\n\n\n Book issued successfully')
            break
        else:
            print('\n\nBook is not available for ISSUE... ')
borrow_book()
