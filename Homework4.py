import math


def gcdex(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1  

    while b != 0:
        q = a // b  
        a, b = b, a % b 
        x0, x1 = x1, x0 - q * x1  
        y0, y1 = y1, y0 - q * y1 

    return a, x0, y0

def inverse_element(a, n):
    d, x, _ = gcdex(a, n)
    if d != 1:
        return None
    return x % n

def phi(m):
    result = 1
    for i in range(2, m):
        if gcdex(i, m)[0] == 1:
            result += 1
    return result

def inverse_element_2(a, n):
    if math.gcd(a, n) != 1:
        return None  
    phi_n = phi(n)

    return pow(a, phi_n - 1, n)


print("\n Завдання 1 \n")

a = int(input("a = "))
b = int(input("b = "))
d, x, y = gcdex(a, b)

print(f"НСД = {d}, x = {x}, y = {y}")
print(f"Перевірка: {a}*{x} + {b}*{y} = {a * x + b * y}")

print("\nЗавдання 2\n")

a = int(input("a = "))
n = int(input("b = "))
inverse = inverse_element(a, n)
if inverse is not None:
    print(f"Мультиплікативний обернений елемент дорівнює: {inverse}")
    print(f"Перевірка: ({a} * {inverse}) % {n} = {(a * inverse) % n}")
else:
    print(f"Мультиплікативний обернений елемент для a = {a} за модулем n = {n} не існує")

print("\nЗавдання 3:\n")

m = int(input("m = "))
print(f"Значення функції Ейлера: {phi(m)}")

print("\nЗавдання 4:\n")

a = int(input("a = "))
n = int(input("n = "))
inverse = inverse_element_2(a, n)

if inverse is not None:
    print(f"Мультиплікативний обернений елемент дорівнює: {inverse}")
else:
    print(f"Мультиплікативний обернений елемент для a = {a} за модулем n = {n} не існує")