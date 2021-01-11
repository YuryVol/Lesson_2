# 1: Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
# типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

data_int = 22
data_float = 1.98
data_str = "Hello World !"
data_list = ['a', '12']
data_tuple = ('b', '45')
data_dict = {'city': 'Moscow', 'country': 'Russia'}

total_list = [data_int, data_float, data_str, data_list, data_tuple, data_dict]
for i in total_list:
    print(f'{i} is {type(i)}')