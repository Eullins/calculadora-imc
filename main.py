import csv
import os
    
if os.path.exists("LucasDiasLins.txt"):
  os.remove("LucasDiasLins.txt")

class PessoaIMC:
    def __init__(self, nome, sobrenome, peso, altura):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.peso = peso 
        self.altura = altura 
        
    def calcularIMC(self):
        peso = self.peso.replace(",", ".")
        altura = self.altura.replace(",", ".")
        if (peso and altura):
            return round(float(peso) / float(altura)**2, 2)
        else:
            return "DADOS INVÁLIDOS"
        
    def formatarNome(self):
        nomeCompleto = self.nome.strip() + " " + self.sobrenome.strip()
        return nomeCompleto.upper()
    
    def resultado(self):
        return self.formatarNome() + " " + str(self.calcularIMC())

arquivo = open("LucasDiasLins.txt", "a")

with open('dataset.csv', newline='') as csvfile:
  Conteudo = csv.reader(csvfile, delimiter=';')
  next(Conteudo)
  listaPessoasIMC = list()
  for linha in Conteudo:
    pessoa = PessoaIMC(linha[0], linha[1], linha[2], linha[3])
    listaPessoasIMC.append(pessoa.resultado() + "\n")

arquivo.writelines(listaPessoasIMC)