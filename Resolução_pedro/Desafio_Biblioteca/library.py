from datetime import date
import random

db_rent_books = [
    {"NAME": "Alice", "RG": "123456789", "BOOKS": [{"ID": 3, "TITLE": "Book Three","AUTHOR": "Fulano 03"}]},
    {"NAME": "Bob", "RG": "987654321", "BOOKS": [{"ID": 1, "TITLE": "Book One" ,"AUTHOR": "Fulano 01"},
    {"ID": 2, "TITLE": "Book Two","AUTHOR": "Fulano 02"},{"ID": 3, "TITLE": "Book Three","AUTHOR": "Fulano 03"}
    ]},
    {"NAME": "Carlos", "RG": "555555555", "BOOKS": []},
    {"NAME": "Diana", "RG": "111222333", "BOOKS": [{"ID": 1, "TITLE": "Book One" ,"AUTHOR": "Fulano 01"},{"ID": 3, "TITLE": "Book Three","AUTHOR": "Fulano 03"}]},
    {"NAME": "Eduardo", "RG": "444555666", "BOOKS": [{"ID": 1, "TITLE": "Book One" ,"AUTHOR": "Fulano 01"},
    {"ID": 2, "TITLE": "Book Two","AUTHOR": "Fulano 02"},
    {"ID": 3, "TITLE": "Book Three","AUTHOR": "Fulano 03"}]}
]

db_books = [
    {"ID": 1, "TITLE": "Book One" ,"AUTHOR": "Fulano 01", "N_COPIES": 30},
    {"ID": 2, "TITLE": "Book Two","AUTHOR": "Fulano 02", "N_COPIES": 2},
    {"ID": 3, "TITLE": "Book Three","AUTHOR": "Fulano 03", "N_COPIES": 10},
    {"ID": 4, "TITLE": "Book Four","AUTHOR": "Fulano 03", "N_COPIES": 13},
    {"ID": 5, "TITLE": "Book ABC","AUTHOR": "Fulano 03", "N_COPIES": 45},
    {"ID": 6, "TITLE": "Book ZZZ","AUTHOR": "Fulano 03", "N_COPIES": 87},
    {"ID": 7, "TITLE": "Book XXXX","AUTHOR": "Fulano 03", "N_COPIES": 101}
]

def add_book(title,author,n_copies):
    new_book = {
        "ID": len(db_books) * random.randint(2,100) ,
        'TITLE' : title,
        'AUTHOR' : author,
        'N_COPIES' : n_copies
    }

    db_books.append(new_book)

    return f"Livro {title} adicionado com sucesso!!"

def add_user(name,rg):
    db_rent_books. append(
        {"NAME": name, "RG": rg, "BOOKS": []}
    )

def list_books():

    ordenada = sorted(db_books, key=lambda p: p['N_COPIES'], reverse=True)

    result = ""
    for book in ordenada:
        # Cria um super String formatada para retorno.
        result += f'{book["ID"]} - {book["TITLE"]} - {book["AUTHOR"]} - {book["N_COPIES"]} copias\n'
    
    return result

def rent_book(user_rg, id_book: int):

    for user in db_rent_books:
        if user.get("RG") == user_rg:
            
            for book in db_books:
                
                if int(book.get("ID")) == id_book: # Buscar o livro pelo ID.
                    if book["N_COPIES"] >= 1: # Verifica se o livro tem copia disponivel para alugar.
                        
                        new_book = {
                            "ID": book["ID"] ,
                            'TITLE' : book["TITLE"],
                            'AUTHOR' : book["AUTHOR"]
                         }
                        
                        user["BOOKS"].append(new_book) # Adicionar o livro à lista BOOKS do usuário.
                        book["N_COPIES"] = book["N_COPIES"] - 1 # Retira uma copia disponivel.
                        
                        return f'Livro {book["TITLE"]} alugado ao usuário {user["NAME"]}'
                    
                    else: 
                        return f"Livro esgotado para aluguel."
                    
            return f"Livro com ID {id_book} não encontrado."
            
    
    return # Retorna None caso nao tenha o usuario cadastrado no sistema e ira pedir para cadastrar.

def list_rent_book():

    result = ""
    for user in db_rent_books:
        result += f"{user["NAME"]} - {user["RG"]} - Livros: "
        if len(user["BOOKS"]) >= 1:
            for book in user["BOOKS"]:
                result += f"\n ##  {book["TITLE"]} - {book["AUTHOR"]}"
        else:
            result += f"\n SEM LIVROS ALUGADOS"
        result += f"\n-------------------\n"

    return result

def return_rent_book():

    book_count = {}
    for person in db_rent_books:
        for book in person["BOOKS"]:
            book_title = book["TITLE"]
            if book_title in book_count:
                book_count[book_title] += 1
            else:
                 book_count[book_title] = 1
    
    return book_count

def fetch_book_by_id(book_id):

    book = list(filter(lambda x: int(x["ID"]) == book_id, db_books))
    
    return book
    # for book in db_books:
    #     if int(book["ID"]) == book_id:
    #         return book
        
    # return None

def return_book_by_user(rg_user, book_id):
    user = fetch_books_rented_by_user(rg_user)

    if user:
        for book in user["BOOKS"]:
            if int(book["ID"]) == book_id:
                user["BOOKS"].remove(book)
                for ref_book in db_books:
                    if ref_book["ID"] == book_id:
                        ref_book["N_COPIES"] += 1
                return f"Sucesso"
    else:
        return None

def fetch_books_rented_by_user(rg_user):

    result = list(filter(lambda x: x["RG"] == rg_user, db_rent_books))
   
    # for user in db_rent_books:
    #     if user["RG"] == rg_user:
    #         return user
    
    return result

def fetch_book_by_title(book_title):
    result = list(filter(lambda x: x["TITLE"].lower() == book_title.lower(), db_books))

    if len(result) == 0:
        return 
    else:
        return result