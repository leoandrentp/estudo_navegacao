import time

# 1. Definindo o estado inicial
estado_atual = "IDLE"

# Variáveis simulando os sensores e comandos do drone (Gatilhos)
comando_decolar = True
altitude_atual = 0
alvo_encontrado = False
distancia_alvo = 50
no_solo = False

print("--- SISTEMA DE CONTROLE INICIADO ---")

# 2. O Loop Principal de Controle
# O código vai rodar continuamente até a missão terminar
while estado_atual != "MISSION_COMPLETE":
    
    # --------------------------------------------------------
    # MÁQUINA DE ESTADOS
    # --------------------------------------------------------
    if estado_atual == "IDLE":
        print("[IDLE] Drone desarmado no solo. Aguardando comando...")
        # Checa o gatilho para sair do IDLE
        if comando_decolar:
            print(">> Gatilho ativado: Comando de decolagem recebido!")
            estado_atual = "TAKEOFF"
            
    elif estado_atual == "TAKEOFF":
        print(f"[TAKEOFF] Subindo... Altitude atual: {altitude_atual}m")
        altitude_atual += 5  # Simulando o drone subindo
        
        # Checa o gatilho para sair do TAKEOFF
        if altitude_atual >= 10: # Altitude de cruzeiro atingida
            print(">> Gatilho ativado: Altitude de cruzeiro atingida!")
            estado_atual = "SEARCH_TARGET"
            
    elif estado_atual == "SEARCH_TARGET":
        print("[SEARCH_TARGET] Procurando o alvo com a câmera...")
        # Simulando a detecção após algum tempo
        alvo_encontrado = True 
        
        # Checa o gatilho para sair do SEARCH_TARGET
        if alvo_encontrado:
            print(">> Gatilho ativado: Alvo detectado pelas câmeras!")
            estado_atual = "GO_TO_TARGET"
            
    elif estado_atual == "GO_TO_TARGET":
        print(f"[GO_TO_TARGET] Navegando até o alvo. Distância: {distancia_alvo}m")
        distancia_alvo -= 25 # Simulando o drone se aproximando
        
        # Checa o gatilho para sair do GO_TO_TARGET
        if distancia_alvo <= 0:
            print(">> Gatilho ativado: Drone chegou na coordenada exata do alvo!")
            estado_atual = "LAND"
            
    elif estado_atual == "LAND":
        print(f"[LAND] Pousando... Altitude atual: {altitude_atual}m")
        altitude_atual -= 5 # Simulando o drone descendo
        
        # Checa o gatilho para sair do LAND
        if altitude_atual <= 0:
            no_solo = True
            
        if no_solo:
            print(">> Gatilho ativado: Drone detectou toque no solo e desarmou motores!")
            estado_atual = "MISSION_COMPLETE"

    # Pausa de 1 segundo para conseguirmos ler o que está acontecendo na tela
    time.sleep(1)

# Fora do loop principal
print("\n[MISSION_COMPLETE] Missão autônoma finalizada com sucesso!")
print("--- SISTEMA DE CONTROLE ENCERRADO ---")