# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

read_file = 'test_file/task1_data.txt'
write_file = 'test_file/task1_answer.txt'
new_f = ''

with open(read_file, 'r', encoding='utf-8') as rf, open(write_file, 'w', encoding='utf-8') as wf:

    for i in rf:
        for item in i:
            if item not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                new_f += item
                wf.write(item)
#print(new_f)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')