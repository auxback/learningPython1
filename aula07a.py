# sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
#while sexo not in 'MmFf':
#    sexo = str(input('informe um caráctere válido! (M/F)')).strip().upper()[0]
#print('Sexo {} registrado com sucesso!'.format(sexo))

# {:^20} coloca o valor/string entre 20 espaços
# {:<20} coloca o valor à esquerda e logo depois 20 espaços
# {:>20} coloca o valor à direita e 20 espaços depois
# {:.3f} pode ser usado p limitar a casa decimal float, p e
# (.format(nome), end='') Esse "end" pode ser usado p n haver a quebra de linha
# Dentro do "print()" pode ser usado "\n" p quebra de linha 'Antony \n Mário'

# Fatorial

#usuario = 1
#while usuario != 0:
#    fatorial = int(input('Digite um valor inteiro para saber seu fatorial: '))
#    aux = fatorial - 1
#    print('Fatorial de {}! é descrito como: '.format(fatorial))
#    print('{}'.format(fatorial), end='')
#    while aux > 0:
#        print(' x {}'.format(aux) if aux > 1 else ' x 1 = ', end='')
#        fatorial *= aux
#        aux -= 1
#    print('{}'.format(fatorial))
#    usuario = int(input('Gostaria de continuar? [1/0] ("1" para SIM ou "0" para NÃO)'))
#

#FIBONACCI
#seq = int(input('Digite a quantidade de sequências da série de Fibonacci: '))
#count = 3
#t1 = 0
#t2 = 1
#t3 = 1
#print(f' {t1} -> {t2} -> {t3} ->', end='')
#while count != seq:
#    t1 = t2
#    t2 = t3
#    t3 = t1 + t2
#    if count == (seq - 1):
#        print(' {}'.format(t3), end='')
#    else:
#        print(f' {t3} ->', end='')
#    count += 1


# CAIXA ELETRÔNICO

#while True:
#    salario = str(input('Qual o seu salário ? (apenas números sem casas decimais) [DIGITE 0 (ZERO) PARA ENCERRAR]')).strip()
#    if int(salario) == 0:
#        time.sleep(1)
#        print('PROGRAMA ENCERRADO...')
#        time.sleep(1)
#        break
#    cedCem = cedDez = cedCinco = moedaUm = 0
#    if len(salario) == 4:
#        cedCem = int(salario[:2])
#         cedDez = int(salario[2])
#         if int(salario[3]) > 5:
#             cedCinco = 1
#             moedaUm = int(salario[3]) - 5
#         elif int(salario[3]) < 5:
#             moedaUm = int(salario[3])
#         elif int(salario[3]) == 5:
#             cedCinco = int(salario[3])
#         time.sleep(1)13
#         print(f'{cedCem} nota(s) de R$100 \n {cedDez} nota(s) de R$10 \n {cedCinco} nota(s) de R$5 \n {moedaUm} moeda(s) de R$1')
#     elif len(salario) == 5:
#         cedCem = int(salario[:3])
#         print(f'Serão {cedCem} notas de R$100')


# POR EXTENSO


# from time import sleep
#
# while True:
#     tuplaExtenso = (
#     'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
#     'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
#     'dezoito', 'dezenove', 'vinte')
#     valor = str(input('Digite o valor entre 0 a 20 que gostaria de ver por extenso '
#     '(Digite 21 para sair) ')).strip()
#     valor = int(valor)
#
#     if 0 <= valor <= 20:
#         print(f'O valor {valor} por extenso é "{tuplaExtenso[valor]}"')
#     elif valor == 21:
#         sleep(1)
#         print('O programa será encerrado...')
#         sleep(2)
#         break
#     else:
#         print('Esse valor não corresponde ao intervalo permitido. Digite um valor entre 0 e 20')


# RANDOM TUPLA MAIOR E MENOR

# from random import randint
#
# tupla = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
# auxTupla = sorted(tupla)
# print(tupla)
# print(f'O menor valor é o {auxTupla.index(0)} e o maior valor é o {auxTupla.index(4)}')


# LISTA DE PREÇOS

# listagem = ('Lápis',1.75,'Borracha',2,'Carderno',15.90,'Estojo',9.90)
# for pos in range(0, len(listagem)):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:>3}')


# MOSTRA A VOGAL DE CADA PALAVRA DE UMA TUPLA

# um for p cada posição da tupla e um for dentro p cada palavra em relação às suas vogais

# from time import sleep
#
# while True:
#     print('=' * 60)
#     print('DIGITE UMA PALAVRA PARA MOSTRAR SUAS VOGAIS\n(separar por espaços e sem acentos)')
#     print('=' * 60)
#     palavra = str(input('Digite a seguir: ')).upper().strip().split()
#     palavra = tuple(palavra)
#     print(palavra)
#     for p in palavra:
#         vogais = ''
#         print(f'Na palavra {p} há as vogais ', end='')
#         for c in p:
#             if c in 'AEIOU':
#                 vogais += c + ' '
#         print(vogais)
#     print('=' * 60 + '\n')
#     continuar = str(input('Gostaria de continuar? [S/N]')).upper().strip()[0]
#     print(('\n') + '=' * 60)
#     if continuar == 'N':
#


# MAIOR MENOR VALOR EM UMA LISTA

from time import sleep

# count = 0
# lista = []

# while True:
#     valor = input('Digite até 5 valores inteiros para ser acrescentados à lista ou digite [S] para sair :').strip().upper()
#     count += 1
#     if valor == 'S':
#         print(f'Você digitou: {valor}')
#         sleep(1)
#         print('FIM DO PROGRAMA')
#         sleep(1)
#         break
#     else:
#         valor = int(valor)
#         lista.append(valor)
#         print(f'Você digitou: {lista}')
#         if count == 5:
#             max = min = posMax = posMin = 0
#             for p, v in enumerate(lista):
#                 if p == 0:
#                     min = v
#                     max = v
#                 else:
#                     if v > max:
#                         max = v
#                         posMax = p
#                     if v < min:
#                         min = v
#                         posMin = p
#             print(f'O maior valor é o {max} e sua posição na lista é', end='')
#             for p, v in enumerate(lista):
#                 if v == max:
#                     print(f' {p}...', end='')
#             print('')
#             print(f'O menor valor é o {min} e sua posição na lista é', end='')
#             for p, v in enumerate(lista):
#                 if v == min:
#                     print(f' {p}...', end='')
#             print('')



# ADICIONAR VALORES ÚNICOS EM UMA LISTA

# lita = []
# while True:
#     valor = input('Adicionar valor inteiro (digite [S] para mostrar a lista e sair) ').strip().upper()
#     if valor == 'S':
#         lista = sorted(lista)
#         print(f'Os valores inseridos em ordem crescente foram: {lista}')
#         break
#     else:
#         valor = int(valor)
#         if valor not in lista:
#             lista.append(valor)
#         else:
#             print('Este valor já foi inserido. Digite um diferente')

# Na expressão "if valor not in lista" toda a lista é verificada de uma vez. Antes fiz de forma manual, ou
#seja, usei um contador e um for p ter o mesmo resultado...



# LISTA ORDENADA SEM USAR SORT

# lista = []
# while True:
#     if len(lista) == 5:
#         print(lista)
#         break
#     valor = int(input('Digite o valor: '))
#     if len(lista) == 0:
#         lista.append(valor)
#     else:
#         for p, v in enumerate(lista):
#             if v >= valor:
#                 lista.insert(p, valor)
#                 break
#             if lista[-1] < valor:
#                 lista.append(valor)
#                 break

# CUIDADO! Adicionar um valor numa lista dentro de um for como o exeplo acima e não
#adicionar um break p parar o loop, a condição [v >= valor] vai fazer adicionar
#repetidamente e nunca para.



# TESTA SE UMA EXPRESSÃO PARÊNTESE OU NÃO

# EXEMPLO 1

# end = ''
# count = 0
# while True:
#     if end == 'N':
#         break
#     else:
#         expressao = str(input('Digite uma expressão matemática envolvenvida em parênteses -> (): '))
#         for v in expressao:
#             if v == '(' or v == ')':
#                 count += 1
#         if count % 2 == 0:
#             print(f'A expressão {expressao} está correta!')
#         else:
#             print(f'A expressão {expressao} não está correta!')
#         end = str(input('Gostaria de continuar ? [S/N]').strip().upper())
#         count = 0


# EXEMPLO 2

# count = 0
# expressao = str(input('Digite uma expressão matemática envolvenvida em parênteses -> (): '))
# for v in expressao:
#     if v == '(' or v == ')':
#         count += 1
# if count % 2 == 0:
#     print(f'A expressão {expressao} está correta!')
# else:
#     print(f'A expressão {expressao} não está correta!')



# MATRIZ LISTA NOME PESO

# end = ''
# lista = list()
# while True:
#     if end == 'N':
#         break
#     else:
#         pessoa = list()
#         nome = str(input('Digite o nome: '))
#         peso = float(input('Digite o peso: '))
#         pessoa.append(nome)
#         pessoa.append(peso)
#         lista.append(pessoa[:])
#         end = str(input('Gostaria de continuar? [S/N]').strip().upper())
#         if end == 'N':
#             print(f'Foram cadastradas {len(lista)} pessoas!')
#             pesados = list()
#             leves = list()
#             maxPeso = minPeso = lista[0][1]
#             for v in lista:
#                 if v[1] >= maxPeso:
#                     maxPeso = v[1]
#                 if v[1] <= minPeso:
#                     minPeso = v[1]
#             for v in lista:
#                 if v[1] == maxPeso:
#                     pesados.append(v[0])
#                 if v[1] == minPeso:
#                     leves.append(v[0])
#             print(f'{len(pesados)} pessoa(s) mais pesada(s) {pesados} com o peso de {maxPeso}Kg')
#             print(f'{len(pesados)} pessoa(s) mais leve(s) {leves} com o peso de {minPeso}Kg')



# LISTA DE LISTA DE VALORES IMPARES E PARES

# end = ''
# vals = []
# imps = []
# pars = []
#
# while True:
#     if end == 'N':
#         break
#     else:
#         while True:
#             if len(vals) < 7:
#                 valor = int(input('Digite um valor: '))
#                 vals.append(valor)
#             else:
#                 break
#         for v in vals:
#             if v % 2 == 0:
#                 pars.append(v)
#             else:
#                 imps.append(v)
#     aux = vals[:]
#     vals.clear()
#     pars.sort()
#     imps.sort()
#     aux.append(pars[:])
#     aux.append(imps[:])
#     vals.append(aux[:])
#     print(f'Os valores pares são {}')
#     print(f'Os valores impares são {imps}')
#     vals.clear()
#     imps.clear()
#     pars.clear()
#     end = input('Gostaria de continuar? [S/N]').strip().upper()


# Para atribuir valores às matrizes de forma automatizada e simplificada basta fazer uma hierarquia de FROM
#p as linhas e colunas.


# DADOS ALEATÓRIOS DICIONÁRIOS

# from random import randint
# from time import sleep
#
# jogadores = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
# for k, v in jogadores.items():
#     jogadores[k] = randint(1, 6)
#     print(f'     O {k} tirou {jogadores[k]}')
#     sleep(1)
# jogadores = dict(sorted(jogadores.items(), key= lambda item: item[1], reverse=True))
# print('Ranking dos jogadores:')
# count = 1
# for k in jogadores.items():
#     if count <= 4:
#         print(f'     {count}º lugar: {k[0]} com {k[1]}')
#         count += 1
#         sleep(1)


# APOSENTADORIA COM DICIONARIO

# from datetime import datetime
#
# empregado = {'nome':'', 'nasc': 0, 'ctps': 0, 'anoContrat': 0, 'salario': 0.00}
# empregado['nome'] = str(input('NOME: '))
# empregado['nasc'] = int(input('ANO DE NASCIMENTO: '))
# empregado['ctps'] = int(input('CTPS: '))
# empregado['anoContrat'] = int(input('ANO DE CONTRATAÇÃO: '))
# empregado['salario'] = float(input('SALÁRIO: '))
# idade = (datetime.now().year) - empregado['nasc']
# for k, v in empregado.items():
#     if k == 'nome':
#         print(f'Nome: {v}')
#     elif k == 'nasc':
#         print(f'idade: {idade}')
#     elif k == 'ctps':
#         if v == 0:
#             print(f'Não há CTPS (Carteira de Trabalho)')
#         else:
#             print(f'CTPS: {v}')
#     elif k == 'anoContrat':
#         print(f'Ano de contratação: {v}')
#     elif k == 'salario':
#         print(f'Salário: {v}')
# anoAposent = (empregado['anoContrat'] + 35)
# idadeAposent = anoAposent - empregado['nasc']
# print(f'Se aposentará provavelmente em {anoAposent} com a idade de {idadeAposent}')


# DESEMPENHO JOGADORES FUTEBOL

# jogador = {'nome': str(input('Digite o nome do jogador: ')),
#            'gols': list(), 'total': 0}
# for p, v in enumerate(range(1, 6)):
#     jogador['gols'].append(int(input(f'Digite quantos gols foram feitos no {p+1}º jogo: ')))
#     if p == 5:
#         for v in jogador['gols']:
#             jogador['total'] += v
# print(jogador)


# ÁREA DE UMA FIGURA GEOMÉTRICA RETANGULAR

a = float(input('Digite a altura em metros: '))
b = float(input('Digite a largura em metros: '))
def ret(x, y):
    r = x * y
    return r


print(f'A figura retangular tem a área de {ret(a, b)}m²')

