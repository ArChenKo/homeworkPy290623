# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('Введите первое число: '))
b = int(input('Введите второе слагаемое: '))


def sum_(a_num, b_num):
    if a_num <= 0 < b_num or b_num <= 0 < a_num:
        return 1 + sum_(a_num - 1, b_num - 1)
    elif a_num <= 0 and b_num <= 0:
        return 0
    else:
        return 1 + 1 + sum_(a_num - 1, b_num - 1)


print(res := sum_(a, b))
