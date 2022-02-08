import requests

def currency_rates(curr: str) ->float:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', json)

