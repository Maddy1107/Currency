import requests
import smtplib


def send_email(subject, msg):
    try:
        EMAIL_ADDRESS = "AKIAYPGMMA6SHIQ3O3PS"
        PASSWORD = "BK24AkU0wbGMREjTlmPiif1r4trYMiyXUwvtYQy3n5Oa"
        server = smtplib.SMTP('email-smtp.us-east-2.amazonaws.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('judodeb17@gmail.com', 'judodeb17@gmail.com', message)
        server.close()
        print("Success: Email sent!\n")
    except:
        print("Email failed to send.\n")


api_key = '0IGXMZC0WGW4OPGV'

from_curr = 'GBP'
to_curr = 'INR'

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_curr + '&to_currency=' + to_curr + '&apikey=' + api_key

response = requests.get(main_url)
output = response.json()

key = output['Realtime Currency Exchange Rate']
rate = key['5. Exchange Rate']
float_rate = round(float(rate), 2)
print(float_rate)

subject = "Currency value Exceeded"
msg = "Hello, your currency value has exceeded.\nThe current value is" + rate + "\n"

if float(rate) < 95.8:
    send_email(subject, msg)
