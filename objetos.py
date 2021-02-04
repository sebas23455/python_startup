
import turtle

class Jogador:
    def __init__(self,nome,forma):
        self.nome = nome
        self.forma = forma

# Comecamos o programa aqui

formas = turtle.getshapes()
print("Qual e o teu nome")
nome = input()
print("Qual a forma que queres")
print(formas)
forma_escolhida = input()

if forma_escolhida not in formas:
    print("forma nao reconhecida, estas tramado") 
    exit(404)
    
j1 = Jogador (nome, forma_escolhida)
print(j1.forma)
