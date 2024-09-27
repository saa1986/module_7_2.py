"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи.

Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.

Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

Пример результата выполнения программы:
Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

"""


def custom_write(file_name, strings):  #Создаем пустой словарь для хранения позиций строк в файле
    strings_positions = {} # Открываем файл для записи с кодировкой utf-8

    with open(file_name, 'w', encoding='utf-8') as file:# Проходим по строкам списка strings с их индексами
        for i, string in enumerate(strings):  # Получаем текущую позицию в файле
            position = file.tell()   # Записываем строку в файл с символом новой строки
            file.write(string + '\n') # Записываем позицию и строку в словарь
            strings_positions[(i + 1, position)] = string  # Возвращаем словарь с позициями строк
    return strings_positions # Список строк для записи в файл


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
] # Вызываем функцию custom_write с именем файла 'test.txt' и списком строк info

result = custom_write('test.txt', info) # Перебираем элементы в словаре result

for elem in result.items(): # Выводим каждый элемент (кортеж) содержащий индекс, позицию и строку
    print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 15), 'Используйте кодировку utf-8.')
# ((3, 64), 'Because there are 2 languages!')
# ((4, 95), 'Спасибо!')
