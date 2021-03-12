import smtplib
from email.message import EmailMessage


def mail(email, otp):
    message = EmailMessage()
    message.set_content('Your OTP for UnclePark is ' + otp)
    
    message['Subject'] = 'OTP for UnclePark'
    message['From'] = 'testid.for.pythonprojects@gmail.com'
    message['To'] = email
    # message['To'] = ['agrawal.kashish1907@gmail.com', 'kashish.agrawal1907@gmail.com']

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('testid.for.pythonprojects@gmail.com', 'iamtestid')
    server.send_message(message)
    server.quit()
