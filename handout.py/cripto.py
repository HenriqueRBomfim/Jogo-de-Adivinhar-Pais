
conteudo='''milho da pipoce qua neo pezze palo fogo continue e zab milho da pipoce, pebe zampba.
ezzim econtaca com e ganta.
ez gbendaz tbenzfobmecoaz econtacam quendo pezzemoz palo fogo.
quam neo pezze palo fogo fice do mazmo jaito, e vide intaibe.
buram elvaz'''
texto=conteudo.split()
print(texto)
plvr=''
texto_final=''

print(texto)
for plv in texto:
    for letra in plv:
        if letra=='s':
            plvr+='z'
        elif letra=='a':
            plvr+='e'
        elif letra=='r':
            plvr+='b'
        elif letra=='b':
            plvr+='r'
        elif letra=='e':
            plvr+='a'
        elif letra=='z':
            plvr+='s'
        else:
            plvr+=letra
    if len(texto_final)==0:
        texto_final=plvr
    else:
       texto_final+=' '+plvr
    plvr=''
print(texto_final)