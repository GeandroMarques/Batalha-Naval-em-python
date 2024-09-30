import random
#menu

def como_jogar():
    print()
    print("Como jogar?")
    print("O jogador deverá posicionar 5 barcos no seu tabuleiro,")
    print("para isso o jogador deverá escolher a linha e a coluna")
    print("(as linhas e colunas vão de 1 a 10) para posicionar")
    print("seus barcos. Após isso o jogador deverá tentar adivinhar")
    print("a posição dos navios do computador, o computador também")
    print("tentará destruir os seus navios, o jogo termina quando")
    print("você destruir todos os navios do computador ou vice-versa.")
    print()

def menu_principal():
    while True:
        print("Bem vindo ao Batalha Naval, escolha entre as opções abaixo!")
        menu = input("1: Jogar   2: Como Jogar: ")
        if menu == '1' or menu == '2':
            # Mostra as instruções se o jogador escolher a opção como jogar.
            if menu == '2':
                como_jogar()
            # Começa o jogo se o jogador escolher a opção jogar
            elif menu == '1':
                print("Começando a batalha...")
                break
        # Mostra a mensagem se o jogador escolher uma opção que nao existe
        else:
            print("Valor inválido, digite novamente.")

menu_principal()

def criar_matrizPlayer():
    # Guarda a posição dos navios do jogador
    global salvaPosiPlayer
    salvaPosiPlayer = []
    # Matriz para jogadas do jogador
    global posijogadasPlayer
    posijogadasPlayer = []
    # Criar matrizes
    for i in range(10):
        # Matriz que mostra o tabuleiro com a posição dos barcos
        salvaPosiPlayer.append(['A'] * 10)
        # Matriz que mostra o tabuleiro com as jogadas do jogador
        posijogadasPlayer.append(['A'] * 10)

criar_matrizPlayer()



# função que verifica se a posição é válida
def posicao_valida(matriz, linha, coluna, tamanho, orientacao):
    if orientacao == 'H':
        # Se o navio for posicionado na horizontal, pega o número da coluna e subtraí o valor do tamanho do navio, se esse numero for menor que 0 ele retorna falso
        # Se o número for menor que 0 uma parte do navio ficaria fora do tabuleiro
        if coluna - tamanho + 1 < 0:
            return False
        for i in range(tamanho):
            # Aqui ele avalia se não existe outro navio já posicionado naquele local
            if matriz[linha][coluna - i] != 'A':
                return False
    else:
        if linha - tamanho + 1 < 0:
            # Se o navio for posicionado na vertical, pega o número da linha e subtraí o valor do tamanho do navio, se esse numero for menor que 0 ele retorna falso
            # Se o número for menor que 0 uma parte do navio ficaria fora do tabuleiro
            return False
        for i in range(tamanho):
            # Verifica se ja existe algum navio posicionado naquela posição
            if matriz[linha - i][coluna] != 'A':
                return False
    # Caso nao tenha nenhum navio naquela posição ou o navio nao fique fora do tabuleiro, a funçao retorna true
    return True


# Função para posicionar os navios no tabuleiro
numeracaoNavios = 16
def posicionar_navio(matriz, linha, coluna, tamanho, orientacao):
    #numeraçao a partir do 16 pra nao repetir os navios do computador
    global numeracaoNavios
    # Verifica a posição que o jogador escolheu (vertical ou horizontal)
    if orientacao == 'H':
        for i in range(tamanho):
            # Adiciona à matriz
            matriz[linha][coluna - i] = str(f'{numeracaoNavios}')
            # Adiciona +1 para não repetir os numeros
            numeracaoNavios += 1
    else:
        for i in range(tamanho):
            # Adiciona à matriz
            matriz[linha - i][coluna] = str(f'{numeracaoNavios}')
            numeracaoNavios += 1


# Função que pergunta ao jogador as posições para posicionar o navio
def posicao_Player():
    # Lista com o tamanho dos diferentes tipos de navios
    tamanhos_navios = [5, 4, 3, 2, 1]
    orientacoes = {'1': 'H', '2': 'V'}
    # Loop que posiciona os navios
    for tamanho in tamanhos_navios:
        while True:
            # Pergunta ao jogador se ele quer posicionar o navio na horizontal ou vertical
            posicaonavio = input(f"Digite 1 para posicionar o navio de {tamanho} posições na horizontal e 2 para posicionar na vertical: ")
            if posicaonavio in orientacoes:
                orientacao = orientacoes[posicaonavio]
                if orientacao == 'H':
                    print("Lembre-se, a casa que você escolher estará representando a frente do navio que estará apontado para a direita")
                    # Pergunta linha e coluna ao jogador em string para não quebrar o código quando o jogador colocar um digito inválido ou apertar enter sem nada escrito
                    linhaJ = input("Digite a linha desejada para posicionar o navio (1-10): ")
                    colunaJ = input(f"Digite a coluna desejada para posicionar o navio ({tamanho}-10): ")
                    # Verifica se o input do jogador está de acordo com o que foi pedido
                    if linhaJ in [str(i) for i in range(1, 11)] and colunaJ in [str(i) for i in range(tamanho, 11)]:
                        # Transforma em int para subtrair 1 numero já que o programa começa a contar a partir do 0
                        linhaJ = int(linhaJ) - 1
                        colunaJ = int(colunaJ) - 1
                        # Verifica se a posição é válida antes de posicionar o navio
                        if posicao_valida(salvaPosiPlayer, linhaJ, colunaJ, tamanho, orientacao):
                            posicionar_navio(salvaPosiPlayer, linhaJ, colunaJ, tamanho, orientacao)
                            for linha in range(len(salvaPosiPlayer)):
                                print(salvaPosiPlayer[linha])
                            break
                        else:
                            # Posição inválida caso a posição esteja ocupada ou o navio fique com alguma parte fora do tabuleiro
                            print("Posição inválida")
                    else:
                        # Posição inválida caso o jogador digite algum valor fora do tamanho do tabuleiro
                        print("Posição inválida")
                else:
                    print("Lembre-se, a casa que você escolher estará representando a frente do navio que estará apontado para baixo")
                    # Pergunta linha e coluna ao jogador em string para não quebrar o código quando o jogador colocar um digito inválido ou apertar enter sem nada escrito
                    linhaJ = input(f"Digite a linha desejada para posicionar o navio ({tamanho}-10): ")
                    colunaJ = input("Digite a coluna desejada para posicionar o navio (1-10): ")
                    # Verifica se o input do jogador está de acordo com o que foi pedido
                    if linhaJ in [str(i) for i in range(tamanho, 11)] and colunaJ in [str(i) for i in range(1, 11)]:
                        # Transforma em int para subtrair 1 numero já que o programa começa a contar a partir do 0
                        linhaJ = int(linhaJ) - 1
                        colunaJ = int(colunaJ) - 1
                        # Verifica se a posição é válida antes de posicionar o navio
                        if posicao_valida(salvaPosiPlayer, linhaJ, colunaJ, tamanho, orientacao):
                            posicionar_navio(salvaPosiPlayer, linhaJ, colunaJ, tamanho, orientacao)
                            for linha in range(len(salvaPosiPlayer)):
                                print(salvaPosiPlayer[linha])
                            break
                        else:
                            # Posição inválida caso a posição esteja ocupada ou o navio fique com alguma parte fora do tabuleiro
                            print("Posição inválida")
                    else:
                        # Posição inválida caso o jogador digite algum valor fora do tamanho do tabuleiro
                        print("Posição inválida")
            else:
                # Opção inválida caso o jogador digite algo diferente de 1 ou 2
                print("Opção inválida. Digite 1 para horizontal ou 2 para vertical.")

    return salvaPosiPlayer

salvaPosiPlayer = posicao_Player()

#numero de navios
naviosPlayer = 5
#vida dos navios do jogador
navios5Player = 5
navios4Player = 4
navios3Player = 3
navios2Player = 2
navios1Player = 1
#Quando o computador acertar um navio chamará essa função para analisar qual navio foi acertado
def vida_naviosPlayer(x, y, salvaPosiPlayer):
    global navios5Player
    global navios4Player
    global navios3Player
    global navios2Player
    global navios1Player
    global naviosPlayer
    # verifica qual navio foi atingido e tira uma vida
    if salvaPosiPlayer[x][y] in ['16', '17', '18', '19', '20']:
        navios5Player -= 1
    elif salvaPosiPlayer[x][y] in ['21', '22', '23', '24']:
        navios4Player -= 1
    elif salvaPosiPlayer[x][y] in ['25', '26', '27']:
        navios3Player -= 1
    elif salvaPosiPlayer[x][y] in ['28', '29']:
        navios2Player -= 1
    elif salvaPosiPlayer[x][y] == '30':
        navios1Player -= 1

    # quando a vida chega a 0 o navio é derrubado e a vida desse navio passa a ser -1 para não diminuir o número de navios por causa de um navio já derrubado
    if navios5Player == 0:
        naviosPlayer -= 1
        navios5Player -= 1
        return naviosPlayer
    elif navios4Player == 0:
        naviosPlayer -= 1
        navios4Player -= 1
        return naviosPlayer
    elif navios3Player == 0:
        naviosPlayer -= 1
        navios3Player -= 1
        return naviosPlayer
    elif navios2Player == 0:
        naviosPlayer -= 1
        navios2Player -= 1
        return naviosPlayer
    elif navios1Player == 0:
        naviosPlayer -= 1
        navios1Player -= 1
        return naviosPlayer

# Função responsável pelos ataques do jogador aos navios do computador
prev_jogadasPlayer = []
def jogar_Player():
    # lista que guarda as posições das jogadas anteriores
    global prev_jogadasPlayer
    global salvaPosiIA
    while True:
        global naviosIA
        # Linha
        global linhajogadaJ
        linhajogadaJ = input("Digite a linha desejada para tentar acertar o navio adversário(1-10): ")
        # Evita que o jogador escolha algo diferente de um número de 1 a 10, pede o input em string para evitar erros ou quebra do código
        if linhajogadaJ in [str(i) for i in range(1, 11)]:
            # Transforma em int
            linhajogadaJ = int(linhajogadaJ)
            # Subtrai -1 porque o programa começa a contar a partir do 0
            linhajogadaJ -= 1
            # Coluna
            global colunajogadaJ
            colunajogadaJ = input("Digite a coluna desejada para tentar acertar o navio adversário(1-10): ")
            # Evita que o jogador escolha algo diferente de um número de 1 a 10
            if colunajogadaJ in [str(i) for i in range(1, 11)]:
                colunajogadaJ = int(colunajogadaJ)
                colunajogadaJ -= 1
                catenacaoJ = str(linhajogadaJ) + str(colunajogadaJ)
                # Verifica se a jogada ja foi feita
                if catenacaoJ not in prev_jogadasPlayer:
                    prev_jogadasPlayer.append(catenacaoJ)
                    # Verifica se acertou ou errou
                    if salvaPosiIA[linhajogadaJ][colunajogadaJ] != 0:
                        posijogadasPlayer[linhajogadaJ][colunajogadaJ] = 'X'
                        vida_naviosIA(linhajogadaJ, colunajogadaJ, salvaPosiIA)
                        break
                    else:
                        posijogadasPlayer[linhajogadaJ][colunajogadaJ] = 'O'
                        break
                else:
                    print("Você ja escolheu essa posição, por favor escolha outra.")
            else:
                print(
                    "Valor inválido, digite novamente a linha e a coluna desejada e certifique-se de escolher um número de 1 a 10.")
        else:
            print("Valor inválido, digite um número de 1 a 10.")



# Imprime a matriz das jogadas do jogador
def imprimir_jogadasPlayer(linhajogadaJ, colunajogadaJ):
    global naviosIA
    # Imprime a matriz com as posições que o jogador escolheu
    for i in range(len(posijogadasPlayer)):
        print(posijogadasPlayer[i])
    # Imprime as posições escolhidas pelo jogador
    print(f'O jogador escolheu a linha: {linhajogadaJ + 1}')
    print(f'O jogador escolheu a coluna: {colunajogadaJ + 1}')
    # Imprime se o jogador acertou ou errou e imprime o número de navios restantes
    if posijogadasPlayer[linhajogadaJ][colunajogadaJ] == 'X':
        print(f"O jogador acertou, o computador possui {naviosIA} navio(s) restante(s)!")
    else:
        print(f"O jogador errou, o computador possui {naviosIA} navio(s) restante(s)")


#Função que irá criar as matizes pro computador
def Criar_MatrizIA():
    #Salva as posições dos navios do computador
    global salvaPosiIA
    salvaPosiIA = []
    #Matriz para jogadas do computador
    global posiJogadasIA
    posiJogadasIA = []
    #Cria as matrizes
    for i in range(10):
        salvaPosiIA.append([0]*10)
        posiJogadasIA.append(['A']*10)

Criar_MatrizIA()

#verifica se as próximas espaços estão disponíveis para posicionar os navios
def verificar(l, c, direcao, z):
    contador = 0
    #para entender essa parte é recomendado ver primeiro a próxima da próxima função 
    # irá verificar se a posição está disponível para posicionar o navio
    if direcao == 1:
        for i in range(c, (c+z)):
            # Estou utilizando o try e except, porque ocorerrá muitas vezes em que o indíce estará fora do alcance
            try:
                if salvaPosiIA[l][i] == 0:
                    contador += 1
            # Aqui quando ocorrer o erro retornará false para indicar que essa posição não está disponível e assim o computador irá tentar uma nova posição para o navio
            except IndexError:
                return False
    elif direcao == 2:
        for i in range(l, (l+z)):
            try:
                if salvaPosiIA[i][c] == 0:
                    contador += 1
            except IndexError:
                return False
    #Confirma se todas posições estão disponíveis
    if contador == z:
        return True
    else:
        return False

numero = 1
def posiciona_IA(l, c, salvaPosiIA, z):
    global numero
    #horizontal
    if direcao == 1:
        for i in range(c, (c+z)):
            salvaPosiIA[l][i] = numero
            numero += 1
    #vertical
    elif direcao == 2:
        for i in range(l, (l+z)):
            salvaPosiIA[i][c] = numero
            numero += 1

#Guarda as posições dos navios do computador
def posicao_IA():
    #Quantidade de navios do computador
    global naviosIA
    global direcao
    naviosIA = 0
    # a variável numero é para diferenciar cada navio 
    
    count = 0
    while count < 5:
        #linha
        l = random.randint(0, 9)
        #coluna
        c = random.randint(0,9)
        #Horizontal ou vertical
        # 1 - horizontal
        # 2 - vertical
        direcao = random.randint(1,2)
        #z é para alterar o range do for da função verificar, dependendo do tamanho do navio
        #navio 5 posições
        if count == 0 and verificar(l, c, direcao, z = 5):
            posiciona_IA(l, c, salvaPosiIA, z=5)
            count += 1
            naviosIA += 1
        #navio 4 posições
        elif count == 1 and verificar(l, c, direcao, z = 4):
            posiciona_IA(l, c, salvaPosiIA, z=4)
            count += 1
            naviosIA += 1
        #navio 3 posições
        elif count == 2 and verificar(l, c, direcao, z = 3):
            posiciona_IA(l, c, salvaPosiIA, z=3)
            count += 1
            naviosIA += 1
        #navio 2 posições
        elif count == 3 and verificar(l, c, direcao, z = 2):
            posiciona_IA(l, c, salvaPosiIA, z=2)
            count += 1
            naviosIA += 1
        #navio 1 posição
        elif count == 4 and salvaPosiIA[l][c] == 0:
            salvaPosiIA[l][c] = numero
            count += 1
            naviosIA += 1

            
posicao_IA()


#vida de cada navio
navios5IA = 5
navios4IA = 4
navios3IA = 3
navios2IA = 2
navios1IA = 1
#Quando o jogador acertar um navio chamará essa função para analisar qual navio foi acertado
def vida_naviosIA(linhajogadaJ, colunajogadaJ, salvaPosiIA):
    global navios5IA
    global navios4IA
    global navios3IA
    global navios2IA
    global navios1IA
    global naviosIA
    # verifica qual navio foi atingido e tira uma vida
    if salvaPosiIA[linhajogadaJ][colunajogadaJ] in [1, 2, 3, 4, 5]:
        navios5IA -= 1
    elif salvaPosiIA[linhajogadaJ][colunajogadaJ] in [6, 7, 8, 9]:
        navios4IA -= 1
    elif salvaPosiIA[linhajogadaJ][colunajogadaJ] in [10, 11, 12]:
        navios3IA -= 1
    elif salvaPosiIA[linhajogadaJ][colunajogadaJ] in [13, 14]:
        navios2IA -= 1
    elif salvaPosiIA[linhajogadaJ][colunajogadaJ] == 15:
        navios1IA -= 1

    # quando a vida chega a 0 o navio é derrubado e a vida desse navio passa a ser -1 para não diminuir o número de navios por causa de um navio já derrubado
    if navios5IA == 0:
        naviosIA -= 1
        navios5IA -= 1
        return naviosIA
    elif navios4IA == 0:
        naviosIA -= 1
        navios4IA -= 1
        return naviosIA
    elif navios3IA == 0:
        naviosIA -= 1
        navios3IA -= 1
        return naviosIA
    elif navios2IA == 0:
        naviosIA -= 1
        navios2IA -= 1
        return naviosIA
    elif navios1IA == 0:
        naviosIA -= 1
        navios1IA -= 1
        return naviosIA

#lista que guarda as posições jogadas anteriormentes
prev_Jogadas = []
#Computador tenta advinhar a posição dos navios do jogador
def jogar_IA():
    global prev_Jogadas
    global salvaPosiPlayer
    while True:
        #linha 
        global x
        x = random.randint(0, 9)
        #Coluna
        global y
        y = random.randint(0, 9)  
        catenacao = str(x) + str(y)
        #verifica se a jogada não foi feita antes
        if catenacao not in prev_Jogadas:
            prev_Jogadas.append(catenacao)
            #Verifica se acertou ou errou
            if salvaPosiPlayer[x][y] != 'A':
                posiJogadasIA[x][y] = 'X'
                vida_naviosPlayer(x, y, salvaPosiPlayer)
                break
            else:
                posiJogadasIA[x][y] = 'O'
                break

#imprime a matriz das jogadas feitas pelo computador
def imprimir_jogadaIA(x, y, naviosPlayer): 
    #imprime o tabuleiro das jogadas do computador
    for i in range(len(posiJogadasIA)):
        print(posiJogadasIA[i])
    #imprime as jogadas do computador
    print(f'O computador escolheu a linha: {x + 1}')
    print(f'O computador escolheu a coluna: {y + 1}')
    #imprime se acertou ou errou
    if posiJogadasIA[x][y] == 'X':
        print("O computador acertou")
    else:
        print("O computador errou")
    #imprime quantos navios o jogador ainda tem
    print(f'Navios do jogador restantes: {naviosPlayer}')
    

#Contadores para impedir que o computador/jogador jogue pela 3 vez depois de ter derrubado um navio(caso não derrube outro nessa jogada a mais)
countIA = 0
countPlayer = 0
#variável que guarda a vida dos navios antes de serem derrubados
prevNavioIA = 5
prevNavioPlayer = 5
while naviosIA != 0 and naviosPlayer != 0:
    #Verifica se um navio foi derrubado pelo computador
    if  prevNavioIA != naviosPlayer and (naviosIA != 0 and naviosPlayer != 0):
        prevNavioIA = naviosPlayer
        #Computador joga
        jogar_IA()
        imprimir_jogadaIA( x, y, naviosPlayer)
        countIA += 1
    #se o navio do jogador não tiver sido derrubado
    elif countPlayer < 2 and (naviosIA != 0 and naviosPlayer != 0):
        countIA = 0
        #Jogador joga
        jogar_Player()
        imprimir_jogadasPlayer(linhajogadaJ, colunajogadaJ)
        countPlayer += 1
    #Verifica se um navio foi derrubado pelo jogador
    if  prevNavioPlayer != naviosIA and (naviosIA != 0 and naviosPlayer != 0):
        prevNavioPlayer = naviosIA
        #Jogador joga
        jogar_Player()
        imprimir_jogadasPlayer(linhajogadaJ, colunajogadaJ)
        countPlayer += 1
    #se o navio do computador não tiver sido derrubado
    elif countIA < 2 and (naviosIA != 0 and naviosPlayer != 0):
        countPlayer = 0
        #Computador joga
        jogar_IA()
        imprimir_jogadaIA( x, y, naviosPlayer)
        countIA += 1

if naviosIA == 0:
    print("Parabéns, você venceu!")
    print("Obrigado por jogar!")
    print("Jogo criado pelos alunos: Juliano e Geandro")
else:
    print("O computador venceu!")
    print("Obrigado por jogar!")
    print("Jogo criado pelos alunos: Juliano e Geandro")
