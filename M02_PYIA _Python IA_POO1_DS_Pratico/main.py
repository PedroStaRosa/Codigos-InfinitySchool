from classes.Hotel import Hotel
from classes.Employee import Employee 
from classes.Room import Room 

def menu():
    print("\n")
    print("1. Adicionar Funcionario.")
    print("2. Quadro de funcionarios.")
    print("3. Quartos diponiveis.")
    print("4. Quartos Alugados")
    print("5. Status geral dos quartos")
    print("6. Realizar uma reserva")
    print("7. Check-out")
    print("99. Fechar Hotel")


def main():
    def add_new_employee(name, function, salary):
        hotel.add_employee(Employee(name,function,salary))
    
    def create_booking(client, room, checkIn, checkOut):
        hotel.add_booking(client, room, checkIn, checkOut)
    
    hotel = Hotel("Hotel Fazendinha Feliz")

    # Adicionando os quartos automaticamente
    hotel.rooms_seed()

    while True:
        menu()
        option = input("->")

        if option == '1':
            emp_name = input("Informe o nome do funcionario: ")
            emp_function = input("Informe a função do funcionario:")
            emp_salary = float(input("Informe o salário do funcionario:"))

            add_new_employee(emp_name,emp_function,emp_salary)

        elif option == "2":
            hotel.list_employee()

        elif option == "3":
            hotel.list_all_available_rooms()

        elif option == "4":
            hotel.list_booking()

        elif option == "5":
            hotel.list_all_rooms()

        elif option == "6":
            client_name = input("Nome do locador: ")
            hotel.list_all_available_rooms()
            room_select = int(input("Informe o numero do quarto: "))
            check_in = input("Data de entrada ( DD/MM/AAAA ): ")
            check_out = input("Data de saida ( DD/MM/AAAA ): ")

            create_booking(client_name,room_select,check_in,check_out)

        elif option == "7":
            room = int(input("Informe o quarto para finalizar a reserva: "))
            hotel.remove_booking(room)

        elif option == "99":
            break
        else:
            print("Opção invalida!!!!")

if __name__ == "__main__":
    main()
