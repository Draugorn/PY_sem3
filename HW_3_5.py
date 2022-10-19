def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def neg_fib(n):
    neg_Fib = []

    for i in range(1, n + 1):
        fibo = fib(i)
        neg_Fib.append(fibo)
        if i != 1:
            neg_Fib.insert(0, (-1) ** (i) * fibo)
    print(f"Последовательность: {neg_Fib}")

fib_input = int(input("Пожалуйста, введите количество чисел по модулю, считая нуль: "))
neg_fib(fib_input)