from datetime import datetime, timedelta

def calcular_valor(tempo):
    minutos = tempo.total_seconds() / 60

   
    if minutos > 24 * 60:
        diarias = int(minutos // (24 * 60))
        resto_minutos = minutos % (24 * 60)
        valor = diarias * 60  
        minutos = resto_minutos
    else:
        valor = 0

    
    horas = int(minutos // 60)
    minutos_restantes = minutos % 60

    valor += horas * 12 

    
    if minutos_restantes > 0:
        fracoes = int((minutos_restantes - 1) // 15 + 1)
        valor += fracoes * 3

    return valor


def gerar_ticket(placa, entrada, saida, valor):
    tempo = saida - entrada
    print("\n========== TICKET DE ESTACIONAMENTO ==========")
    print(f"Placa do veículo: {placa}")
    print(f"Data de entrada: {entrada.strftime('%d/%m/%Y %H:%M')}")
    print(f"Data de saída:   {saida.strftime('%d/%m/%Y %H:%M')}")
