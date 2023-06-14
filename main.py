from Aluno import Aluno
#conexão usando biblioteca pymongo
from pymongo import MongoClient
import datetime
 
# Url para conectar
connection = MongoClient("mongodb://localhost:27017/")
db=connection.escola

nomeAluno = input("Qual o nome do aluno? ")
idadeAluno = int(input("Qual a idade de " + nomeAluno + "?"))
notaAluno = float(input("Qual a média de " + nomeAluno + "?"))

#Inserindo valores
insercao = db.Aluno.insert_many(
    [
    {"nota": notaAluno,
    "nome": nomeAluno,
    "idade": idadeAluno,
    "data_criacao": datetime.datetime.utcnow()
    }
    ]
)

print("Aluno inserido com o ID: {0}".format(insercao.inserted_ids))

#Mostra informações registradas no banco de dados, porém com data_criacao aparecendo
# print("Informações do banco: ")
# for item in db.Aluno.find({'nome': { '$exists': True }}):
#     print( str(item))

#Mostra informações registradas no banco de dados sem data_criacao
#Essa função retorna um None que não saquei como tirar...(só consegui transformar em True ou False, mas não em vazio)
obj = Aluno(notaAluno, nomeAluno, idadeAluno)
print("Informações do banco: ")
print(str(obj.exibir_informacoes()))

    #adicionar pontos extras
pontoExtra = input("O aluno " + nomeAluno + " vai ter direito a ponto extra? (s/n) ")
if pontoExtra == 'n':
        print("")
elif pontoExtra == 's':
        pontoPrat = float(input("Quantos pontos o aluno tirou na prática? (0 a 2) "))
        novaNota = notaAluno + pontoPrat
        db.Aluno.update_one( 
            {"nome": nomeAluno,
            "idade": idadeAluno},
            {"$set": {"nota": novaNota}})
        print("Nota atualizada com sucesso!")
        
        #Mostra informações registradas no banco de dados sem data_criacao
        obj = Aluno(novaNota, nomeAluno, idadeAluno)
        print("Informações do banco: ")
        print(str(obj.exibir_informacoes()))
else:
        print("Digite somente 's' ou 'n'")

#excluir registros
exclusao = input("Deseja excluir algum registro? (s/n) ")
#Mostra informações registradas no banco de dados sem data_criacao
print("Informações do banco: ")
print(str(obj.exibir_informacoes()))

if exclusao == 'n':
        print("Nada foi modificado!")
elif exclusao == 's':
        nomeExcl = input("Digite o nome do aluno que deseja excluir: ")
        db.Aluno.delete_one(
        {"nome": nomeExcl}
        )
        print("Aluno deletado com sucesso!")
else:
        print("Digite somente 's' ou 'n'")

#realizar outro cadastro no sistema
novoCadastro = input("Além de " + nomeAluno + ", deseja cadastrar outro aluno no MongoDB? (s/n) ") 

if novoCadastro == 'n':
        print("")
elif novoCadastro == 's':

        nomeAluno = input("Qual o nome do aluno? ")
        idadeAluno = int(input("Qual a idade de " + nomeAluno + "?"))
        notaAluno = float(input("Qual a média de " + nomeAluno + "?"))

        #Inserindo valores
        insercao = db.Aluno.insert_many(
        [{"nota": notaAluno,
        "nome": nomeAluno,
        "idade": idadeAluno,
        "data_criacao": datetime.datetime.utcnow()
        }])

        print("Aluno inserido com o ID: {0}".format(insercao.inserted_ids))

        #Mostra informações registradas no banco de dados, porém com data_criacao aparecendo
        print("Informações do banco: ")
        for item in db.Aluno.find({'nome': { '$exists': True }}):
            print( str(item))
        
else:
        print("Digite somente 's' ou 'n'")
    
print("Até Logo!")
