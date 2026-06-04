import os
import time

LARGURA = 5
ALTURA = 5

robot = [0, 0]
target = [4, 4]

# Os obstáculos
obstaculos = [
    [1, 1], [2, 1], [3, 1],
    [1, 3], [2, 3]
]

def desenhar_mapa():
    os.system('clear' if os.name == 'posix' else 'cls')
    for y in range(ALTURA):
        linha = ""
        for x in range(LARGURA):
            if [x, y] == robot:
                linha += "R "
            elif [x, y] == target:
                linha += "T "
            elif [x, y] in obstaculos:
                linha += "# " # Desenha o obstáculo
            else:
                linha += ". "
        print(linha)
    print(f"\nRobô: {robot} | Alvo: {target}")

while True:
    desenhar_mapa()
    
    if robot == target:
        print("\nAlvo alcançado! Missão de navegação concluída.")
        break
        
    time.sleep(0.5)
    
    # 1. Planejamento do Eixo X
    proximo_x = robot[0]
    if robot[0] < target[0]:
        proximo_x += 1
    elif robot[0] > target[0]:
        proximo_x -= 1
        
    # Verifica se o passo em X bate na parede. Se não bater, ele anda.
    if [proximo_x, robot[1]] not in obstaculos:
        robot[0] = proximo_x

    # 2. Planejamento do Eixo Y
    proximo_y = robot[1]
    if robot[1] < target[1]:
        proximo_y += 1
    elif robot[1] > target[1]:
        proximo_y -= 1
        
    # Verifica se o passo em Y bate na parede. Se não bater, ele anda.
    if [robot[0], proximo_y] not in obstaculos:
        robot[1] = proximo_y