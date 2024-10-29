from library import *

def menu():
    print ("==== MENU BIBLIOTECA====")
    print(" ( OK ) 1- Adicionar Livro")
    print(" ( OK ) 2- Listar Livros Disponiveis")
    print(" ( OK ) 3- Alugar um livro")
    print(" ( OK ) 4- Devolver um livro")
    print(" ( OK ) 5- Buscar um livro (ID)")
    print(" ( OK ) 6- Buscar Todos livros alugados")
    print(' ( OK ) 7- Buscar TODOS livros alugados por todos os clientes')
    print(' ( OK ) 8- Buscar livro pelo TITULO')
    print(' ( OK ) 9- Buscar livros alugados por usuario(RG)')
    print('99- Sair')

    option = int(input("=>"))

    return option

while True:
   option = menu()

   if option ==   1:

    title = input("Informe o titulo do livro: ")
    author = input("Informe o autor: ")
    n_copies = int(input("Informe o números de copias: "))

    result = add_book(title,author,n_copies)
    print(result)

   elif option == 2:
     
     print(list_books())

   elif option == 3:
      
        user_rg = input("Informe o RG do cliente: ")
        
        id_book = int(input("Informe o id do livro: ")) 
        # vamos supor que todo livro da biblioteca 
        # tenha uma etiqueta com ID marcada na capa.

        result_after_rent_book = rent_book(user_rg,id_book)

        if not result_after_rent_book:
            print("Atenção!!, \nUsúario não cadastrado, realize o cadastro a seguir")
            print("Apos a conclusão do cadastro o aluguel ja será efetuado.")
            user_name = input("Informe o nome do usúario: ")
            add_user(user_name,user_rg)

            result_after_add_user = rent_book(user_rg, id_book)
            print(result_after_add_user)
        else: 
           
            print(result_after_rent_book)

   elif option == 4:
      user_rg = input("Informe o RG do cliente: ")
      book_id = int(input("ID do livro devolvido: "))
      result = return_book_by_user(user_rg, book_id)

      print(result)

   elif option == 5:
      
      book_id = int(input("Informe o ID do livro a ser pesquisado: "))
      book = fetch_book_by_id(book_id)

      if book:
        print("\n")
        print(f"ID: {book[0]["ID"]}")
        print(f"Título: {book[0]["TITLE"]}")
        print(f"Autor: {book[0]["AUTHOR"]}")
        print(f"Copias disponiveis: {book[0]["N_COPIES"]}")
        print("\n")
      else: 
         print(f"\nLivro de ID {book_id} não encontrado... \n")
        
   elif option == 6:
     
     result = return_rent_book()

     print('\n------------------')

     for book_title, n_copies_rent in result.items():
        print(f"O livro {book_title} tem {n_copies_rent} copias alugadas.")
    
     print("------------------\n\n")
        
   elif option == 7:
     print("\n")
     print(list_rent_book())
   
   elif option == 8:
    
    book_title = input("Informe o título do livro: ")
    
    result = fetch_book_by_title(book_title)

    if result:
       for book in result:
          print(f"{book["ID"]} - {book["TITLE"]} - {book["AUTHOR"]} - Copias disponiveis: {book["N_COPIES"]}")
    else:
       print(f"\nLivro {book_title} não encontrado! \n")

   elif option == 9:
    user_rg = input("Informe o RG do cliente: ")
    user = fetch_books_rented_by_user(user_rg)

    if not user:
       print(f"\nCliente de RG {user_rg} não encontrado... \n")
    else:
      print(f"\nNome: {user[0]["NAME"]}")
      print(f"#  Livros alugados:")
      for book in user[0]["BOOKS"]:
        print(f"-----{book["TITLE"]} - {book["AUTHOR"]}")
      print("\n\n")

   elif option == 99:
       break

