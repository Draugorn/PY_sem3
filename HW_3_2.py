"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д."""

Array = [2, 3, 5, 6, 5, 5]
if len(Array) % 2 == 0:
    Arr_result = [Array[n] * Array[-n - 1]
            for n in range(len(Array)) if n < len(Array)/2]
else:
    Arr_result = [Array[n] * Array[-n - 1]
            for n in range(len(Array)) if n < len(Array)/2]
print(Arr_result)