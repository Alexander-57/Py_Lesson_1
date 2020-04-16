
import divisor_master
n = int(input('Введите натуральное число от 1 до 1000:'))

if divisor_master.PrimeNum(n):
    print(n, '- простое число')
else:
    print(n, '- составное число')
print('Список всех делителей числа:', divisor_master.DivNum(n))
print('Максимальный простой делитель числа:', divisor_master.MaxDivNum(n))
print ('Простые множители числа','{} = {}' .format(n, ' * '.join(map(str, divisor_master.PrimeMult(n)))))
print('Максимальный делитель числа:', divisor_master.DivNumMax(n))