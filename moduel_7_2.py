def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    for string in strings:
        file.write(string + '\n')
    for num_string, string in enumerate(strings, start=1):
        strings_position[num_string, file.tell() - len(string) - 1] = string #вычитаем длину строки и '\n' так как file.tell() выводит число байтов в конце строки
    file.close()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('text.txt', info)
for elem in result.items():
  print(elem)
