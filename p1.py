import os

LARGURA = 5
ALTURA = 5

# Posição inicial do Robô (x=coluna, y=linha)
robo_x = 0
robo_y = 0

# Posição do Alvo (Target)
alvo_x = 3
alvo_y = 3


def move_north():
    global robo_y
    # Só move para cima se não bater no limite superior (y = 0)
    if robo_y > 0:
        robo_y -= 1

def move_south():
    global robo_y
    # Só move para baixo se não bater no limite inferior
    if robo_y < ALTURA - 1:
        robo_y += 1

def move_east():
    global robo_x
    # Só move para a direita se não bater no limite da largura
    if robo_x < LARGURA - 1:
        robo_x += 1

def move_west():
    global robo_x
    # Só move para a esquerda se não bater no limite esquerdo (x = 0)
    if robo_x > 0:
        robo_x -= 1

def desenhar_mapa():
    # Limpa o terminal (funciona tanto em Linux/Mac quanto Windows)
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Varre cada linha e cada coluna para desenhar a matriz
    for y in range(ALTURA):
        linha = ""
        for x in range(LARGURA):
            if x == robo_x and y == robo_y:
                linha += "R " # Desenha o robô
            elif x == alvo_x and y == alvo_y:
                linha += "T " # Desenha o alvo
            else:
                linha += ". " # Desenha o espaço vazio
        print(linha)
    
    # Exibe as coordenadas atuais para facilitar o debug
    print(f"\nPosição do Robô: ({robo_x}, {robo_y})")

while True:
    desenhar_mapa()
    
    # Aguarda o usuário digitar um comando
    comando = input("Digite um comando (w=norte, s=sul, d=leste, a=oeste, q=sair): ").lower()
    
    # Toma uma ação baseada no comando digitado
    if comando == 'w':
        move_north()
    elif comando == 's':
        move_south()
    elif comando == 'd':
        move_east()
    elif comando == 'a':
        move_west()
    elif comando == 'q':
        print("Encerrando a simulação...")
        break 
    else:
        print("Comando inválido!")