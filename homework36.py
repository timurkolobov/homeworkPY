'''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.
'''

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печать заголовка таблицы
    print("     ", end="")
    for col in range(1, num_columns+1):
        print("{:5}".format(col), end="")
    print()
    
    # Печать строк таблицы
    for row in range(1, num_rows+1):
        print("{:5}".format(row), end="")
        for col in range(1, num_columns+1):
            result = operation(row, col)
            print("{:5}".format(result), end="")
        print()

# Пример функции, вычисляющей элемент таблицы
def multiply(row, col):
    return row * col

# Вызов функции print_operation_table() с функцией multiply
print_operation_table(multiply)