# analisador.py - v2.2.0
# "O Valor de uma Transição"
# Copyright (c) 2026 servodecristorj-ai

def formatar_brl(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def calcular_diferenca(a: float, b: float) -> float:
    menor = min(abs(a), abs(b))
    return (abs(a - b) / menor) * 100 if menor != 0 else 0.0

def main():
    print("=== ANALISADOR DE INJUSTIÇAS v2.2.0 ===")
    print("Título: O Valor de uma Transição (Auditoria RJ)")
    print("-" * 45)
    print("1. Deputado Federal (Cota Máxima)")
    print("2. Transição Governador RJ (Auditoria Comparativa)")
    print("3. Entrada Manual")
    
    opcao = input("\nEscolha uma opção (1-3): ")
    salario_minimo = 1621.00 # Base 2026

    if opcao == "1":
        valor_a = 262037.79 
        cargo = "Deputado Federal (Custo Mensal Total)"
        
    elif opcao == "2":
        # METODOLOGIA: O VALOR DE UMA TRANSIÇÃO (RJ)
        subsidio_acumulado = 75000.00 
        custo_comissionados_orig = 4000000.00 
        staff_especial_tjrj = 1175000.00 
        viagens_logistica = 27142.85 
        prev_licitacoes_futuras = 500000.00 
        
        valor_a = subsidio_acumulado + custo_comissionados_orig + staff_especial_tjrj + viagens_logistica + prev_licitacoes_futuras
        cargo = "Governador RJ - O Valor de uma Transição"
        
        print("\n--- DETALHAMENTO DA AUDITORIA (GOVERNADOR) ---")
        print(f"Salário Acumulado (Judiciário+Gov): {formatar_brl(subsidio_acumulado)}")
        print(f"Custo Médio Cargos Extintos/Subst: {formatar_brl(custo_comissionados_orig)}")
        print(f"Gratificações 47 Técnicos TJRJ:     {formatar_brl(staff_especial_tjrj)}")
        print(f"Viagens e Logística (Mensal):      {formatar_brl(viagens_logistica)}")
        print(f"Previsão de Licitações/Apoio:      {formatar_brl(prev_licitacoes_futuras)}")
        
    else:
        try:
            valor_a = float(input("Digite o Valor A: ").replace(".", "").replace(",", "."))
            cargo = "Manual"
        except: return

    perc = calcular_diferenca(valor_a, salario_minimo)

    print("-" * 45)
    print(f"ANÁLISE: {cargo}")
    print(f"VALOR A (Custo Estrutural/Mês): {formatar_brl(valor_a)}")
    print(f"VALOR B (Salário Mínimo 2026):  {formatar_brl(salario_minimo)}")
    print(f"DISPARIDADE: {perc:,.2f}%")

    if perc > 50:
        print("\n>>> STATUS: INJUSTIÇA EXTREMA DETECTADA!")
        print(f"Este custo equivale a {valor_a/salario_minimo:.1f} famílias vivendo com um salário mínimo.")

if __name__ == "__main__":
    main()
