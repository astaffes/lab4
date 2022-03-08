a, b = input("Введите два числа: ").split()
a = int(a)
b = int(b)
print((a % b) * (b % a) + 1)
