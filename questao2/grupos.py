class GrupoA:

    def __init__(self, equipe1, equipe2, equipe3):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.equipe3 = equipe3
        self.pontuacaoequipe1 = 0
        self.pontuacaoequipe2 = 0
        self.pontuacaoequipe3 = 0

    def fazerPartida(self, e1, e2):
        vencedor = ''
        print(f"{e1} x {e2}")
        x = int(input(f"Gols de {e1}: "))
        y = int(input(f"Gols de {e2}: "))
        gols = (x,y)
        if x > y:
            vencedor = e1
        elif x < y:
            vencedor = e2
        else:
            vencedor = "empate"
        return vencedor, gols
class GrupoB:

    def __init__(self, equipe1, equipe2, equipe3):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.equipe3 = equipe3
        self.pontuacaoequipe1 = 0
        self.pontuacaoequipe2 = 0
        self.pontuacaoequipe3 = 0

    def fazerPartida(self, e1, e2):
        vencedor = ''
        print(f"{e1} x {e2}")
        x = int(input(f"Gols de {e1}: "))
        y = int(input(f"Gols de {e2}: "))
        gols = (x,y)
        if x > y:
            vencedor = e1
        elif x < y:
            vencedor = e2
        else:
            vencedor = "empate"
        return vencedor, gols

class Finalistas:

    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2

    def fazerPartida(self, e1, e2):
        vencedor = ''
        print("Jogo final")
        print(f"{e1} x {e2}")
        x = int(input(f"Gols de {e1}: "))
        y = int(input(f"Gols de {e2}: "))
        gols = (x,y)
        if x > y:
            vencedor = e1
        elif x < y:
            vencedor = e2
        else:
            print("A competição foi para os pênaltis! 5 chances para cada!")
            pe1 = int(input(f"Quantos pênaltis a {e1} acertou? "))
            pe2 = int(input(f"Quantos pênaltis a {e2} acertou? "))
            if pe1 > pe2:
                vencedor = e1
            else:
                vencedor = e2
        return vencedor, gols
