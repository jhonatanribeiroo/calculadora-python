def calculadora():
    print("=== MINHA CALCULADORA ===")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print("\nEscolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair") 
    print("3 - Multiplicar")
    print("4 - Dividir")
    
    opcao = input("Digite a opção: ")
    
    if opcao == "1":
        resultado = num1 + num2
    elif opcao == "2":
        resultado = num1 - num2
    elif opcao == "3":
        resultado = num1 * num2
    elif opcao == "4":
        resultado = num1 / num2
    else:
        print("Opção inválida")
        return
    
    print(f"\nResultado: {resultado}")

calculadora()
