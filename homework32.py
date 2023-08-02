#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)
#Ввод:
#3 4 2 5 7
#[4,6]
#Вывод:
#1, 3


def find_indexes(lst, range):
    min_val, max_val = range
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return ', '.join(map(str, indexes))

input_list = input("Введите элементы массива через пробел: ").split()
input_list = list(map(int, input_list))

input_range = input("Введите диапазон в формате [минимальное значение, максимальное значение]: ")
input_range = input_range.strip("[]")
input_range = input_range.split(",")

min_value = int(input_range[0])
max_value = int(input_range[1])

result = find_indexes(input_list, [min_value, max_value])
print("Индексы элементов, значения которых принадлежат заданному диапазону:", result)