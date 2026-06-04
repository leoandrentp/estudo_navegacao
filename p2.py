import os
import time  

LARGURA = 5
ALTURA = 5

# robot[0] é o X (colunas), robot[1] é o Y (linhas)
robot = [0, 0]
target = [2, 3]

def desenhar_mapa():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    for y in range(ALTURA):
        linha = ""
        for x in range(LARGURA):
            # Agora acessamos as coordenadas usando os índices da lista [0] e [1]
            if x == robot[0] and y == robot[1]:
                linha += "R "
            elif x == target[0] and y == target[1]:
                linha += "T "
            else:
                linha += ". "
        print(linha)
    
    print(f"\nPosição Atual do Robô: {robot}")
    print(f"Posição do Alvo: {target}")


while True:
    # 1º Passo: Tira uma "foto" do estado atual e mostra na tela
    desenhar_mapa()
    
    # 2º Passo: Verifica se já chegamos no alvo antes de tentar mover
    if robot[0] == target[0] and robot[1] == target[1]:
        print("\nAlvo alcançado! Missão de navegação concluída.")
        break # Quebra o loop e encerra o programa com sucesso
        
    # 3º Passo: Pausa o programa por 0.5 segundos para conseguirmos ver o movimento
    time.sleep(0.5)
    
    # 4º Passo: Toma a decisão de movimento (Calcula o erro e atua)
    
    # Avalia o Eixo X
    if robot[0] < target[0]:
        robot[0] += 1
    elif robot[0] > target[0]:
        robot[0] -= 1
        
    # Avalia o Eixo Y
    if robot[1] < target[1]:
        robot[1] += 1
    elif robot[1] > target[1]:
        robot[1] -= 1

    # O loop recomeça desenhando a nova posição