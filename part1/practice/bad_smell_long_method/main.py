# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(input_data):
    # Читаем входные данные с помощью list comprehension
    read_data = [seq.split(';') for seq in input_data.split('\n')]
    return read_data


def _sort(data):
    # Сортируем данные встроенным методом sorted с использованием ключа по lambda от полученных ранее данных
    return sorted(data, key=lambda person: int(person[1]))


def _filter(data):
    # Фильтруем по возрасту с помощью list comprehension
    filtered = [i for i in data if (int(i[1])>10)]
    return filtered


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    data = _filter(data)
    return data


if __name__ == '__main__':
    print(get_users_list())
