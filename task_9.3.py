# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

# f = open('test_file/task_3.txt', 'r', encoding='utf-8')
# str1 = str(f.split(' '))

three_most_expensive_purchases = 0
str1 = []
sum1 = 0
with open('test_file/task_3.txt', 'r') as f:

    for pillar in f:
        if pillar == '\n':
            str1.append(sum1)
            sum1 = 0
        else:
            sum1 += int(pillar)

str1.sort()
three_most_expensive_purchases = sum(str1[-3::])

assert three_most_expensive_purchases == 202346
print('Прошел')