import Cartao
from pymongo import MongoClient, ASCENDING

from flask_restful import Api, Resource, abort
from flask import Flask, url_for
from flask import request
from flask import json, jsonify
from bson import  json_util

app = Flask(__name__)

walletClient = MongoClient('localhost',27017) #Abre conexão com banco de dados Mongo na porta 27017
DocsDB = walletClient.database
db = DocsDB.wallets

class Wallet(Resource):
    '''Classe de Wallet da API
        Cada wallet tem um usuário de nome único e uma lista de cartões registrados nessa wallet
    '''
    def __init__(self,name):
        self.userName = name #Nome do dono da Wallet
        self.cartoes = [] #Lista de cartões que o usuário registrou na sua Wallet
        self.limiteMax = 0
        self.limiteReal = 0
        self.gasto = 0

    #Define o limite da Wallet de um usuário
    def setLimite(self,novoLimite):
      if(self.limiteMax>novoLimite):
        self.limiteReal = novoLimite
      else:
        self.limiteReal = self.limiteMax


    #Cria um novo usuario e sua wallet, inicialmente sem cartoes.
    #Ausente de nome de usuário duplicados
    @app.route("/<userName>",methods = ["POST"])
    def insereWallet(userName):
        wlt = Wallet(userName).__dict__ #converte a Wallet para
        lookup = db.find_one({"userName": userName})
        if not(lookup):
            cleanwlt = json.loads(json_util.dumps(wlt)) #remove o ObjectId da query que será exibida, porque é um hex.
            db.insert_one(wlt)#insere da coleção
            return jsonify(cleanwlt)#retorna a Wallet em forma de JSON
        else:
            abort(409,description="Esse nome de usuário já existe! Por Favor escolha outro!")

    @app.route("/<user>",methods = ["GET"])
    def getWallet(user):
        wlt = db.find_one({"userName": user})
        cleanwlt = json.loads(json_util.dumps(wlt))
        cleanwlt.pop("_id") #tira o ObjectID da query
        return jsonify(cleanwlt) #retorna a query em formato JSON

    @app.route("/<user>", methods = ["GET"])
    def buscaUser(self, nome):
        lookup = db.find_one({"userName": nome})


    # GET /wallet/{user}/cards
    def buscaCartoes(self, id, collection):
        wallet = collection.find_one({"userID": id})
        if wallet:
            listaDeCartoes = wallet.get("cartoes")
        return listaDeCartoes


    # PUT wallet/{user}/cards/
    #insere cartao e recalcula limite total
    def insereCartao(self, id, collection, cartao):
        wallet = collection.find_one({"userID": id})
        cartoes = self.buscaCartoes(id,collection)
        if cartoes:
            cartoes.append(cartao)
            wallet.update({"userID": id},{"cartoes": cartoes})

    # DELETE wallet/{user}/cards
    def removeCartao(self, id, collection, cartao):
        wallet = collection.find_one({"userID": id})
        if wallet:
            cartoes = self.buscaCartoes(id, collection)
            for cartao in cartoes:
                cartoes.remove(cartao)
            wallet.update({"userID": id}, {"cartoes":cartoes})


    # POST wallet/{user}/pay
    def realizaCompra(self, id, collection, cartao):
        pass


    def ordenaCartoes(self, id, collection, lista):
        pass


api = Api(app)
api.add_resource(Wallet, "/",endpoint="userName")
if __name__ == '__main__':
    app.run(debug=True)