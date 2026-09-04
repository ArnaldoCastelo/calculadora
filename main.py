
print("Minha primeira calculadora em Python")
print("=== calculadora ===")

numero1 = float(input("Digite o primeiro numero: "))
operacao = input("Digite a operação (+, -, * ou /): ")
numero2 = float(input("Digite o segundo numero: "))

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Não é possível dividir por zero."

else:
    resultado = "Operação inválida."

print("Resultado:", resultado)
