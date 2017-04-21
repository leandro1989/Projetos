from socket import *
import sys
from termcolor import colored

host = '192.168.0.104'
port = 5000
tcp = socket(AF_INET, SOCK_STREAM)
dest = (host, port)
tcp.bind(dest)
tcp.listen(1)

def cria_grelha(matriz):
    '''esta função cria uma matriz 10X10'''
    for i in range(10):
        matriz.append([])
        for j in range(10):
            D = colored('~', 'blue')
            matriz[i].append(D)

def interface():
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

def regras():
    print('\n Lembrando algumas regras da Batalha Naval: \n '
      '\n 1 - Não é possível colocar um embarcação ao lado de outra embarcação; '
      '\n 2 - Os limites dados no tabuleiro devem ser respeitados, ou seja, não pode ficar nenhuma parte da embarcação fora '
      '\n      do tabuleleiro, caso isso ocorra será solicitada uma nova posição; '
      '\n 3 - Uma embarcação não pode ser colocada em uma posição já ocupada por alguma parte de outra embarcação;'
      '\n 4 - Caso uma embarcação seja acertada aparecerá a letra X no local atirado, caso contrário será exibida a letra "O";'
      '\n 5 - O jogador que primeiro afundar todas embarcações ganha;'
      '\n 6 - Ao selecinar uma posição para o barco, a parte inicial da embarcação será colocada na posição selecinada,'
      ' \n     as demais parte serão colocada no sentido(Horizontal ou vertical) que você escolher;')

def verifica_tiro_entrada(linha,coluna):
    if matriz_aliado[linha][coluna] == 1:
        conecxao.send(b'X')
        matriz_aliado[linha][coluna] = colored('X', 'red')
    else:
        conecxao.send(b'O')
        matriz_aliado[linha][coluna] = colored('O', 'green')

def verifica_tiro_saida (linha, coluna, recebe_dado):
    matriz_inimigo[linha][coluna] = colored(recebe_dado,'red')

def coloca_barco(linha,coluna,sentido_do_barco,matriz_aliado,barco,i):
    '''Esta função coloca o barco na posição desejada e coloca 'a' em volta dos barcos para não ser possível colocar barcos adjacentes'''

    a = colored('x', 'yellow')  #O caractere atribuido ao termo 'a' será colocado em volta dos barcos

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
    b = colored('~', 'blue') #colocado no tabuleiro inteiro, mas aqui é simplesmente para verificação se é valido colocar o barco.
    c = colored('x', 'yellow')#colocado em volta dos barcos, mas aqui é simplesmente para verificação se é valido colocar o barco.
    if sentido_do_barco == 1:

        try:
            for p in range(len(barco)):
                '''Verifica se tem algum 'x' ou '1' nas posições que serão ocupadas pelo barco ou se o barco excede o limite do tabuleiro
                , permitindo ou não que o barco seja inserido'''
                if c not in matriz_aliado[linha][coluna:coluna + len(barco)] and 1 not in matriz_aliado[linha][coluna:coluna + len(barco)]:
                    return True
        except:
            return False

        cont_h = 0

        for p in range(coluna - 1, coluna + len(barco)):
            '''Esta parte verifica e impede que alguma parte do barco seja substituida por 'a', impedindo a colocação do barco.
            O elemento matriz_aliado[linha][p] pode ser uma parte de uma embarcação colocada anteriormente.'''
            if b != matriz_aliado[linha][p]:
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
                if matriz_aliado[p][coluna] == b:
                    cont_v += 1
            except IndexError:
                return False

            if cont_v >= len(barco):
                return True
    else:
        return False

while True:
    p = input('Gostaria de ler as regras do jogo(s ou n)? ')
    regra = p.upper()
    if regra not in ['S', 'N']:
        print('Caractere inválido. Informe S para sim ou N para não!')
        continue
    if regra == 'S':
        regras()
        break
    else:
        break

print('')
print('Saudações, Capitão! Bem vindo a bordo! Para iniciarmos a batalha vamos posicionar nossas embarcações: ')
print('')
print('Esperando o outro jogar! Wait Please...')
print('')

resp_2 = 'S'
 
while True:
    conecxao, cliente = tcp.accept()
    while resp_2 == 'S':

        letras = ['A','B','C','D','E','F','G','H','I','J']
        linha_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        matriz_aliado = []
        matriz_inimigo = []
        barcos = [[1],[1,1],[1,1,1],[1,1,1,1],[1,1,1,1,1]]
        cria_grelha(matriz_aliado)
        cria_grelha(matriz_inimigo)
        X = colored('X', 'red') #Acertou em um barco
        matriz_pede_barco = ['1) Barco que ocupa uma posições(Digite 1)', '2) Barco que ocupa duas posições(Digite 2)','3) Barco que ocupa três posições(Digite 3)',
                             '4) Barco que ocupa quatro posições(Digite 4)','5) Barco que ocupa cinco posições(Digite 5)']
        interface()
        print('')

        '''Com matriz_escolha_barco verifico se o barco solicitado já foi posicionado'''
        matriz_escolha_barco = []

        for i in range(len(barcos)):
            '''Esta parte do código pede ao usuário as posição e o sentido que o barco deve ser colocado, além de chamar funções para verificar se a posição é valida ou não.'''

            while True:
                try:
                    for k in range(len(matriz_pede_barco)):
                        print(matriz_pede_barco[k])
                    print('')
                    barco_escolhido = int(input('Baseado nas opções acima. Informe o barco que você quer colocar: ')) - 1

                    if barco_escolhido < 0 or barco_escolhido > 4:
                        print('Barco Inexistente. Informe um número que de 1 a 5.')
                        continue
                    matriz_escolha_barco.append(barco_escolhido)

                    if matriz_escolha_barco.count(barco_escolhido) > 1:
                        print('Esta embarcação já foi posicionado, por favor escolha outro barco.')
                        print('')
                        continue
                    break
                except ValueError:
                    print('Caractere inválido. Informe um número que de 1 a 5.')
                    continue
            matriz_pede_barco[barco_escolhido] = ' '

            while True:
                while True:
                    try:
                        if barco_escolhido != 0:  #Se O barco escolhido não for que ocupa uma posição
                            sentido_do_barco = int(input('Capitão, a embarcação deve ser colocada na Horizontal(digite - 1) ou na Vertical(digite - 2)? '))
                        else:
                            sentido_do_barco = 1

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
                        print('Caractere inválido. Informe uma letra que esteja de A a J.')
                        continue
                    while True:
                        try:
                            coluna = int(input('Digite o número da coluna que a embarcação vai ser posicionada: ')) - 1
                            print('')
                            if coluna < 0 or coluna > 10:
                                print('Valor inválido. Informe um número que esteja entre 1 e 10.')

                                continue
                            break
                        except:
                            print('Caracter inválido. Informe um número que esteja entre 1 e 10.')

                            continue
                    break

                linha = letras.index(linha)

                if corrige(barcos[barco_escolhido],linha,coluna) == True and verifica_coloca_barco(barcos[barco_escolhido], linha, coluna, sentido_do_barco) == True:
                    '''Esta parte chama as funções acima para verificar se é possível o barco ser colocado na posição solicitada.'''
                    coloca_barco(linha,coluna,sentido_do_barco,matriz_aliado,barcos[barco_escolhido],0)
                    interface()
                    print('')
                    break
                else:
                    print('Posição inválida ou já existe um barco na posição determinada!')
                    interface()
                    continue
        print('\n Agora começa a Batalha Naval! Selecione as posicões para atirar!')
        print('')

        '''Fim do For '''

        while True:
            '''aki espera o outro usuario'''
            print('Esperando o INIMIGO  posicionar os barcos!')
            print('')
            conecxao.send(b'ok')
            recebe_comfirmação = conecxao.recv(1024)
            if recebe_comfirmação == b'ok':
                break
            else:
                continue
        while True:
            print('Aguardando o usuario online atirar...\nwait please.')
            for i in range(2):
                if i ==0:
                    letra_inimigo = conecxao.recv(1024)
                    letra_inimigo = str(letra_inimigo,'utf-8')
                    letra_inimigo = int(letra_inimigo)                
                else:
                    numero_inimigo = conecxao.recv(1024)
                    numero_inimigo = str(numero_inimigo, 'utf-8')
                    numero_inimigo = int(numero_inimigo)        
            
            verifica_tiro_entrada(letra_inimigo, numero_inimigo-1)
            interface()

            acertos_inimigos = 0
            
            for y in range(0,10):
                '''Verifica se vc ganhou a batalha.'''
                acertos_inimigos += matriz_aliado[y].count(X) #X = colored('X', 'red')

            if acertos_inimigos == 15:
                print('O INIMIGO GANHOU!! DA PRÓXIMA GANHAMOS!')
                while True:
                    resp = input('Gostaria de Jogar novamente(s ou n):')
                    resp_2 = resp.upper()
                    if resp_2 not in ['S','N']:
                        print('Informe s para jogar novamente ou n para parar de jogar!')
                        continue
                    if resp_2 =='N':
                        conecxao.send(b'nao')
                        print('Até a proxima Capitão!!!')
                        resp_nao = conecxao.recv(1024)
                        conecxao.close()
                        while True:
                            '''o jogo acabou'''

                    if resp_2 == 'S':
                        while True:
                            print('aguardando o jogador responder...')
                            conecxao.send(b'ok')
                            revanche = conecxao.recv(1024)
                            if revanche == b'nao':
                                print('O outro jogodor parou de jogar!!')
                                conecxao.close()
                                while True:
                                    '''acabou o jogo'''
                                    
                                break
                            if revanche == b'ok':
                                break
                            break
                        break
                    break
                break

            for j in range(2):
                if j ==0:
                    while True:
                        letra_local = input('Capitão, imforme a letra da linha que o tiro vai acertar: ')
                        letra_tiro = letra_local.upper()
                        if letra_tiro not in letras:
                            print('Caractere inválido. Imforme uma letra maiúscula de A a J. ')
                            print('')
                            continue
                        else:
                            break
                    letra_local = letras.index(letra_tiro)
                    recebe_letra = letra_local
                    letra_local = bytes(str(letra_local),'utf-8')
                    conecxao.send(letra_local)
                            
                else:
                    while True:
                        try:
                            numero_local = int(input('Capitão, imforme o numero da coluna que o tiro vai acertar:'))
                            rec_numero = numero_local
                            if numero_local<0 or numero_local>10:
                                print('Capitão, o senhor imformou um numero inválido, imforme um número de 1 a 10.')
                                continue
                            else:
                                break
                        except:
                            continue
                    numero_local = bytes(str(numero_local), 'utf-8')
                    conecxao.send(numero_local)
            teste_dado = conecxao.recv(1024)
            teste_dado = str(teste_dado, 'utf-8')
                    
            verifica_tiro_saida(recebe_letra, rec_numero - 1, teste_dado)#subistitui na matriz do adversário se acertou por X ou O se errou
            interface()

            meus_acertos = 0
            
            for y in range(0,10):
                '''Verifica se vc ganhou a batalha.'''
                meus_acertos += matriz_inimigo[y].count(X) #X = colored('X', 'red')

            if meus_acertos == 15:
                print(colored('✌✌✌✌✌✌✌✌✌✌✌CAPITÃO, GANHAMOS!! Parabéns!✌✌✌✌✌✌✌✌✌✌✌✌', 'red'))
                print('')
                print(colored('✌✌✌✌✌✌✌✌✌✌✌CAPITÃO, GANHAMOS!! Parabéns!✌✌✌✌✌✌✌✌✌✌✌✌', 'yellow'))

                while True:
                    resp = input('Gostaria de Jogar novamente(s ou n):')
                    resp_2 = resp.upper()
                    if resp_2 not in ['S','N']:
                        print('Informe s para jogar novamente ou n para parar de jogar!')
                        continue
                    if resp_2 == 'N':
                        conecxao.send(b'nao')
                        print('Até a proxima Capitão!!!')
                        resp_inimigo = conecxao.recv(1024)
                        conecxao.close()
                        while True:
                            '''acabou o jogo'''

                    if resp_2 == 'S':
                        while True:
                            print('Aguardando o jogador responder...')
                            conecxao.send(b'ok')
                            revanche = conecxao.recv(1024)
                            revanche  = str(revanche, 'utf-8')
                            if revanche == 'nao':
                                print('O outro jogodor parou de jogar!!')
                                conecxao.close()
                                while True:
                                    '''Acabou o jogo'''

                            if revanche == b'ok':
                                break
                            break
                        break
                    break
                break