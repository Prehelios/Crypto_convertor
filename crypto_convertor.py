import requests

def convert_crypto(to_currency, amount):
    url = f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={to_currency}'
    response = requests.get(url)
    data = response.json()
    converted_amount = data[to_currency] * amount
    return converted_amount

# list of currencies to convert to
currencies = ['USD', 'EUR', 'GBP', 'JPY']

# original amount and currency
amount = float(input("Enter the amount of BTC to convert: "))

# iterate through the list of currencies and print out the converted amount
for currency in currencies:
    result = convert_crypto(currency, amount)
    print(f'{amount} BTC = {result} {currency}')
