from func import div,mult,soma,sub
from manip_string import count_works,invert_string,palindrome

while True:

    print("\n----- MENU -----")
    print("1- Soma")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Sair")
    
    option = int(input("Escolha uma opção: "))
    
    if option <1 or option > 5:
        print("opção invalida...")
        continue
    
    num1 = float(input("informe o primeiro número 1: "))
    num2 = float(input("informe o primeiro número 2: "))
    
    if option == 1:
        result = soma(num1,num2)
        print(f"Resultado = {result}")
        
    elif option == 2:
        
        result = sub(num1,num2)
        print(f"Resultado = {result}")
        
    elif option == 3:

        result = mult(num1,num2)
        print(f"Resultado = {result}")
        
    elif option == 4:
        
        result = div(num1,num2)
        print(f"Resultado = {result}")
        
    elif option == 5:
        break
    else:
        print("Opção invalida!!")

# ATIVIDADE 02
while True:
    print("\n----- MENU -----")
    print("1- Inverter Texto")
    print("2- Contar numero de palavras do texto")
    print("3- É um palíndromo??")
    print("4- Sair")
    
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
        text = input("informe o texto: ")
        result = invert_string(text)
        print(result)
        
    elif option == 2:
        
        text = input("informe o texto: ")
  
        result = count_works(text)
        print(f"O texto contem {result} palavras")
        
    elif option == 3:

        text = input("informe o texto: ")
  
        result = palindrome(text)
        print(f"O texto {result}")
        
    elif option == 4:
        break

    else:
        print("Opção invalida!!")    
