from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    a = line.replace('-', ' ')[:15].replace(' ', '')
    b = line[line.find('"') + 1:line.find('"') + 4]
    c = line[line.find('"') + 5:line.find('"') + 5 + 20]
    return (a, b, c)


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for row in fr.readlines():
        print(get_parse_attrs(row))



# some_str = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
#
# print(get_parse_attrs(some_str))