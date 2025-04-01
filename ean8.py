from PIL import Image, ImageDraw


EAN13_TABLE = {
    "gauche": {
        "A": {
            "0": "0001101", "1": "0011001", "2": "0010011", "3": "0111101",
            "4": "0100011", "5": "0110001", "6": "0101111", "7": "0111011",
            "8": "0110111", "9": "0001011"
        },
        "B": {
            "0": "0100111", "1": "0110011", "2": "0011011", "3": "0100001",
            "4": "0011101", "5": "0111001", "6": "0000101", "7": "0010001",
            "8": "0001001", "9": "0010111"
        }
    },
    "droite": {
        "0": "1110010", "1": "1100110", "2": "1101100", "3": "1000010",
        "4": "1011100", "5": "1001110", "6": "1010000", "7": "1000100",
        "8": "1001000", "9": "1110100"
    }
}


ENCODAGE_GAUCHE = {
    "0": "AAAAAA", "1": "AABABB", "2": "AABBAB", "3": "AABBBA",
    "4": "ABAABB", "5": "ABBAAB", "6": "ABBBAA", "7": "ABABAB",
    "8": "ABABBA", "9": "ABBABA"
}

# Zones de garde
ZONE_GARDE = {
    "début": "101",
    "milieu": "01010",
    "fin": "101"
}

# Controle
def smmme_cntrl(code):
    somme = sum(int(chiffre) * (3 if i % 2 else 1) for i, chiffre in enumerate(code))
    return (10 - (somme % 10)) % 10

# Mise EN place de la sequence principal en bin
def seqbin(code):
    sequence = ZONE_GARDE["début"]
    structure = ENCODAGE_GAUCHE[code[0]]
    for i in range(1, 7):
        encodage = structure[i - 1]
        sequence += EAN13_TABLE["gauche"][encodage][code[i]]
    sequence += ZONE_GARDE["milieu"]
    for i in range(7, 13):
        sequence += EAN13_TABLE["droite"][code[i]]
    sequence += ZONE_GARDE["fin"]
    return sequence

# Creation de l'image
def img(sequence, nom_fichier):
    largeur = len(sequence)
    hauteur = 100
    image = Image.new("1", (largeur, hauteur), 1)  # 1 pour en blanc
    draw = ImageDraw.Draw(image)

    for x, bit in enumerate(sequence):
        if bit == "1":
            draw.line([(x, 0), (x, hauteur)], fill=0)  

    image.save(nom_fichier)
    print(f"Code-barres enregistré sous {nom_fichier}")

# Programme principal (main prgrm)
def codebarreean13(code):
    if len(code) != 12 or not code.isdigit():
        raise ValueError("Le code doit comporter 12 chiffres.")

    code += str(smmme_cntrl(code))  
    sequence = seqbin(code) 
    img(sequence, "ean13.png")

# Appels
codebarreean13("123456789012")