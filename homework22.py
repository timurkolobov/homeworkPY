# Ввод количества элементов первого и второго множеств
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Ввод элементов первого множества
set1 = set()
print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

# Ввод элементов второго множества
set2 = set()
print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

# Находим пересечение множеств
intersection = set1.intersection(set2)

# Выводим результат без повторений в порядке возрастания
result = sorted(intersection)
print("Числа, которые встречаются в обоих наборах, без повторений и в порядке возрастания:")
for element in result:
    print(element)
