# 2.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел
# от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def InputNumbers(inputDigit):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputDigit}"))
            is_OK = True
        except ValueError:
            print("Не верное введено число. ")
    return number
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

num = InputNumbers("Введите число N: ")
list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до введенно вами числа ({num}) составляют:  {list} {}.")