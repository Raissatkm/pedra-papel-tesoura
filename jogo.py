
from random import randint
class Jogador():
    def __init__(self):
        self.itens = ("PEDRA", "PAPEL", "TESOURA")

    def jogar(self):

        print("""Suas opições:
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA""")

        jogador = int(input("Qual é sua jogada?"))
        computador = randint(0, 2)

        print("computador jogou",self.itens[computador])
        print("jogador jogou", self.itens[jogador])
        

        if computador == 0: # computador jogou pedra
            if jogador == 0 :
                print("Empate")
            if jogador == 1:
                print("Jogador vence")
            elif jogador == 2:
                print("Computador venceu")
            else:
                print("jogada invalida!")
        elif computador ==1: #computador jogol papel
            if jogador == 0:
                print("Computador venceu")
            elif jogador ==1:
                print("Empate")

            elif jogador ==2:
                print("jogador venceu")
        elif computador == 2: #computador jogol tesoura
            if jogador == 0:
                print("Empate")
            elif jogador ==1 :
                print("jogador venceu")
            elif jogador == 2:
                print("Computador venceu")

jogo = Jogador()
jogo.jogar()    