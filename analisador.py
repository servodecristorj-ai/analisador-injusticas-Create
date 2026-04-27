# analisador.py - v1.0.0
# Copyright (c) 2026 servodecristorj-ai
# Licença: BSD-3-Cláusulas (ver arquivo LICENÇA)
#
# Analisador de Injustiças
# Compara dois valores e sinaliza quando a diferença percentual > 50%
# Inclui constante Valor A (metodologia do README) para referência futura.

SUBSIDIO_MENSAL = 46366.19  # R$ - base para cálculo do Valor A (mandato no teto)

def calcular_diferenca_percentual(a: float, b: float) -> float:
    """Retorna diferença percentual em relação ao menor valor absoluto.
    Evita divisão por zero."""
    if a == 0 and b == 0:
        return 0.0
    menor = min(abs(a), abs(b))
    if menor == 0:
        return 100.0
    diferenca = abs(a - b)
    return (diferenca / menor) * 100

def valor_a_mandato(meses: int = 48) -> float:
    """Exemplo da metodologia do README: custo total do subsídio no teto."""
    return SUBSIDIO_MENSAL * meses

def main():
    print("=== Analisador de Injustiças v1.0.0 ===")
    try:
        a = float(input("Digite o valor A: ").replace(",", ".").strip())
        b = float(input("Digite o valor B: ").replace(",", ".").strip())
    except ValueError:
        print("Erro: digite apenas números.")
        return

    perc = calcular_diferenca_percentual(a, b)

    print(f"
Valor A: {a:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Valor B: {b:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Diferença percentual: {perc:.1f}%")

    if perc > 50:
        print(">>> POSSÍVEL INJUSTIÇA detectada!")
    else:
        print("Diferença dentro do aceitável.")

    # referência opcional
    print(f"
[Ref] Valor A (48 meses no teto): R$ {valor_a_mandato():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

if __name__ == "__main__":
    main()
