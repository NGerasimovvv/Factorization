from random import randint
import math
import time
from sympy import *

n = 3692655488820624713
B = 2
i = 1

start = time.time()

a = randint(2, n - 2)
a1 = a
print (f'а: {a}')

d = math.gcd(a, n)

if d >= 2:
    print(f'Делитель найден: {d}')
else :
    while 1:
        l = int(math.log(n)/math.log(B))
        a = pow(a, pow(B,l), n)
        print(f'{i})B = {B}, l = {l}')
        i+=1

        d = math.gcd(a-1, n)
        if d != 1 and d != n:
            print (f'а: {a1}')
            print(f'Делитель найден: {d}')
            print(f'Время: {time.time() - start} секунд')
            print(f'Число иттераций: {i-1}')
            print(f'{n} = {d}*{(int)(n/d)}')
            break
        else:
            B+=1
            while isprime(B) != true:
                B+=1
