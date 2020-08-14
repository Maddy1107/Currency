import requests

api_key = '0IGXMZC0WGW4OPGV'

from_curr = 'GBP'
to_curr = 'INR'

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_curr + '&to_currency=' + to_curr + '&apikey=' + api_key

response = requests.get(main_url)
output = response.json()

key = output['Realtime Currency Exchange Rate']
rate = key['5. Exchange Rate']
float_rate = round(float(rate),2)
