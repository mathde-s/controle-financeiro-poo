class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data
    
    def resumo():
        return f"{self.descricao} | +{self.valor} | {self.categoria} | {self.data}"

