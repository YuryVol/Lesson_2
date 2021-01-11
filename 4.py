# Пользователь вводит строку из нескольких слов, разделённых
# пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.

data_str = input("Введите строку из нескольких слов ")
data_word = []
num = 1
for el in range(data_str.count(' ') + 1):
    data_word = data_str.split()
    if len(str(data_word)) <= 10:
        print(f" {num} {data_word [el]}")
        num += 1
    else:
        print(f" {num} {data_word [el] [0:10]}")
        num += 1