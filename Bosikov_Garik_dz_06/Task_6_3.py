import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as uf:
        users_list = [line.strip().replace(',', ' ') for line in uf.readlines()]
    with open(path_hobby_file, 'r', encoding='utf-8') as uh:
        hobby_list = [line.strip().replace(',', ' ') for line in uh.readlines()]
    if len(users_list) > len(hobby_list):
        sys.exit(1)
    return {user: (hobby_list[idx] if idx < len(hobby_list) else None) for idx, user in  enumerate(users_list)}


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
