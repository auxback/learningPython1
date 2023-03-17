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

from time import sleep

while True:
    print('=' * 60)
    print('DIGITE UMA PALAVRA PARA MOSTRAR SUAS VOGAIS\n(separar por espaços e sem acentos)')
    print('=' * 60)
    palavra = str(input('Digite a seguir: ')).upper().strip().split()
    palavra = tuple(palavra)
    print(palavra)
    for p in palavra:
        print(f'Na palavra {p} há as vogais ', end='')
        for c in p:
            if c in 'A' or 'E' or '':
                if c[-1]:
                    print(f'{c}')
                    print('=' * 60 + '\n')
                    continuar = str(input('Gostaria de continuar? [S/N]')).upper().strip()
                    print(('\n') + '=' * 60)
                    if continuar == 'N':
                        break
                else:
                    print(f'{c}, ')
