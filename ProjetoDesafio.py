db_tasks = [
        {
        "nome": "Estudar Python",
        "descricao": "Estudar conceitos básicos e avançados de Python",
        "prioridade": "Alta",
        "categoria": "Estudo",
        "status": False
    },
    {
        "nome": "Comprar supermercado",
        "descricao": "Comprar itens essenciais como arroz, feijão, leite, etc.",
        "prioridade": "Média",
        "categoria": "Compras",
        "status": False
    },
    {
        "nome": "Reunião de trabalho",
        "descricao": "Reunião com a equipe para discutir o projeto",
        "prioridade": "Alta",
        "categoria": "Trabalho",
        "status": False
    },
    {
        "nome": "Fazer exercício",
        "descricao": "Caminhar 30 minutos no parque",
        "prioridade": "Média",
        "categoria": "Saúde",
        "status": False
    },
    {
        "nome": "Ler livro",
        "descricao": "Ler 50 páginas do livro 'Sapiens'",
        "prioridade": "Baixa",
        "categoria": "Lazer",
        "status": False
    },
    {
        "nome": "Limpar a casa",
        "descricao": "Limpar a cozinha, sala e banheiros",
        "prioridade": "Alta",
        "categoria": "Tarefas domésticas",
        "status": False
    },
    {
        "nome": "Assistir série",
        "descricao": "Assistir um episódio de 'Stranger Things'",
        "prioridade": "Baixa",
        "categoria": "Lazer",
        "status": False
    },
    {
        "nome": "Pagar contas",
        "descricao": "Pagar contas de luz, água e internet",
        "prioridade": "Alta",
        "categoria": "Financeiro",
        "status": False
    },
    {
        "nome": "Marcar consulta médica",
        "descricao": "Agendar consulta com o clínico geral",
        "prioridade": "Média",
        "categoria": "Saúde",
        "status": False
    },
    {
        "nome": "Escrever artigo",
        "descricao": "Escrever e revisar o artigo para o blog",
        "prioridade": "Alta",
        "categoria": "Trabalho",
        "status": False
    }
]

def add_task(name,description,priority,category):
    task ={
        "nome": name,
        "descricao": description,
        "prioridade" : priority,
        "categoria": category,
        "status" : False
    }
    
    db_tasks.append(task)


def list_tasks():
    print("---- TAREFAS ----")
    if len(db_tasks) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        index = 1
        for task in db_tasks:
            status = "Concluida" if task["status"] else "Pendente"
            print(f"{index} - {task["nome"]} - {task["descricao"]} - {task["prioridade"]} - {task["categoria"]} - Status: {status}")
            index += 1

def mark_task_as_completed(index):
   
    
    db_tasks[index]["status"] = True
    
    return f"{db_tasks[index]["nome"]} foi concluida com sucesso!"
    
def list_per_priority(priority):
    
    result = list(filter(lambda x: x["prioridade"] == priority, db_tasks))

    index = 1
    for task in result:
        status = "Concluida" if task["status"] else "Pendente"
        print(f"{index} - {task["nome"]} - {task["descricao"]} - {task["prioridade"]} - {task["categoria"]} - Status: {status}")
        index += 1

def list_por_category(category):
    result = list(filter(lambda x: x["categoria"] == category, db_tasks))

    index = 1
    for task in result:
        status = "Concluida" if task["status"] else "Pendente"
        print(f"{index} - {task["nome"]} - {task["descricao"]} - {task["prioridade"]} - {task["categoria"]} - Status: {status}")
        index += 1
    
    
def delete_task(index):
  
    task = db_tasks[index]
    db_tasks.pop(index)

    return f"Tarefa {task["nome"]} deletada com sucesso!"

while True:
    print("\n----- MENU -----")
    print("1- Adicionar tarefa")
    print("2- Listar tarefas")
    print("3- Marcar como concluida")
    print("4- Listar por prioridade")
    print("5- Listar por categoria")
    print("6- Deletar tarefa")
    print("7- Sair")
    
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
        
        name = input("Nome da tarefa: ")
        description = input("Descrição: ")
        priority = input("Prioridade (Alta,Media,Baixa): ")
        category = input("Categoria: ")
        
        add_task(name,description,priority,category)
        print(f"A tarefa {name} foi criada com sucesso.")
        
    elif option == 2:
        list_tasks()
        
    elif option == 3:
        list_tasks()
        index = int(input("Qual tarefa deseja marca como concluida: ")) - 1
        result = mark_task_as_completed(index)
        print(result)
        
    elif option == 4:
        priority = input("Qual a prioridade? (Alta,Media,Baixa) ")
        list_per_priority(priority)
        
    elif option == 5:
        category = input("Qual a categoria? ")
        list_por_category(category)
    elif option == 6:
        list_tasks()
        index = int(input("Qual tarefa deseja marca como concluida: ")) - 1
        result =  delete_task(index)
        print(result)
       
    elif option == 7:
        break
    else:
        print("Opção invalida!!")
        