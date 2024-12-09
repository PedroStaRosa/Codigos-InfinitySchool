class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        
    @property
    def nome(self):
        return self.__nome
    
    def set_nome(self, value):
        self.__nome = value
        
    @property
    def telefone(self):
        return self.__telefone
    
    def set_telefone(self, value):
        self.__telefone = value
        
    @property
    def email(self):
        return self.__email
    
    def set_email(self, value):
        self.__email = value
        