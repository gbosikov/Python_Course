import datetime as dt
import requests

# что-то запутался

def currency_rates_adv(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    resp_text = response.text
    currency_idx = resp_text.find(code.upper())
    year = resp_text[resp_text.find('Date') + 12:resp_text.find('Date') + 16:]
    month = resp_text[resp_text.find('Date') + 9:resp_text.find('Date') + 11:]
    day = resp_text[resp_text.find('Date') + 6:resp_text.find('Date') + 8:]
    some_date = f'{year}-{month}-{day}'
    date_time_obj = dt.datetime.strptime(some_date, '%Y-%m-%d')

    if currency_idx == -1:
        return
    else:
        resp_text = resp_text[currency_idx:resp_text.find('</Value>', currency_idx)]
        nominal = float(resp_text[resp_text.find('<Nominal>') + 9:resp_text.find('</Nominal>')].replace(',', '.'))
        value = float(resp_text[resp_text.find('<Value>') + 7:].replace(',', '.'))

    result_value = round(value / nominal, 2)

    return result_value, date_time_obj

# kurs, date_value = currency_rates_adv("USD")
#
# empty = bool(not kurs and not date_value)
# if not empty and not isinstance(kurs, float):
#     raise TypeError("Неверный тип данных у курса")
# if not empty and not isinstance(date_value, dt.date):
#     raise TypeError("Неверный тип данных у даты")
# print(kurs, date_value)

print(currency_rates_adv("USD"))
