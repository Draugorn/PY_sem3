def binary_converter(num):
    num_t = num
    num_bin = ""
    while num_t > 0:
        num_bin = str(num_t % 2) + num_bin
        num_t //= 2
    return print(f"Число в дясятичной {num} = {num_bin} в двоийчной системе")1

num_input = int(input("Пожалуйста, введите десятичное число: "))

binary_converter(num_input)