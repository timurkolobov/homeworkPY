"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
"""

def check_rhythm(poem):
    lines = poem.split(" ")  # Разделяем стихотворение на строки
    syllable_counts = []

    for line in lines:
        words = line.split("-")  # Разделяем строку на слова
        syllable_count = sum([count_syllables(word) for word in words])  # Считаем количество слогов в каждом слове
        syllable_counts.append(syllable_count)

    if len(set(syllable_counts)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(word):
    vowels = "аоиеёэыуюяАОИЕЁЭЫУЮЯ"  # Гласные буквы
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count

# Пример использования
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)