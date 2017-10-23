class Cartao:
    'Classe de cartões de cŕedito'
    def __init__(self,numero,vencimento,validade,titular,cvv,limite):
        ''' Metodo construtor de cartões de crédito.
            Cada instância dessa classe terá os atributos abaixo:

        '''

        self.numero = numero #Número do Cartão de 16 dígitos
        self.vencimento = vencimento #Data de Vencimento da fatura do cartão(DD)
        self.validade = validade #Data de Validade do cartão de crédito (MM/AA)
        self.titular = titular #Nome do titular do cartão de crédito
        self.cvv = cvv #Código de verificação do cartão
        self.limite = limite #Limite do cartão de crédito
        self.gasto = 0 #Valor gasto no total pelo usuário

    #Os getters abaixo retornam cada  atributo da instância
    def getNumero(self,numero):
        return self.numero

    def getVencimento(self, vencimento):
        return self.vencimento

    def getValidade(self, validade):
        return self.validade

    def getTitular(self,titular):
        return self.titular

    def getCVV(self, cvv):
        return self.cvv

    def getLimite(self, limite):
        return self.limite

    '''Função que verifica se o valor que o cliente deseja utilizar é maior que o
        valor disponível(limite do cartão - valor gasto nesse cartao).
        Se for, ele soma o crédito liberado ao valor gasto no cartão e retorna True
        Se não, ele simplesmente retorna False
    '''
    def liberaCredito(self,valor):
        if (self.limite - self.gasto > valor):
            self.gasto += valor
            return True
        else:
            return False
