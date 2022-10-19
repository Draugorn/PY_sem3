"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""
Array = [1.1, 1.2, 3.1, 5, 10.01]
max_num, min_num = 0, 1
for i in Array:
    if (divmod(i, 1))[1] > max_num:
        max_num = divmod(i, 1)[1]
    elif (divmod(i, 1))[1] < min_num and (divmod(i, 1))[1] != 0:
        min_num = (divmod(i, 1))[1]
print(round(max_num - min_num, 2))