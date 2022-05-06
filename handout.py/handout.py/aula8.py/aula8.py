import random
n=random.randint(1,20)
x=0
while x!=n:
    x= int(input('valor: '))
    if n==x:
        print('Acertou')
    elif x>n:
        print('Muito alto')
    else:
        print('Muito baixo')