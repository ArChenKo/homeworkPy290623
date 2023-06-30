# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью
# рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))


def step(a_num, b_num):
    if b_num == 0:
        return 1
    elif b_num == 1:
        return a_num
    else:
        return a_num * step(a_num, b_num - 1)


res = step(a, b)
print(f'Результат возведения в степень = {res}')
