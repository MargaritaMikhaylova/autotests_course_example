# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt', encoding='utf-8') as file:
    data = file.readlines()
    # all_sales = data.split('\n\n')
    bill = 0
    bills = []
    for i in data:
        if i != '\n':
            bill += int(i)
        else:
            bills.append(bill)
            bill = 0
    bills.sort()
    three_most_expensive_purchases = bills[-1] + bills[-2] + bills[-3]
    print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
