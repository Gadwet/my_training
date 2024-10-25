file_name = 'm_7_2.txt'
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

def custom_write(file_name, strings):
    strings_position = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            start_bytes = file.tell()
            file.write(string + '\n')
            strings_position[(line_number, start_bytes)] = string
    return strings_position

result = custom_write('m_7_2.txt', info)
for i in result.items():
    print(i)
