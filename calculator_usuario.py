from calculator import*

def main():
    
    print("==== Menu ====")       
    print("1.Add")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Go out")
    
    choice = int(input("Escolha uma opção: "))
    
    if choice < 1 or choice > 6:
        print("Invalid input")
        return
    
    return choice

while True:
    
    choice = main()
    
    if choice == None:
        continue
    else choice == 6:
        print("Ate Logo...")
        break
        
    num1 = float(input("Digite um primeiro número:  ")) 
    num2 = float(input("Digite um segundo número:  "))    


    if choice == 1:
        result = add (num1, num2)
        print(result)
        
    elif choice == 2:
        result = subtract (num1, num2)
        print(result)
        
    elif choice == 3:
        result = multiplication (num1, num2)
        print(result)
        
    elif choice == 4:
        result = division(num1, num2)
        print(result)
        
    elif choice == 5:
        result = exponentiation(num1, num2)
        print(result)
        
        





