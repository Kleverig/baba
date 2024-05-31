# Необхідно ввести з клавіатури N чисел, знайти з них найбільше і
# вивести його.
#--------------------------------------------------------------------------------

def find_max():
    N = int(input("Введіть кількість чисел: "))

    if N <= 0:
        print("Кількість чисел повинна бути більше нуля.")
        return

    max_num = None

    for i in range(N):
        num = float(input(f"Введіть число {i + 1}: "))
        if max_num is None or num > max_num:
            max_num = num

    print(f"Найбільше число: {max_num}")

find_max()
