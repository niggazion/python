import math

num = int(input('escreva o numero pra fazer a taboada'))
for a in range(1,11):
    x = a * num
    print('{} x {} = {}'.format(num,a,x))
    a =a +1

