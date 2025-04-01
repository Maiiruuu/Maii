import sqlite3
from PIL import Image, ImageDraw

# Initialisation de la base de données
def init_db(db_name: str):
    """
    Initialise une base SQLite avec une table pour stocker les codes-barres.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS barcodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Ajout de données dans la base
def add_barcode_data(db_name: str, data: str):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO barcodes (data) VALUES (?)", (data,))
    conn.commit()
    conn.close()

# Récupération de données
def fetch_barcode_data(db_name: str, barcode_id: int):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM barcodes WHERE id = ?", (barcode_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Génération du code-barre (comme dans la première version)
def generate_barcode(data: str, filename: str):
    width = 400
    height = 200
    bar_width = 5
    padding = 20
    
    img = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(img)
    
    x = padding
    for char in data:
        binary = format(ord(char), '08b')
        for bit in binary:
            if bit == '1':
                draw.rectangle([x, padding, x + bar_width - 1, height - padding], fill="black")
            x += bar_width
    
    img.save(filename)
    print(f"Code-barre généré : {filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    db_name = "barcodes.db"
    
    # Initialisation de la base de données
    init_db(db_name)
    
    # Ajout de données
    add_barcode_data(db_name, "PRODUIT123")
    add_barcode_data(db_name, "CODE456")
    
    # Récupération et génération de codes-barres
    barcode_id = 1
    data = fetch_barcode_data(db_name, barcode_id)
    if data:
        generate_barcode(data, f"barcode_{barcode_id}.png")
    else:
        print(f"Aucune donnée trouvée pour l'ID {barcode_id}")
