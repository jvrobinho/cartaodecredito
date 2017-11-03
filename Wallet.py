from .Cartao import Cartao


class Wallet:
    '''Classe de Wallet da API
        Cada wallet tem um usuário de nome único e uma lista de cartões registrados nessa wallet
    '''
    def __init__(self,id,name,limiteReal):
        self.userid = user #ID do dono da Wallet
        self.userName = name #Nome do dono da Wallet
        self.cartoes = [] #Lista de cartões que o usuário registrou na sua Wallet
        lim = 0
        for cartao in self.cartoes:
           lim+= cartao.limite
        self.limiteMax = lim
        self.limiteReal = lim
        self.gasto = 0


    def buscaUser(self,nome):
        pass

    #Define o limite da Wallet de um usuário
    def setLimite(self,novoLimite):
      if(self.limiteMax>novoLimite):
        self.limiteReal = novoLimite
      else:
        self.limiteReal = self.limiteMax

    #TODO all below
    def buscaCartao(self,numero):
        pass
    def insereCartao(self,cartao: Cartao):
        pass
    def removeCartao(self,cartao):
        pass
    def realizaCompra(self,cartao):
        pass
    def ordenaCartoes(self,lista):
        pass