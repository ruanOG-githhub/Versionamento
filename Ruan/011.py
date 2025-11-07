from datetime import datetime

def calcular_valor(tempo_total):
    total_minutos = tempo_total.total_seconds() / 60
    total_horas = total_minutos / 60

    if total_horas >= 24:
        diarias = int(total_horas // 24)
        restante = total_horas % 24
        valor = diarias * 60.0

        if restante >= 1:
            valor += int(restante) * 12.0
            frac = (restante - int(restante)) * 60
            valor += int(frac // 15) * 3.0
        return valor

    horas = int(total_horas)
    minutos_restantes = total_minutos - horas * 60
    valor = horas * 12.0

    fracoes = int(minutos_restantes // 15)
    if minutos_restantes % 15 != 0:
        fracoes += 1
    valor += fracoes * 3.0

    if valor > 60.0:
        valor = 60.0

    return valor


def main():
    print("=== SISTEMA DE ESTACIONAMENTO ===")

    placa = input("Digite a placa do carro: ").upper()

    data_entrada = input("Digite a data de entrada (dd/mm/aaaa): ")
    hora_entrada = input("Digite a hora de entrada (hh:mm): ")
    data_hora_entrada = datetime.strptime(f"{data_entrada} {hora_entrada}", "%d/%m/%Y %H:%M")

    data_saida = input("Digite a data de saída (dd/mm/aaaa): ")
    hora_saida = input("Digite a hora de saída (hh:mm): ")
    data_hora_saida = datetime.strptime(f"{data_saida} {hora_saida}", "%d/%m/%Y %H:%M")

    tempo_total = data_hora_saida - data_hora_entrada
    valor_total = calcular_valor(tempo_total)

    print("\n===== TICKET DE ESTACIONAMENTO =====")
    print(f"Placa do veículo : {placa}")
    print(f"Entrada          : {data_hora_entrada.strftime('%d/%m/%Y %H:%M')}")
    print(f"Saída            : {data_hora_saida.strftime('%d/%m/%Y %H:%M')}")
    horas = tempo_total.total_seconds() // 3600
    minutos = (tempo_total.total_seconds() % 3600) // 60
    print(f"Tempo total      : {int(horas)}h {int(minutos)}min")
    print(f"Valor total      : R$ {valor_total:.2f}")
    print("====================================")

if __name__ == "__main__":
    main()
