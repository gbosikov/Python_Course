from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    a = line.replace('-', ' ')[:15].replace(' ', '')
    b = line[line.find('"') + 1:line.find('"') + 4]
    c = line[line.find('"') + 5:line.find('"') + 5 + 20]
    return a, b, c


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out)


