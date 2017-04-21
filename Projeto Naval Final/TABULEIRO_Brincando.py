from random import *
import sys
from termcolor import colored

def resultado():
    print('')
    print('Os resultados foram:')
    print('')
    for i in range(len(nomes_jogador)):
        print(nomes_jogador[i], '--->' , contador_de_seus_acertos)

def cria_grelha(matriz):
    '''esta função cria uma matriz 10X10'''
    for i in range(10):
        matriz.append([])
        for j in range(10):
            matriz[i].append(colored('~', 'blue'))

def interface(matriz):
    '''Mostra o Tabuleiro que aparecerá as embarcações e os tiros dados'''
    print('     |   %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |'%(linha_numero[0],linha_numero[1],linha_numero[2],linha_numero[3],linha_numero[4],
                                                                                           linha_numero[5],linha_numero[6],linha_numero[7],linha_numero[8],linha_numero[9]))
    print('     ---------------------------------------------------------------')

    for k in range(10):

        print('  %s  |   %s     %s     %s     %s     %s     %s     %s     %s     %s     %s   |      ' %(letras[k],matriz[k][0],matriz[k][1], matriz[k][2],
                                                                                                  matriz[k][3], matriz[k][4],matriz[k][5],matriz[k][6],
                                                                                                  matriz[k][7], matriz[k][8], matriz[k][9]))
    print('     ---------------------------------------------------------------')
    print('                 Mar das embarcações do meu INIMIGO                  ')

def verifica_tiro(numero,letra_tiro):
    '''esta função verifica se na matriz_aliado contém algum barco e substitui na matriz_inimigo que é a matriz do adversário'''


    if matriz_aliado[letras.find(letra_tiro)][numero - 1] == 1:
        '''Caso acerte o tiro aparece o número 1'''

        X = colored('X', 'red')
        matriz_inimigo[letras.find(letra_tiro)][numero - 1] = X

    else:
        matriz_inimigo[letras.find(letra_tiro)][numero - 1] = 'O'
        print('Tiro em alto Mar. Atire novamente!')

def coloca_barco(linha,coluna,sentido_do_barco,matriz_aliado,barco,i):
    '''Esta função coloca o barco na posição desejada e coloca 'a' em volta dos barcos para não ser possível colocar barcos adjacentes'''

    a = 'x'  #O caractere atribuido ao termo 'a' será colocado em volta dos barcos

    if i == 0:
        '''Esta parte coloca 'a' ao redor do barco quando os barcos forem colocados na horizontal'''

        if sentido_do_barco == 1:

            matriz_aux0 = []
            for v in range(coluna, 10):
                matriz_aux0.append(v)

            if 0 < coluna < 9 and 0 < linha < 9:
                matriz_aliado[linha][coluna - 1] = a

                if len(barco) < matriz_aux0.index(matriz_aux0[-1]) + 1:
                    '''Esta parte verifica se o limite do barco encosta ou não no limite do tabuleiro para acrecentar ou não o 'a'.'''
                    matriz_aliado[linha][coluna + len(barco)] = a

                    for v in range(coluna - 1, coluna + len(barco) + 1):
                        matriz_aliado[linha - 1][v] = a
                        matriz_aliado[linha + 1][v] = a

                else:
                    matriz_aliado[linha][coluna - 1] = a

                    for v in range(coluna - 1, coluna + len(barco)):
                        matriz_aliado[linha - 1][v] = a
                        matriz_aliado[linha + 1][v] = a

            matriz_aux0.clear()

            if 0 < coluna < 9 and linha == 0:
                matriz_aliado[linha][coluna - 1] = a

                if coluna + len(barco) <= 9:
                    '''Se existir mais elementos depois da ultima parte do barco acrecenta-se 'a'. '''
                    matriz_aliado[linha][coluna + len(barco)] = a

                if coluna + len(barco) + 1 <= 10:

                    for v in range(coluna - 1, coluna + len(barco) + 1):
                        matriz_aliado[linha + 1][v] = a

                else:
                    for v in range(coluna - 1, coluna + len(barco)):
                        matriz_aliado[linha + 1][v] = a

            elif 0 < coluna < 9 and linha == 9:
                matriz_aliado[linha][coluna - 1] = a

                if coluna + len(barco) <= 9:
                    matriz_aliado[linha][coluna + len(barco)] = a

                if coluna + len(barco) + 1 <= 10:

                    for v in range(coluna - 1, coluna + len(barco) + 1):
                        matriz_aliado[linha - 1][v] = a
                else:

                    for v in range(coluna - 1, coluna + len(barco)):
                        matriz_aliado[linha - 1][v] = a

            elif coluna == 0 and 0 < linha < 9:
                matriz_aliado[linha][coluna + len(barco)] = a

                for v in range(coluna , coluna + len(barco) + 1):
                    matriz_aliado[linha - 1][v] = a
                    matriz_aliado[linha + 1][v] = a

            elif coluna == 9 and 0 < linha < 9:
                matriz_aliado[linha][coluna - 1] = a

                for v in range(coluna - 1, coluna + len(barco)):
                    matriz_aliado[linha - 1][v] = a
                    matriz_aliado[linha + 1][v] = a

            elif coluna == 0 and linha == 0:
                matriz_aliado[linha][coluna + len(barco)] = a

                for v in range(coluna , coluna + len(barco) + 1):
                    matriz_aliado[linha + 1][v] = a

            elif coluna == 9 and linha == 0:
                matriz_aliado[linha][coluna - 1] = a

                for v in range(coluna - 1, coluna + len(barco)):
                    matriz_aliado[linha + 1][v] = a

            elif coluna == 0 and linha == 9:
                matriz_aliado[linha][coluna + len(barco)] = a

                for v in range(coluna , coluna + len(barco) + 1):
                    matriz_aliado[linha - 1][v] = a

            elif coluna == 9 and linha == 9:
                matriz_aliado[linha][coluna - 1] = a

                for v in range(coluna - 1, coluna + len(barco)):
                    matriz_aliado[linha - 1][v] = a

        if sentido_do_barco == 2:
            '''Esta parte coloca 'a' em volta dos barcos colocados na vertical.'''

            j = len(barco)
            matriz_aux = []

            for r in range(linha, 10):
                matriz_aux.append(matriz_aliado[r][coluna])

            if linha != 0 and linha != 9 and coluna != 0 and coluna != 9 and (len(barco) != len(matriz_aux)):

                matriz_aliado[linha - 1][coluna] = a
                matriz_aliado[linha + j][coluna] = a

                for r in range(linha - 1, linha + len(barco) + 1):
                    matriz_aliado[r][coluna - 1] = a
                    matriz_aliado[r][coluna + 1] = a

            elif (0 < linha < 9) and coluna == 9 and (len(barco) != len(matriz_aux)):

                matriz_aliado[linha - 1][coluna] = a
                matriz_aliado[linha + j][coluna] = a

                for r in range(linha - 1, linha + len(barco) + 1):
                    matriz_aliado[r][coluna - 1] = a

            elif (0 < linha < 9) and coluna == 0 and (len(barco) != len(matriz_aux)):

                matriz_aliado[linha - 1][coluna] = a
                matriz_aliado[linha + j][coluna] = a

                for r in range(linha - 1, linha + len(barco) + 1):
                    matriz_aliado[r][coluna + 1] = a

            elif linha == 0 and 0 < coluna < 9:

                matriz_aliado[j][coluna] = a

                for r in range(linha, linha + j + 1):
                    matriz_aliado[r][coluna - 1] = a
                    matriz_aliado[r][coluna + 1] = a

            elif linha == 9 and 0 < coluna < 9:
                matriz_aliado[linha - 1][coluna] = a

                for r in range(linha - 1, linha + len(barco)):
                    matriz_aliado[r][coluna - 1] = a
                    matriz_aliado[r][coluna + 1] = a

            elif linha == 0 and coluna == 0:

                matriz_aliado[j][coluna] = a

                for r in range(linha, linha + j + 1):
                    matriz_aliado[r][coluna + 1] = a

            elif linha == 0 and coluna == 9:

                matriz_aliado[j][coluna] = a

                for r in range(linha, linha + j + 1):
                    matriz_aliado[r][coluna - 1] = a

            elif len(barco) == len(matriz_aux):
                if coluna == 0:
                    matriz_aliado[linha - 1][coluna] = a
                    for r in range(linha - 1, linha + len(barco)):
                        matriz_aliado[r][coluna + 1] = a

                elif coluna == 9:
                    matriz_aliado[linha - 1][coluna] = a
                    for r in range(linha - 1, linha + len(barco)):
                        matriz_aliado[r][coluna - 1] = a

                elif 0 < coluna < 9:
                    matriz_aliado[linha - 1][coluna] = a
                    for r in range(linha - 1, linha + len(barco)):
                        matriz_aliado[r][coluna - 1] = a
                        matriz_aliado[r][coluna + 1] = a

            matriz_aux.clear()

    if i == len(barco):
        return matriz_aliado

    matriz_aliado[linha][coluna] = barco[i]
    #Coloca barco na Horizontal
    if sentido_do_barco == 1:
        return coloca_barco(linha,coluna+1,sentido_do_barco,matriz_aliado,barco,i+1)
    # Coloca barco na Vertical
    else:
        return coloca_barco(linha+1,coluna,sentido_do_barco,matriz_aliado,barco,i+1)
'''Fim da def coloca_barco'''

def corrige(barco,linha,coluna):
    '''Verifica se a posição do barco é válida nos limites das matriz_aliado'''
    '''Verifica na Horizontal'''
    if len(matriz_aliado[linha][coluna:]) < len(barco) and sentido_do_barco == 1:
        return False
    cont = 1
    for i in range(linha, 10):
        cont += 1
    '''Verifica na vertical'''
    if cont < len(barco) and sentido_do_barco == 2:
        return False
    else:
        return True

def verifica_coloca_barco(barco,linha,coluna,sentido_do_barco):
    '''Verifica se um barco esta sendo colocado em cima de outro sentido_do_barco == 1(Horizontal) e sentido_do_barco == 2 (vertical)'''
    a = '~'
    if sentido_do_barco == 1:

        try:
            for p in range(len(barco)):
                '''Verifica se tem algum 'x' ou '1' nas posições que serão ocupadas pelo barco ou se o barco excede o limite do tabuleiro
                , permitindo ou não que o barco seja inserido'''
                if 'x' not in matriz_aliado[linha][coluna:coluna + len(barco)] and 1 not in matriz_aliado[linha][coluna:coluna + len(barco)]:
                    return True
        except:
            return False

        cont_h = 0

        for p in range(coluna - 1, coluna + len(barco)):
            '''Esta parte verifica e impede que alguma parte do barco seja substituida por 'a', impedindo a colocação do barco.
            O elemento matriz_aliado[linha][p] pode ser uma parte de uma embarcação colocada anteriormente.'''
            if a != matriz_aliado[linha][p]:
                cont_h += 1
        if cont_h == 0:
            return True
        else:
            return False

    elif sentido_do_barco == 2:
        '''Esta parte verifica se o barco pode ser colocado verticalmente na posição solicitada'''
        cont_v = 0

        for p in range(linha, linha + len(barco)):
            try:
                if matriz_aliado[p][coluna] == a:
                    cont_v += 1
            except IndexError:
                return False

            if cont_v >= len(barco):
                return True
    else:
        return False

print('\n Lembrando algumas regras da Batalha Naval: \n '
      '\n 1 - Não é possível colocar um embarcação ao lado de outra embarcação; '
      '\n 2 - Os limites dados no tabuleiro devem ser respeitados, ou seja, não pode ficar nenhuma parte da embarcação fora '
      '\n      do tabuleleiro, caso isso ocorra será solicitada uma nova posição; '
      '\n 3 - Uma embarcação não pode ser colocada em uma posição já ocupada por alguma parte de outra embarcação;'
      '\n 4 - Caso uma embarcação seja acertada aparecerá o número 1 no local atirado, caso contrário será exibida a letra "x";'
      '\n 5 - O jogador que primeiro afundar todas embarcações ganha;'
      '\n 6 - Ao selecinar uma posição para o barco, a parte inicial da embarcação será colocada na posição selecinada,'
      ' \n     as demais parte serão colocada no sentido(Horizontal ou vertical) que você escolher;'
      '\n 7 - Tabuleiro do jogo: ')

print('')
print('Saudações, Capitão! Bem vindo a bordo! Para iniciarmos a batalha vamos posicionar nossas embarcações: ')
print('')

resp = 's'
nomes_jogador = []
acertos_jogador = []

while resp == 's':

    letras = 'ABCDEFGHIJ'
    linha_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    matriz_aliado = []
    matriz_inimigo = []
    barcos = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
    cria_grelha(matriz_aliado)
    cria_grelha(matriz_inimigo)
    interface(matriz_inimigo)

    print('')
    jogador = input('Qual seu nome Senhor? E futuro CAPITÃO!? ')
    nomes_jogador.append(jogador)

    while True:
        try:
            nivel_dificuldade =  int(input('Qual é a nivel que o CAPITÃO que jogar( 1 - Fácil(Errar 25 tiros), 2 - Normal(Errar 20 tiros), '
                                           '3 - Difícil(Errar 15 tiros) ou 4 - Quase Impossível(Errar 10 tiros)? '))
            if nivel_dificuldade not in [1,2,3,4]:
                print('Número inválido. Informe um número de 1 a 4.')
                continue
            break
        except ValueError:
            print('Caractere inválido. Informe um número de 1 a 4.')
    print('')

    n = []
    for i in range(len(barcos)):
        '''Esta parte do código pede ao usuário as posição e o sentido que o barco deve ser colocado, além de chamar funções para verificar se a posição é valida ou não.'''

        while True:
            '''Esta parte parte impede que o mesmo barco seja posicionado mais de uma vez no tabuleiro.'''
            x = randint(0,4)

            if x not in n:
                n.append(x)
                break

        while True:
            '''Posiciona aleatoriamente o barco.'''
            sentido_do_barco = randint(1,2)
            linha = randint(0, 9)
            coluna = randint(0, 9)

            if corrige(barcos[x],linha,coluna) == True and verifica_coloca_barco(barcos[x], linha, coluna, sentido_do_barco) == True:
                '''Esta parte chama as funções acima para verificar se é possível o barco ser colocado na posição solicitada.'''
                coloca_barco(linha,coluna,sentido_do_barco,matriz_aliado,barcos[x],0)
                break
            else:
                continue

    '''Fim do For '''

    print('\n Agora começa a Batalha Naval! Informe a posicão que devemos atirar, Capitão!')
    print('')

    while True:
        '''Esta parte pede a posição que o jogador vai atirar'''
        while True:
            c = input('Informe a letra da linha que o tiro vai ser disparado: ')
            letra_tiro = c.upper()

            if letra_tiro not in letras:
                print('Letra inválida. Informe uma letra maiúscula de A a J.')
                print('')
                continue
            else:
                break

        while True:
            try:
                numero = int(input('Informe o número da coluna que o tiro vai ser disparado: '))
                if numero < 0 or numero > 10:
                    print('Valor inválido. Informe um número de 1 a 10.')
                    continue
                else:
                    print('')
                    break
            except:
                print('Valor inválido. Informe um número de 1 a 10.')
                continue

        verifica_tiro(numero,letra_tiro)
        interface(matriz_inimigo)
        print('')

        '''A qui começa a parte de contagem de erros e acertos dos tiros, determinado quando o jogo acaba. '''

        contador_de_erros = 0
        contador_de_seus_acertos = 0

        for y in range(0,10):
            '''Verifica se vc ganhou a batalha.'''
            contador_de_erros += matriz_inimigo[y].count('O')

        if nivel_dificuldade == 1:

            if contador_de_erros == 25:
                interface(matriz_aliado)
                print('ACABOU nossas BALAS Capitão!!')
                for y in range(0, 10):
                    '''Verifica se vc ganhou a batalha.'''
                    contador_de_seus_acertos += matriz_inimigo[y].count(1)
                    acertos_jogador.append(contador_de_seus_acertos)

                while True:
                    resp = input('Gostaria de ARMAR os CANHÕES e ATIRAR novamente(s ou n)? ')
                    if resp == 'n':
                        resultado()
                    elif resp not in ['s','n']:
                        print('Informe s para jogar novamente ou n para parar de jogar!')
                        continue
                    break
                break
            else:
                print('Em qual posição vai atirar novamente Capitão??')

        elif nivel_dificuldade == 2:

            if contador_de_erros == 20:
                interface(matriz_aliado)
                print('ACABOU nossas BALAS Capitão!!')
                for y in range(0, 10):
                    '''Verifica se vc ganhou a batalha.'''
                    contador_de_seus_acertos += matriz_inimigo[y].count(1)
                    acertos_jogador.append(contador_de_seus_acertos)

                while True:
                    resp = input('Gostaria de ARMAR os CANHÕES e ATIRAR novamente(s ou n)? ')
                    if resp == 'n':
                        resultado()
                    elif resp not in ['s','n']:
                        print('Informe s para jogar novamente ou n para parar de jogar!')
                        continue
                    break
                break
            else:
                print('Em qual posição vai atirar novamente Capitão??')

        elif nivel_dificuldade == 3:

            if contador_de_erros == 15:
                interface(matriz_aliado)
                print('ACABOU nossas BALAS Capitão!!')
                for y in range(0, 10):
                    '''Verifica se vc ganhou a batalha.'''
                    contador_de_seus_acertos += matriz_inimigo[y].count(1)
                    acertos_jogador.append(contador_de_seus_acertos)

                while True:
                    resp = input('Gostaria de ARMAR os CANHÕES e ATIRAR novamente(s ou n)? ')
                    if resp == 'n':
                        interface(matriz_aliado)
                    elif resp not in ['s', 'n']:
                        print('Informe s para jogar novamente ou n para parar de jogar!')
                        continue
                    break
                break
            else:
                print('Em qual posição vai atirar novamente Capitão??')

        elif nivel_dificuldade == 4:

            if contador_de_erros == 10:
                interface(matriz_aliado)
                print('ACABOU nossas BALAS Capitão!!')
                for y in range(0, 10):
                    '''Verifica se vc ganhou a batalha.'''
                    contador_de_seus_acertos += matriz_inimigo[y].count(1)
                    acertos_jogador.append(contador_de_seus_acertos)

                while True:
                    resp = input('Gostaria de ARMAR os CANHÕES e ATIRAR novamente(s ou n)? ')
                    if resp == 'n':
                        resultado()
                    elif resp not in ['s', 'n']:
                        print('Informe s para jogar novamente ou n para parar de jogar!')
                        continue
                    break
                break
            else:
                print('Em qual posição vai atirar novamente Capitão??')