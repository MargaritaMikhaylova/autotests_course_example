# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

# Здесь пишем код
# class FileOpener:
# f = open('test_file/task1_data.txt', encoding='utf-8')
# print(f.read)

from pathlib import Path


with open('test_file/task1_data.txt', encoding='utf-8') as file:
    data = file.read()
    file2 = ''
    for i in data:
        if i.isdigit() != True:
            file2 += i
with open('test_file/task1_answer.txt', encoding='utf-8', mode='w') as new_file:
    new_file.write(file2)
    new_file.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
