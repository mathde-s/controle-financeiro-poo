class Carteira:
    def __ini__(self):
        self.lista_de_transacoes = []

    def adicionar(self, transacao):
        self.lista_de_transacao.append(transacao)

    def exibir_transacoes(self):
        for transacao in self.lista_de_transacoes:
             print(transacao.resumo())    

    def saldo(self):
        return sum(transacao.valor for transacao in self.lista_de_transacoes)

    def filtrar_por_categoria(categoria, self):
        for i in self.lista_de_transacoes:
            if i.categoria == categoria:
                print(lista_de_transacoes[i])

    def gastos_totais(self):
        return sum(transacao.valor for transacao in self.transacoes if transacao.valor < 0)

    def renda_total(self):
        return sum(transacao.valor for transacao in self.transacoes if transacao.valor > 0)
    