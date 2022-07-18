import pypyodbc
import os
from datetime import timedelta, time, datetime
import re
import bcrypt
import smtplib
import ssl

try:
    conn = pypyodbc.connect('Driver={Sql server};'
                            'server=DESKTOP-AOE0JS4\SQLEXPRESS;'
                            'Database=LMS;'
                            'Trusted_connection = yes;')
    cursor = conn.cursor()


    # cursor.execute('Drop table  if EXISTS user_details')
    # cursor.execute('''CREATE TAxBLE user_details (firstname TEXT,
    # lastname TEXT, password VARCHAR(MAX),email VARCHAR (30)UNIQUE, role TEXT  DEFAULT 'USER' )''')
except Exception as e:
    print(e)

class User:
    user = ()

    @staticmethod
    def getUser():
        return User.user

    @staticmethod
    def setUser(userObject):
        User.user = userObject


def main():
    print('.............Welcome to LMS............')
    while True:
        option = int(input('1. login \n'
                           '2. Signup\n'))
        if option == 2:
            print(signup())
            break
        elif option == 1:
            print(login())
            break
        else:
            print("Wrong input... Please try again")
            continue


def display_book():
    cursor.execute('select* from book')
    print('\n\nbooks | author | ISBN | available'
          '\n _______________________________')
    for i in cursor.fetchall():
        print(f'{i[1]} | {i[2]} | {i[4]} | {i[-1]}')
    # conn.close()

    print('\n\n\n\n')
    mainpage()
    return


def add_book():
    try:
        cursor = conn.cursor()
        id = input('Enter book id :')
        Book_name = input('Enter Book Name :')
        Author_name = input('Enter Book Author : ')
        cursor.execute('''SELECT * FROM Author_details WHERE Book_name = ? and Author_name=? ''',[Book_name, Author_name])
        alreadyexsist=cursor.fetchall()
        if alreadyexsist:
            print(f'This book already exsist ....')
        else:
            cursor.execute('''INSERT INTO Author_details(id, Book_name, Author_name)
        VALUES(?,?,?)''', [id, Book_name, Author_name])
            conn.commit ()
            print('\n\nNew Book added successfully')
    except Exception :
            print('This book already exists ')
            mainpage()


def search_book():
        while True:
            print('Search for a book, please enter numbers between 1 and 2 ')
            option = int(input('1. Search For Book By Book Title \n'
                               '2. Search For Book By Author Name\n'
                               '3.Back to main page\n '))

            if option == 1:
                cur = conn.cursor()
                title = input('Enter  name of book: ').lower()
                cur.execute("SELECT author, book_name, ISBN FROM book WHERE book_name = ?", [title])
                records = cur.fetchone()
                print('book author: ' + records[0])
                print('book name: ' + records[1])
                print('ISBN: ' + records[2])
                # conn.close()
            elif option == 2:
                cursor = conn.cursor()
                author = input('Enter  name of author: ')
                cursor.execute("SELECT  book_name, ISBN FROM book WHERE author = ?", [author])
                records = cursor.fetchall()
                for record in records:
                    print('book name: ' + record[0])
                    print('book ISBN: ' + record[1])
                    # conn.close
                    break
            elif option==3:
                mainpage()
            else:
                print('Book not found ....')
                search_book()



def borrow_book():
    DATE = 7
    today = datetime.now().date()
    return_date = today + timedelta(days=DATE)
    while True:
        cursor = conn.cursor()
        print('\n  BOOK ISSUING  ')
        Book_name = input('Enter book name:')
        email = input('Enter your email')
        Book_author = input('Enter book author:')
        cursor.execute('SELECT* from book WHERE book_name=?', [Book_name])
        book_found = cursor.fetchone()
        STATUS = 'ISSUE'
        if book_found[-1].lower() == 'available':
            print('date to be returned :\n ', return_date)
            print('You can only borrow a book for 7 days .....')
            print('date taken :\n ', today)
            cursor.execute('''INSERT INTO library_log( Book_name, email,Book_Author, status,date_taken,date_return)
                    VALUES(?,?,?,?,?,?)''', [Book_name, email, Book_author, STATUS, today, return_date])
            sql_book = f"update book set status='issue' where id = '{str(book_found[0])} ' "
            cursor.execute(sql_book)
            conn.commit()
            print('\n\n\n Book issued successfully')
            continue
        else:
            print('\n\nBook is not available for ISSUE... ')
        while today >= return_date:
            try:  # Create your SMTP session
                smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server = 'smtp.gmail.com'
                port = 465
                context = ssl.create_default_context()
                sender = "oyinsofolahan@gmail.com"
                password = input('Enter your password: ')
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender, password)
                    print('It worked!!!')

                # Use TLS to add security
                # smtp.starttls()

                # User Authentication
                smtp.login("oyinsofolahan@gmail.com", "Kofoworola123")

                # Defining The Message
                message = "This message is from LMS library , a reminder to return the book you borrowed"

                # Sending the Email
                # set up gmail and turn off the less secure property.
                smtp.sendmail("oyinsofolahan@gmail.com", User.getUser()[3], message)

                # Terminating the session
                smtp.quit()
                print("Email sent successfully!")


            except smtplib.SMTPException:
                print("Error: unable to send email")
                borrow_book()
                mainpage()


def mainpage():
    print('.............Welcome to LMS............')
    print('(1) Display books \n'
          '(2) Search for books\n'
          '(3) Borrow books\n'
          '(4) Add books\n'
          '(5) Log out')

    while True:
        option = input('input one option : ')
        if option == '1':
            display_book()
            break
        elif option == '2':
            search_book()
            break
        elif option == '3':
            borrow_book()
        elif option == '4':
            print(add_book())
            break
        elif option == '5':
            print(main())
            break
        else:
            print('Invalid option.. ')
            mainpage()


def login():
    while True:
        email = input('Enter your email:').strip()
        password = input('Enter password:').strip()
        cursor.execute('SELECT * FROM user_details WHERE email=?', [email])
        user = cursor.fetchone()
        # this is to set global user object
        User.setUser(user)
        if not user:
            print('Invalid Login Credentials. Please try again')
            continue
        if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(user[2], 'utf-8')):
            print('Login successful')
            mainpage()
        return


def signup():
    print('signup ')
    try:
        FirstName = input('Enter your First name:').strip()
        lastName = input('Enter your Last name :').strip()
        while True:
            email = input('Enter email:').strip()
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not re.search(regex, email):
                print('invalid email')
                continue
            cursor.execute('SELECT  email from user_details where email=?', [email])
            if cursor.fetchone():
                print('Email already exist.....Try another email')
                continue
            salt = bcrypt.gensalt()
            password = input('Enter password: ').strip()
            password2 = input('Confirm Password: ').strip()
            hashedPassword = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
            if password != password2:
                print("Passwords does not match. Re enter both passwords")
                break
            cursor.execute('INSERT INTO user_details (firstname, lastname , password, email) VALUES(?,?,?,?)',
                           [FirstName, lastName, hashedPassword, email])
            conn.commit()
            print(cursor.rowcount, "row count")
            if cursor.rowcount > 0:
                print('Signup successful,\n Login: ')
                login()
                return
    except Exception as e:
        print(e)


main()
