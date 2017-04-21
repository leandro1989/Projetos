from random import *
from socket import *

def cria_grelha(matriz):
    '''esta função cria uma matriz 10X10'''
    for i in range(10):
        matriz.append([])
        for j in range(10):
            matriz[i].append('~')

def interface(linha_numero,matriz_inimigo):
    '''Mostra o Tabuleiro que aparecerá as embarcações e os tiros dados'''
    print('     |   %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |'%(linha_numero[0],linha_numero[1],linha_numero[2],linha_numero[3],linha_numero[4],
                                                                                           linha_numero[5],linha_numero[6],linha_numero[7],linha_numero[8],linha_numero[9]),'     ',
          '     |   %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |'%(linha_numero[0],linha_numero[1],linha_numero[2],linha_numero[3],linha_numero[4],
                                                                                           linha_numero[5],linha_numero[6],linha_numero[7],linha_numero[8],linha_numero[9]))
    print('     ---------------------------------------------------------------','         ', ' ---------------------------------------------------------------')

    for k in range(10):

        print('  %s  |   %s     %s     %s     %s     %s     %s     %s     %s     %s     %s   |      ' %(letras[k],matriz_inimigo[k][0],matriz_inimigo[k][1], matriz_inimigo[k][2],
                                                                                                  matriz_inimigo[k][3], matriz_inimigo[k][4],matriz_inimigo[k][5],matriz_inimigo[k][6],
                                                                                                  matriz_inimigo[k][7], matriz_inimigo[k][8], matriz_inimigo[k][9]),

              '  %s  |   %s     %s     %s     %s     %s     %s     %s     %s     %s     %s   |      ' %(letras[k],matriz_aliado[k][0],matriz_aliado[k][1], matriz_aliado[k][2], matriz_aliado[k][3],
                                                                                                               matriz_aliado[k][4], matriz_aliado[k][5], matriz_aliado[k][6], matriz_aliado[k][7],
                                                                                                               matriz_aliado[k][8], matriz_aliado[k][9]))
    print('     ---------------------------------------------------------------', '         ', ' ---------------------------------------------------------------')
    print('                 Mar das embarcações do meu INIMIGO                                                Mar das MINHAS embarcações')

def pede_barco1(conta_barco):
    if len(conta_barco) == 0:
        x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                    '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                    '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                    '\n 3) Barco que ocupa três posições(Digite 3)? '
                                    '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                    '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
        conta_barco.append(x)
    return x

def pede_barco2(conta_barco):
    if len(conta_barco) == 1:

        if 0 in conta_barco: #se não der certo tentar com n.count(1) < 1
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 1 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 2 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1

        elif 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? \n')) - 1
            conta_barco.append(x)

    return x

def pede_barco3(conta_barco):
    if len(conta_barco) == 2:

        if 0 in conta_barco and 1 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 0 in conta_barco and 2 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: '
                                        '\n 2) Barco que ocupa duas posição(Digite 2)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 0 in conta_barco and 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar:\n '
                                        '\n 2) Barco que ocupa duas posição(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 0 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? \n')) - 1
            conta_barco.append(x)

        elif 1 in conta_barco and 2 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 3) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cindo posições(Digite 5)? \n')) - 1
            conta_barco.append(x)

        elif 1 in conta_barco and 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)

        elif 1 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n'
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? \n')) - 1
            conta_barco.append(x)

        elif 2 in conta_barco and 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)

        elif 2 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? \n')) - 1
            conta_barco.append(x)

        elif 3 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? \n')) - 1
            conta_barco.append(x)
    return x

def pede_barco4(conta_barco):

    if len(conta_barco) == 3:

        if 0 in conta_barco and 1 in conta_barco and 2 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)
        elif 0 in conta_barco and 1 in conta_barco and 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)

        elif 0 in conta_barco and 2 in conta_barco and 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)

        elif 0 in conta_barco and 2 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? \n')) - 1
            conta_barco.append(x)

        elif 0 in conta_barco and 3 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? \n')) - 1
            conta_barco.append(x)

        elif 1 in conta_barco and 2 in conta_barco and 3 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
            conta_barco.append(x)

        elif 1 in conta_barco and 2 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 4) Barco que ocupa quatro posições(Digite 4)? \n')) - 1
            conta_barco.append(x)

        elif 1 in conta_barco and 3 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 3) Barco que ocupa três posições(Digite 3)? \n')) - 1
            conta_barco.append(x)

        elif 2 in conta_barco and 3 in conta_barco and 4 in conta_barco:
            x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                        '\n 1) Barco que ocupa uma posição(Digite 1)? '
                                        '\n 2) Barco que ocupa duas posições(Digite 2)? \n')) - 1
            conta_barco.append(x)

    return x

def pede_barco5(conta_barco):

    if 1 in conta_barco and 2 in conta_barco and 3 in conta_barco and 4 in conta_barco:
        x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                '\n 1) Barco que ocupa uma posições(Digite 1)? \n')) - 1
        conta_barco.append(x)

    elif 0 in conta_barco and 2 in conta_barco and 3 in conta_barco and 4 in conta_barco:
        x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                '\n 2) Barco que ocupa duas posições(Digite 2)? \n')) - 1
        conta_barco.append(x)

    elif 0 in conta_barco and 1 in conta_barco and 3 in conta_barco and 4 in conta_barco:
        x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                    '\n 3) Barco que ocupa três posições(Digite 3)? \n')) - 1
        conta_barco.append(x)

    elif 0 in conta_barco and 1 in conta_barco and 2 in conta_barco and 4 in conta_barco:
        x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                    '\n 4) Barco que ocupa quatro posições(Digite 4)? \n')) - 1
        conta_barco.append(x)

    elif 0 in conta_barco and 1 in conta_barco and 2 in conta_barco and 3 in conta_barco:
        x = int(input('Informe qual embarcação deseja colocar em alto mar: \n '
                                    '\n 5) Barco que ocupa cinco posições(Digite 5)? \n')) - 1
        conta_barco.append(x)

    return x

def verifica_tiro(numero,letra_tiro):
    '''esta função verifica se na matriz_aliado contém algum barco e substitui na matriz_inimigo que é a matriz do adversário'''

    if matriz_aliado[letras.find(letra_tiro)][numero - 1] == 1:
        '''Caso acerte o tiro aparece o número 1'''
        matriz_inimigo[letras.find(letra_tiro)][numero - 1] = 1

    else:
        matriz_inimigo[letras.find(letra_tiro)][numero - 1] = 'x'
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

'''Fim da Definição coloca_barco'''

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

'''FIm da definição verifica_coloca_barco'''

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
while resp == 's':

    letras = 'ABCDEFGHIJ'
    linha_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    matriz_aliado = []
    matriz_inimigo = []
    barcos = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
    cria_grelha(matriz_aliado)
    cria_grelha(matriz_inimigo)
    interface(linha_numero, matriz_inimigo)
    matriz_pede_barco = ['1) Barco que ocupa uma posições(Digite 1)','2) Barco que ocupa duas posições(Digite 2)?',
                         '3) Barco que ocupa três posições(Digite 3)', '4) Barco que ocupa quatro posições(Digite 4)', '5) Barco que ocupa cinco posições(Digite 5)']

    '''Com martriz_escolha_barco verifico se o barco solicitado já foi posicionado'''
    matriz_escolha_barco = []

    for i in range(len(barcos)):
        '''Esta parte do código pede ao usuário as posição e o sentido que o barco deve ser colocado, além de chamar funções para verificar se a posição é valida ou não.'''

        while True:
            try:
                for o in range(len(matriz_pede_barco)):
                    print(matriz_pede_barco[o])
                print('')
                x = int(input('Baseado nas opções acima. Informe o barco que você quer colocar: ')) - 1


                if x < 0 or x > 4:
                    print('Barco Inexistente. Informe um número que de 1 a 5.')
                    continue
                matriz_escolha_barco.append(x)

                if matriz_escolha_barco.count(x) > 1:
                    print('Esta embarcação já foi posicionado, por favor escolha outro barco.')
                    print('')
                    continue
                break
            except ValueError:
                print('Caractere inválido. Informe um número que de 1 a 5.')
                continue
        matriz_pede_barco[x] = ' '

        while True:
            while True:
                try:
                    print('')
                    sentido_do_barco = int(input('Capitão, a embarcação deve ser colocada na Horizontal(digite - 1) ou na Vertical(digite - 2)? '))
                    print('')

                    if sentido_do_barco not in [1, 2]:
                        print('Valor inválido! Informe 1 --> Horizontal ou 2 --> Vertical.')
                        continue
                    break
                except:
                    print('Caracter inválido! Informe 1 --> Horizontal ou 2 --> Vertical.')
                    continue

            while True:
                linha = input('Digite a letra da linha que a embarcação vai ser posicionada: ')
                linha = linha.upper()

                if linha not in['A','B','C','D','E','F','G','H','I','J']:
                    print('Letra inválida. Informe uma letra maiúscula que esteja entre A e J.')
                    continue
                while True:
                    try:
                        coluna = int(input('Qual o número da coluna que a embarcação vai ser posicionada: ')) - 1
                        print('')
                        if coluna < 0 or coluna > 10:
                            print('Valor inválido. Informe um número que esteja entre 1 e 10.')
                            continue
                        break
                    except:
                        print('Caracter inválido. Informe um número que esteja entre 1 e 10.')
                        continue
                break

            linha = letras.find(linha)

            if corrige(barcos[x],linha,coluna) == True and verifica_coloca_barco(barcos[x], linha, coluna, sentido_do_barco) == True:
                '''Esta parte chama as funções acima para verificar se é possível o barco ser colocado na posição solicitada.'''
                coloca_barco(linha,coluna,sentido_do_barco,matriz_aliado,barcos[x],0)
                interface(linha_numero, matriz_inimigo)
                print('')
                break
            else:
                print('Posição inválida ou já existe um barco na posição determinada')
                continue

    '''Fim do For '''

    print('\n Agora começa a Batalha Naval! Selecione as posicões para atirar!')
    print('')

    while True:
        '''Esta parte pede a posição que o jogador vai atirar'''
        while True:
            c = input('Capitão, Informe a letra da linha que o tiro vai acertar: ')
            letra_tiro = c.upper()

            if letra_tiro not in letras:
                print('Letra inválida. Informe uma letra maiúscula de A a J.')
                print('')
                continue
            else:
                break

        while True:
            try:
                numero = int(input('Capitão, informe o número da coluna que o tiro vai acertar: '))
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
        interface(linha_numero, matriz_inimigo)
        print('')

        contador_de_seus_acertos = 0

        for y in range(0,10):
            '''Verifica se vc ganhou a batalha.'''
            contador_de_seus_acertos += matriz_inimigo[y].count(1)

        if contador_de_seus_acertos == 15:
            print('✌✌✌✌✌✌✌✌✌✌✌CAPITÃO GANHAMOS!! Parabéns! ✌✌✌✌✌✌✌✌✌✌✌✌')

            while True:
                resp = input('CAPITÃO! Gotaria de ARMAR os CANHÕES e ATIRAR novamente(s ou n)? ')
                if resp not in ['s','n']:
                    print('Informe s para jogar novamente ou n para parar de jogar!')
                    continue
                break
            break
        else:
            print('Em qual posição vamos atirar novamente Capitão??')

    '''
        contador_de_acertos_inimigo = 0

        for y in range(0,10):
            Verifica se seu inimigo ganhou a batalha.
            contador_de_acertos_inimigo += matriz_aliado[y].count(1)

        if contador_de_acertos_inimigo == 15:
            print('Você Ganhou!! Parabéns')
            break

        else:
            print('Em qual posição vai atirar novamente Capitão??')
            print('')
    '''