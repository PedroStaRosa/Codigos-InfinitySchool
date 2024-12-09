def menu():
    print(f"--- BANCO FELIZ ----")
    print("1. Abrir uma conta.")
    print("2. Depositar.")
    print("3. Sacar.")
    print("4. Resumo das contas.")
    print("88. Avançar um mês....")
    print("99 - Sair da conta")

option = 0
while option != 99:
    menu()
    option = int(input("-> "))
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 88:
        pass
    elif option == 99:
        pass
    else:
        print("Opção invalida...")