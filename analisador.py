# analisador.py - v1
# Compara dois valores e aponta possível injustiça se diferença > 50%

def calcular_diferenca_percentual(a, b):
    if a == 0 and b == 0:
        return 0
    menor = min(abs(a), abs(b))
    if menor == 0:
        return 100.0  # evita divisão por zero
    diferenca = abs(a - b)
    return (diferenca / menor) * 100

def main():
    print("=== Analisador de Injustiças ===")
    try:
        a = float(input("Digite o valor A: ").replace(",", "."))
        b = float(input("Digite o valor B: ").replace(",", "."))
    except ValueError:
        print("Erro: digite apenas números.")
        return

    perc = calcular_diferenca_percentual(a, b)
    
    print(f"\nValor A: {a}")
    print(f"Valor B: {b}")
    print(f"Diferença percentual: {perc:.1f}%")

    if perc > 50:
        print(">>> POSSÍVEL INJUSTIÇA detectada!")
    else:
        print("Diferença dentro do aceitável.")

if __name__ == "__main__":
    main()