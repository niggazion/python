num = int(input("digite um numero entre 1 e 100"))

if num >=1 and num <=100 :
    divisores = 0
    for divisor in range(1, 1 + num):
        if num % divisor == 0:

            print('{} '.format(divisor), end=('')) #apos o print '{} server pra colocar em tupla end ('') para manter os numeros na mesma linha

    if divisores > 1:
        print("não é primo")

    else:
        print("é primo")
else:
 print ("digite um numero entre 1 e 100")
