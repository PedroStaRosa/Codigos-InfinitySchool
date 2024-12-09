class Quarto:
    def __init__(self, numero_quarto,tipo_quarto,preco_diaria):
        self.__numero_quarto = numero_quarto
        self.__tipo_quarto = tipo_quarto
        self.__preco_diaria = preco_diaria
        self.__avaliable = True
        
    @property
    def numero_quarto(self):
        return self.__numero_quarto
    
    @property
    def tipo_quarto(self):
        return self.__tipo_quarto
    
    def set_tipo_quarto(self, value):
        ## VALIDADE TIPO DE QUARTOS POSSIVEIS
        if value:
            self.__tipo_quarto = value
    
    @property
    def preco_diaria(self):
        return self.__preco_diaria
    
    def set_preco_diaria(self, value):
        if value > 0:
            self.__preco_diaria = value
    
    @property
    def avaliable(self):
        return self.__avaliable
    
    def set_avaliable(self):
        # VAI INVERTER O BOLEANO NO CHECKIN E CHECKOUT
        self.__avaliable = not self.__avaliable
        
        