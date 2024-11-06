import os
from email.message import EmailMessage
import ssl
import smtplib

def EmailConfirmation(last_name, email_address, arrival_date, departure_date, people, room1_value, room2_value, password):
    email_sender = "fontaynepark@gmail.com"
    email_password = os.environ.get("EMAIL_PASSWORD")
    email_receiver = email_address

    subject = "Reservation at Fontayne Vacation Park"
    body = f""" 

    Hello Mr./Ms.{last_name},\n
    
    We trust this message finds you well and eagerly anticipating \n
    your upcoming visit to Fontayne Vacation Park. \n
    We wanted to provide you with some essential information to \n
    enhance your stay and offer details about your reservation:

    Arrival date:{arrival_date}
    Departure date:{departure_date}
    Number of guests: {people}
    Number of type 1 rooms: {room1_value}
    Number of type 2 rooms: {room2_value}
    Account password: {password}

    Your comfort and enjoyment are of utmost importance to us,\n
    and we are committed to ensuring your time with us is a memorable one.\n
    If you have any questions, special requests, or need assistance \n
    with anything during your stay, please do not hesitate to reach out \n
    to our dedicated team.

    We sincerely hope you have a wonderful and relaxing vacation at \n
    Fontayne Vacation Park. We look forward to welcoming you soon and \n
    are here to make your experience truly exceptional.   

    Warm regards,
    Fontayne Vacation Park
    """


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl. create_default_context()


    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smpt:
        smpt.login(email_sender, email_password)
        smpt.sendmail(email_sender, email_receiver, em.as_string())
