import smtplib
import config

from CODE.Currency_Converter import rate


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Currency value Exceeded"
msg = "Hello, your currency value has exceeded.\nThe current value is" + rate

if float(rate) < 95.8:
    send_email(subject, msg)