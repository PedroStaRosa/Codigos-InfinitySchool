products_list = [
    { 'NAME': "Feijão", 'PRICE': 8.99, 'STOCK': 2},
    { 'NAME': "Arroz", 'PRICE': 1.99, 'STOCK': 100}
    ]

def add_product(name,price,stock):
    product = { 'NAME': name, 'PRICE': price, 'STOCK': stock }
    products_list.append(product)

    return f"Produto {name} cadastrado. "
# -------------------------------------------------------------------------
def remove_product(name):
    for p in products_list:
        if p["NAME"].lower() == name.lower():
            index = products_list.index(p)
            products_list.pop(index)
            return f"Produto {name} foi deletado."

    return f"Produto {name} não encontrado.\n"
# -------------------------------------------------------------------------
def update_product(name,price,stock):

    for product in products_list:
        if product["NAME"] == name:
            product["PRICE"] = price
            product["STOCK"] = stock
            return f"Produto {name} foi atualizado."
        
    return f"Produto {name} não encontrado!\n"
# -------------------------------------------------------------------------
def list_products():
    result = ""
    for p in products_list:
        result += f"{p["NAME"]} - R$ {p["PRICE"]}, Estoque: {p["STOCK"]} und(s)\n"
    
    return result