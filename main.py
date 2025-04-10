def calculadora ():
    operacao = (input("Digite qual operação (Exemplo: - , + , * , / ) : "))
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    if operacao == "+":
        print(valor1, "+", valor2, "=", valor1 + valor2)
    
    elif operacao == "-":
        print(valor1, "-", valor2, "=", valor1 - valor2)

    elif operacao == "*":
        print(valor1, "x", valor2, "=", valor1 * valor2)

    elif operacao == "/":
        print(valor1, "/", valor2, "=", valor1 / valor2)

    else:
        print("Operação inválida!")

calculadora()