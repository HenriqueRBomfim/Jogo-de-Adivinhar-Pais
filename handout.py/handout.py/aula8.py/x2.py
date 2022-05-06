p=input('que adcionar as notas de mais um aluno?')
c=0
o=0
z=0
j=0
while p!='não':
    q1=int(input('quiz1?'))
    q2=int(input('quiz2?'))
    q3=int(input('quiz1?'))
    q4=int(input('quiz4?'))
    q5=int(input('quiz5?'))
    ai=int(input('ai?'))
    af=int(input('af?'))
    ep1=int(input('ep1?'))
    ep2=int(input('ep2?'))
    pf=int(input('pf?'))
    if q1<0 or q2<0 or q3<0 or q4<0 or q5<0:
        m=0 
    elif q1>10 or q2>10 or q3>10 or q4>10 or q5>10:
        m=0 
    elif q1<=q2 and q1<=q3 and q1<=q4 and q1<=q5:
        m=(q2+q3+q4+q5)/4
    elif  q2<=q1 and q2<=q3 and q2<=q4 and q2<=q5:
        m=(q1+q3+q4+q5)/4
    elif q3<=q1 and q3<=q2 and q3<=q4 and q3<=q5:
        m=(q1+q2+q4+q5)/4
    elif q4<=q1 and q4<=q2 and q4<=q3 and q4<=q5:
        m=(q1+q2+q3+q5)/4
    elif q5<=q1 and q5<=q2 and q5<=q3 and q5<=q4:
        m=(q1+q2+q3+q4)/4
    else:
        m=m=(q1+q2+q3+q4+q5)/4
    if m<0 or ai<0 or af<0 or ep1<0 or ep2<0 or pf<0:
        print (0)
    if m>10 or ai>10 or af>10 or ep1>10 or ep2>10 or pf>10:
        print(0)
    else:
        ni= 0.4*ai +0.5*af+0.1*m
        ng=0.1*ep1+ 0.2*ep2 + 0.7*pf
        if ni>=5 and ng>=5:
            nf= (ni+ ng)/2
            o+=1
        elif ni<5 or ng<5:
            nf=min(ni,ng)
            z+=1
    print('Nota final do aluno:{:.2f}'.format(nf))
    j+=1
    c+=nf
    y=c/j
    x= (o/(o+z))*100
    r=100-x
    print('Média da sala:{:.2f}'.format(y))
    print('Aprovados:{:.2f}%'.format(x))
    print('Reprovados:{:.2f}%'.format(r))
    p=input('que adcionar as notas de mais um aluno?')