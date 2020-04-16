# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
# Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def PrimeNum(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

# 2) выводит список всех делителей числа;
def DivNum(n):
    list_div = []
    for i in range(1, n + 1):
        if n % i == 0:
            list_div == list_div.insert(0, i)
    return list_div

# 3) выводит самый большой простой делитель числа.
def MaxDivNum(n):
    list_div = DivNum(n)
    list_pdiv = []
    for i in range(0, len(list_div)):
        if PrimeNum(list_div[i]):
            list_pdiv == list_pdiv.insert(i, list_div[i])
    return list_pdiv[0]

# 4) функция выводит каноническое разложение числа на простые множители;
def PrimeMult(n, b=2):
    while n > 1:
        n1, n2 = divmod(n, b)
        if n2:
            b += 1
        else:
            yield b
            n = n1

# 5)функция выводит самый большой делитель (не обязательно простой) числа.
def DivNumMax(n):
    list_div_max = []
    for i in range(1, n + 1):
        if n % i == 0:
            list_div_max == list_div_max.insert(0, i)
    return list_div_max[0]

n = int(input('Введите натуральное число от 1 до 1000:'))

if PrimeNum(n):
    print(n, '- простое число')
else:
    print(n, '- составное число')
print('Список всех делителей числа:', DivNum(n))
print('Максимальный простой делитель числа:', MaxDivNum(n))
print ('Простые множители числа','{} = {}' .format(n, ' * '.join(map(str, PrimeMult(n)))))
print('Максимальный делитель числа:', DivNumMax(n))
