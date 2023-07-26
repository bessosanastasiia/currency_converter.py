import requests

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    converted_amount = data["rates"][to_currency] * amount
    return round(converted_amount, 2)

print("Welcome to Currency Converter!")
print("Supported currencies:")
print("USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, HKD, NZD\n")

amount = float(input("Enter amount: "))
from_currency = input("From currency: ")
to_currency = input("To currency: ")

converted_amount = currency_converter(amount, from_currency.upper(), to_currency.upper())

print(f"\n{amount} {from_currency.upper()} is equal to {converted_amount} {to_currency.upper()}").
