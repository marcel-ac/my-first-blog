## ::Salve!
## print('Hello, Django Girls!')

## ::If... elif...else

##if 3 > 2:
##    print('Funciona')
##
##if 5 > 2:
##    print('5 é maior que 2')
##else:
##    print('5 não é maior que 2')
##"""
##
'''name = 'Sonja'
if name == 'ola':
    print('Olá ola')
elif name == 'Sonja':
    print('Olá Sonja')
else:
    print('E agora josé?')'''
##
'''
volume = 149
if volume < 20:
    print('Está um pouco baixo')
elif 20 <= volume < 40:
    print('Está bom para música ambiente')
elif 40 <= volume < 60:
    print('Perfeito! Posso ouvir todos os detalhes')
elif 60 <= volume <80:
    print('Ótimo para festas!')
elif 80 <= volume < 100:
    print('Está muito alto')
else:
    print('Meus ouvidos doem')'''
##mudar o volume se estiver muito alto ou baixo
'''volume = 70
if volume < 20 or volume > 80:
    volume = 50
    print('Agora está beeemmm melhor!'); print('O volume atual é ',volume)
else:
    print('oh oh')'''
##

'''def oi():
    print('Olá')
    print('Tudo bem?')


oi()'''

'''def oi(nome):
    if nome == 'ola':
        print('Olá ola')
    elif nome == 'Sonja':
        print('Olá Sonja')
    else:
        print('E agora, josé?')

oi('Estranho')
'''
'''
def oi(name):
    print('Olá ' + name + "!")

oi('Rachel')
'''
'''
def oi(nome):
    print('Oi ' + nome + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'você']
for nome in girls:
    oi(nome)
    print('Próxima')
'''

for i in range(1, 6):
    print(i)
