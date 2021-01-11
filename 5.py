# 5: Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.

num = int(input("Введите натуральное число: "))
data_list = [123, 12, 6, 0]
a = data_list.count(num)
for var in data_list:
    if a > 0:
        b = data_list.index(num)
        data_list.insert(b+a, num)
        break
    else:
        if num > var:
            c = data_list.index(var)
            data_list.insert(c, num)
            break
        elif num < data_list[len(data_list) - 1]:
            data_list.append(num)
print(data_list)