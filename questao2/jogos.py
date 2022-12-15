from grupos import GrupoA
from grupos import GrupoB
from grupos import Finalistas

x = input("Digite a equipe 1 do Grupo A: ")
y = input("Digite a equipe 2 do Grupo A: ")
z = input("Digite a equipe 3 do Grupo A: ")
grupoA = GrupoA(x, y, z)

x = input("Digite a equipe 1 do Grupo B: ")
y = input("Digite a equipe 2 do Grupo B: ")
z = input("Digite a equipe 3 do Grupo B: ")
grupoB = GrupoB(x, y, z)

golsgrupoA = [0]*3
for c in range(3):
    if c == 0 or c == 1:
        e1 = grupoA.equipe1
        if c == 0:
            e2 = grupoA.equipe2
        else:
            e2 = grupoA.equipe3
    else:
        e1 = grupoA.equipe2
        e2 = grupoA.equipe3
    vencedor, golsgrupoA[c] = grupoA.fazerPartida(e1, e2)
    if vencedor == e1:
        if e1 == grupoA.equipe1:
            grupoA.pontuacaoequipe1 += 3
        elif e1 == grupoA.equipe2:
            grupoA.pontuacaoequipe2 += 3
    elif vencedor == e2:
        if e2 == grupoA.equipe2:
            grupoA.pontuacaoequipe2 += 3
        elif e2 == grupoA.equipe3:
            grupoA.pontuacaoequipe3 += 3
    else:
        if e1 == grupoA.equipe1:
            grupoA.pontuacaoequipe1 += 1
        elif e1 == grupoA.equipe2:
            grupoA.pontuacaoequipe2 += 1
        if e2 == grupoA.equipe2:
            grupoA.pontuacaoequipe2 += 1
        elif e2 == grupoA.equipe3:
            grupoA.pontuacaoequipe3 += 1

golsgrupoB = [0]*3
for c in range(3):
    if c == 0 or c == 1:
        e1 = grupoB.equipe1
        if c == 0:
            e2 = grupoB.equipe2
        else:
            e2 = grupoB.equipe3
    else:
        e1 = grupoB.equipe2
        e2 = grupoB.equipe3
    vencedor, golsgrupoB[c] = grupoB.fazerPartida(e1, e2)
    if vencedor == e1:
        if e1 == grupoB.equipe1:
            grupoB.pontuacaoequipe1 += 3
        elif e1 == grupoB.equipe2:
            grupoB.pontuacaoequipe2 += 3
    elif vencedor == e2:
        if e2 == grupoB.equipe2:
            grupoB.pontuacaoequipe2 += 3
        elif e2 == grupoB.equipe3:
            grupoB.pontuacaoequipe3 += 3
    else:
        if e1 == grupoB.equipe1:
            grupoB.pontuacaoequipe1 += 1
        elif e1 == grupoB.equipe2:
            grupoB.pontuacaoequipe2 += 1
        if e2 == grupoB.equipe2:
            grupoB.pontuacaoequipe2 += 1
        elif e2 == grupoB.equipe3:
            grupoB.pontuacaoequipe3 += 1

vencedorGrupoA = ''
if grupoA.pontuacaoequipe1 >= grupoA.pontuacaoequipe2 and grupoA.pontuacaoequipe1 >= grupoA.pontuacaoequipe3:
    vencedorGrupoA = grupoA.equipe1
elif grupoA.pontuacaoequipe2 > grupoA.pontuacaoequipe1 and grupoA.pontuacaoequipe2 >= grupoA.pontuacaoequipe3:
    vencedorGrupoA = grupoA.equipe2
else:
    vencedorGrupoA = grupoA.equipe3

vencedorGrupoB = ''
if grupoB.pontuacaoequipe1 >= grupoB.pontuacaoequipe2 and grupoB.pontuacaoequipe1 >= grupoB.pontuacaoequipe3:
    vencedorGrupoB = grupoB.equipe1
elif grupoB.pontuacaoequipe2 > grupoB.pontuacaoequipe1 and grupoB.pontuacaoequipe2 >= grupoB.pontuacaoequipe3:
    vencedorGrupoB = grupoB.equipe2
else:
    vencedorGrupoB = grupoB.equipe3

finalistas = Finalistas(vencedorGrupoA, vencedorGrupoB)
vencedorFinal, golsFinal = finalistas.fazerPartida(vencedorGrupoA, vencedorGrupoB)

print()
print('Grupo A')
print(f"{grupoA.equipe1} x {grupoA.equipe2} {golsgrupoA[0]}")
print(f"{grupoA.equipe1} x {grupoA.equipe3} {golsgrupoA[1]}")
print(f"{grupoA.equipe2} x {grupoA.equipe3} {golsgrupoA[2]}")
print()
print("Grupo B")
print(f"{grupoB.equipe1} x {grupoB.equipe2} {golsgrupoB[0]}")
print(f"{grupoB.equipe1} x {grupoB.equipe3} {golsgrupoB[1]}")
print(f"{grupoB.equipe2} x {grupoB.equipe3} {golsgrupoB[2]}")
print()
print("Final")
print(f"{finalistas.equipe1} x {finalistas.equipe2} {golsFinal}")
print(f"O vencedor foi: {vencedorFinal}!")
