import PIL
import PIL.ImageDraw

gauche = {
    0: "0001101",
    1: "0011001",
    2: "0010011",
    3: "0111101",
    4: "0100011",
    5: "0110001",
    6: "0101111",
    7: "0111011",
    8: "0110111",
    9: "0001011"
}

droite = {
    0: "1110010",
    1: "1100110",
    2: "1101100",
    3: "1000010",
    4: "1011100",
    5: "1001110",
    6: "1010000",
    7: "1000100",
    8: "1001000",
    9: "1110100"
}

def ean8(nb):
    gauche_code = ""
    droite_code = ""
    controle = 0
    nb = str(nb)
    

    if len(nb) != 7:
        return "Erreur : le nombre doi avoir 7 chiffres"
    

    for i in range(4):
        gauche_code += gauche[int(nb[i])]
        if i % 2 == 0:
            controle += int(nb[i]) * 3
        else:
            controle += int(nb[i])
    

    for i in range(4, 7):
        droite_code += droite[int(nb[i])]
        if (i - 4) % 2 == 0:
            controle += int(nb[i]) * 3
        else:
            controle += int(nb[i])

    controle = (10 - (controle % 10)) % 10
    controle_code = droite[controle]
    

    code = "101" + gauche_code + "01010" + droite_code + controle_code + "101"
    
    # Création de l'image du code-barres
    image = PIL.Image.new("RGB", (len(code) * 10, 100), "white")
    drawede = PIL.ImageDraw.Draw(image)

    for i in range(len(code)):
        if code[i] == '1':
            drawede.rectangle((i * 10, 0, (i + 1) * 10, 100), fill="black")

    image.save("ean8_du_seigneur.png")
    image.show()


def ean13(nb):
    gauche_code = ""
    droite_code = ""
    controle = 0
    nb = str(nb)
    

    if len(nb) != 12:
        return "Erreur : le nombre doigt avoir 12 chiffre"
    
    for i in range(6):
        gauche_code += gauche[int(nb[i])]
        if i % 2 == 0:
            controle += int(nb[i])
        else:
            controle += int(nb[i]) * 3
    

    for i in range(6, 12):
        droite_code += droite[int(nb[i])]
        if i % 2 == 0:
            controle += int(nb[i])
        else:
            controle += int(nb[i]) * 3
    
    # Calcul de la clé de contrôle
    controle = (10 - (controle % 10)) % 10
    controle_code = droite[controle]
    

    code = "101" + gauche_code + "01010" + droite_code + controle_code + "101"
    
    image = PIL.Image.new("RGB", (len(code) * 10, 100), "white")
    drawede = PIL.ImageDraw.Draw(image)
    

    for i in range(len(code)):
        if code[i] == '1':
            drawede.rectangle((i * 10, 0, (i + 1) * 10, 100), fill="black")
    

    image.save("ean13.png")
    image.show()

# Entrée utilisateur et gestion des choix entre EAN8 et EAN13
entree = input("Entrez un nombre pour le code EAN8 ou EAN13 : ")
if len(entree) == 7:
    ean8(entree)
elif len(entree) == 12:
    ean13(entree)
else:
    print("Erreur : le nombre doit avoir 7 ou 12 chiffres")
