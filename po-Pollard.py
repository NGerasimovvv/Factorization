import time
import math

n = 3692655488820624713
c = 1
a = c
b = c
d = 1
i = 0

start = time.time()

while d == 1:
   i += 1
   a = (pow(a,2) + 1) % n
   b = (pow(b,2) + 1) % n
   b = (pow(b,2) + 1) % n
   d = math.gcd(a - b, n)
   print(f'{i}) a = {a}, b = {b}, НОД(a - b, n) = {d}')
   if (1 < d) and (d < n):
      p = d
      print('Делитель: %d' %(p))
   if d == n:
      print(f'Делитель не найден')
      break

print(f'Время: {time.time() - start} секунд')
print(f'Число иттераций: {i}')
print(f'{n} = {p}*{(int)(n/p)}')
