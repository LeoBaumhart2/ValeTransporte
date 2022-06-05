gu = float(8.8)
gru = float(20.9)
moema = float(8.8)
m = ('''[ 1 ] Guarulhos
[ 2 ] Moema
[ 3 ] Patriarca
[ 0 ] Sair do Programa ''')
print(m)
while m != 0:
    m = int(input('Digite uma opção: '))
    if m == 1:
        print('Você irá para Guarulhos')
        dia = int(input('Quantos dias você quer calcular? '))
        resultado1 = float(gru) * (dia)
        print('Vai dar {:.2f}'.format(resultado1))
    elif m == 2:
        print('Você irá para Moema')
        dia = int(input('Quantos dias você quer calcular? '))
        resultado2 = float(moema) * (dia)
        print('Vai dar {:.2f}'.format(resultado2))
    elif m == 3:
        print('Você irá para Artur Alvim')
        dia = int(input('Quantos dias você quer calcular? '))
        resultado3 = float(gu) * (dia)
        print('Vai dar {:.2f}'.format(resultado3))
print('Muito obrigado por me utilizar ;)')



