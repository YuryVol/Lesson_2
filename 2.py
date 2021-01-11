# 2: Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

data_list = ['0', 'a', '2', 'b', '4']
if len(data_list) % 2 == 0:
    i = 0
    while i < len(data_list):
        var = data_list[i]
        data_list[i] = data_list[i+1]
        data_list[i+1] = var
        i += 2
else:
    i = 0
    while i < len(data_list) - 1:
        var = data_list[i]
        data_list[i] = data_list[i + 1]
        data_list[i + 1] = var
        i += 2
print(data_list)