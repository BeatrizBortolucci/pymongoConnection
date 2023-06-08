from Pessoa import Pessoa

class Aluno(Pessoa):
   def __init__(self, nota, nome, idade):
       super().__init__(nome, idade)
       self.nota = nota

   def getNota(self):
       return self.nota

   def setNota(self, nota):
       self.nota = nota

   def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nota: {self.nota}")