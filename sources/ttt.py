from random import randrange

# usar configuracoes globais?

tabuleiro = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]


def tabuleiro_cheio():
    for linha in tabuleiro:
        for posicao in linha:
            if posicao == "":
                return False
    return True


# poderia ser com um tuplo ou dicionario
def fazer_jogada(x, y, jogador_humano=True):
    '''
    retorna True se a jogada for valida
    retorna False caso contrario
    '''
    if tabuleiro[x][y] == "":
        if jogador_humano is True:
            tabuleiro[x][y] = "X"
        else:
            tabuleiro[x][y] = "O"


def imprimir_tabuleiro():
    print "--------------"
    for linha in tabuleiro:
        for posicao in linha:
            if posicao == "":
                print "_",  # imprimir sem nova linha
            else:
                print posicao,  # imprimir sem nova linha
        print ""  # nova linha
    print "--------------"


def verificar_vencedor(jogador_humano=True):
    # verificar linhas
    venceu = False

    for linha in tabuleiro:
        venceu = True
        for posicao in linha:
            # se houver uma posicao vazia
            # ou do outro jogador
            # sai-se do ciclo
            if jogador_humano:
                if not posicao == "X":
                    venceu = False
                    break
            else:
                if not posicao == "O":
                    venceu = False
                    break

        if venceu:
            break

    return venceu


    # verificar colunas
    # verificar diagonais?

def realizar_turno(jogador_humano=True):
    # imprimir tabuleiro
    # fazer_jogada
    # verificar se ha vencedor
    # verificar se tabuleiro esta cheio
    # trocar de jogador
    imprimir_tabuleiro()

    if jogador_humano is True:
        posicao = raw_input("diga as coordenadas em formato xy: ")
        # try... except while cycle?
        x = int(posicao[0])
        y = int(posicao[1])

        while not tabuleiro[x][y] == "":
            posicao = raw_input("diga as coordenadas em formato xy: ")
            # try... except while cycle?
            x = int(posicao[0])
            y = int(posicao[1])

        # preencher posicao
        tabuleiro[x][y] = "X"
    else:
        # podia-se buscar lista de posicoes vazias
        x = randrange(3)
        y = randrange(3)
        while not tabuleiro[x][y] == "":
            x = randrange(3)
            y = randrange(3)

        # preencher posicao
        tabuleiro[x][y] = "O"

    if verificar_vencedor(True) is True:
        print "Jogador venceu"
        imprimir_tabuleiro()
    elif verificar_vencedor(False) is True:
        print "Computador venceu"
        imprimir_tabuleiro()
    elif tabuleiro_cheio():
        print "Empate"
    else:
        realizar_turno(not jogador_humano)

    # e quando o tabuleiro estiver cheio?

realizar_turno(False)
