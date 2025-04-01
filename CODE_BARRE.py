from PIL import Image, ImageDraw #je remarque que l'on a seulement besoin de cela 

# je détaillerai ce code le plus possible étant la premiere fois de l'utilisation de l'utilisatiodn de pillow 
    #https://www.geeksforgeeks.org/python-pil-image-new-method/
    #https://fr.wikipedia.org/wiki/Code-barres_EAN

def generate_barcode(data: str, filename: str): #de type ste et str 

    # Configuration du code-barre
    width = 400
    height = 200
    bar_width = 5
    padding = 20

    # Créer une image blanche
    img = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(img)
    
    # Génération du code-barre
    x = padding
    for char in data:
        binary = format(ord(char), '08b')  # Convertit le caractère en binaire
        for bit in binary:
            if bit == '1':
                draw.rectangle([x, padding, x + bar_width - 1, height - padding], fill="black")
            x += bar_width
    
    # Enregistrer l'image
    img.save(filename)
    print(f"Code-barre généré : {filename}")

# Exemple d'utilisation
a = (3*'\n'+'/'+10*("-->_<--")+'/' + 3*'\n')
print(a)

generate_barcode("PRODUIT123", "barcode1.png")
print(a)
