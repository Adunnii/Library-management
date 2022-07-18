import smtplib
import ssl
import traceback
import socket

try:# Create your SMTP session
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server='smtp.gmail.com'
    port=465
    context=ssl.create_default_context()
    sender="oyinsofolahan@gmail.com"
    password='Kofoworola123'
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
    smtp.sendmail("oyinsofolahan@gmail.com", "sofolahanoyindamola@gmail.com", message)

    # Terminating the session
    smtp.quit()
    print("Email sent successfully!")


except smtplib.SMTPException:
    print( "Error: unable to send email")
    print(TracebackException)





