import random
def apostando_em_dados(s,a,r):
    c=0
    while c<=r:
        n= random.randint(1,6)
        if s==n:
            a=a+(a/3)
        else:
            a= a-(a/6)
        c+=1
    return a
print(apostando_em_dados(5,150,5))