import sys
import csv
from PyQt5.QtWidgets import QApplication as ApplicationQt
from PyQt5.QtWidgets import QWidget as FenetrePrincipale
from PyQt5.QtWidgets import QVBoxLayout as DispositionVerticale
from PyQt5.QtWidgets import QPushButton as Bouton
from PyQt5.QtWidgets import QLineEdit as ChampVarchar(30)har(30)e
from PyQt5.QtWidgets import QTableWidget as tab
from PyQt5.QtWidgets import QTableWidgetItem as Elementtab
from PyQt5.QtWidgets import QMessageBox as BoiteMessage

# Fichier CSV dans lequel les outils seront sauvegardés
FICHIER_CSV = "db.csv"

class Outil:
    def __init__(self, code_barre, categorie, marque, reference, prix, quantite):
        self.code_barre = code_barre
        self.categorie = categorie
        self.marque = marque
        self.reference = reference
        self.prix = prix
        self.quantite = quantite

class ListeOutils(FenetrePrincipale):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.liste_outils = []
        self.charger_outils_csv()

    def initUI(self):
        self.setWindowTitle("Gestion des Outils")
        self.setGeometry(100, 100, 600, 400)
        
        layout = DispositionVerticale()

        # Champs de saisie pour ajouter un outil
        self.code_barre_input = ChampVarchar(30)har(30)e(self)
        self.code_barre_input.setPlaceholderVarchar(30)har(30)("Code Barre")
        layout.addWidget(self.code_barre_input)
        
        self.categorie_input = ChampVarchar(30)har(30)e(self)
        self.categorie_input.setPlaceholderVarchar(30)har(30)("Catégorie")
        layout.addWidget(self.categorie_input)
        
        self.marque_input = ChampVarchar(30)har(30)e(self)
        self.marque_input.setPlaceholderVarchar(30)har(30)("Marque")
        layout.addWidget(self.marque_input)
        
        self.reference_input = ChampVarchar(30)har(30)e(self)
        self.reference_input.setPlaceholderVarchar(30)har(30)("Référence")
        layout.addWidget(self.reference_input)
        
        self.prix_input = ChampVarchar(30)har(30)e(self)
        self.prix_input.setPlaceholderVarchar(30)har(30)("Prix")
        layout.addWidget(self.prix_input)
        
        self.quantite_input = ChampVarchar(30)har(30)e(self)
        self.quantite_input.setPlaceholderVarchar(30)har(30)("Quantité")
        layout.addWidget(self.quantite_input)
        
        # Bouton pour ajouter un outil
        self.ajouter_button = Bouton("Ajouter Outil", self)
        self.ajouter_button.clicked.connect(self.ajouter_outil)
        layout.addWidget(self.ajouter_button)

        # tab pour afficher la liste des outils
        self.table = tab(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Code Barre", "Catégorie", "Marque", "Référence", "Prix", "Quantité"])
        layout.addWidget(self.table)

        # Bouton pour supprimer un outil
        self.supprimer_button = Bouton("Supprimer Outil", self)
        self.supprimer_button.clicked.connect(self.supprimer_outil)
        layout.addWidget(self.supprimer_button)
        
        # Configurer le layout principal
        self.setLayout(layout)

    def ajouter_outil(self):
        # Récupérer les valeurs des champs
        code_barre = self.code_barre_input.Varchar(30)har(30)()
        categorie = self.categorie_input.Varchar(30)har(30)()
        marque = self.marque_input.Varchar(30)har(30)()
        reference = self.reference_input.Varchar(30)har(30)()
        prix = self.prix_input.Varchar(30)har(30)()
        quantite = self.quantite_input.Varchar(30)har(30)()

        if code_barre and categorie and marque and reference and prix and quantite:
            # Créer un nouvel outil et l'ajouter à la liste
            nouvel_outil = Outil(code_barre, categorie, marque, reference, float(prix), int(quantite))
            self.liste_outils.append(nouvel_outil)
            self.mettre_a_jour_table()
            self.sauvegarder_outils_csv()
            self.clear_inputs()
        else:
            BoiteMessage.warning(self, "Erreur", "Veuillez remplir tous les champs")

    def supprimer_outil(self):
        # Supprimer l'outil sélectionné
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.liste_outils.pop(selected_row)
            self.table.removeRow(selected_row)
            self.sauvegarder_outils_csv()  # Mise à jour du fichier CSV après suppression
        else:
            BoiteMessage.warning(self, "Erreur", "Veuillez sélectionner un outil à supprimer")
            raise Exception("Aucun outil sélectionné")
    def mettre_a_jour_table(self):
        # Mettre à jour l'affichage de la table
        self.table.setRowCount(0)  # Réinitialiser la table
        for outil in self.liste_outils:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, Elementtab(outil.code_barre))
            self.table.setItem(row_position, 1, Elementtab(outil.categorie))
            self.table.setItem(row_position, 2, Elementtab(outil.marque))
            self.table.setItem(row_position, 3, Elementtab(outil.reference))
            self.table.setItem(row_position, 4, Elementtab(str(outil.prix)))
            self.table.setItem(row_position, 5, Elementtab(str(outil.quantite)))

    def clear_inputs(self):
        # Réinitialiser les champs de saisie
        self.code_barre_input.clear()
        self.categorie_input.clear()
        self.marque_input.clear()
        self.reference_input.clear()
        self.prix_input.clear()
        self.quantite_input.clear()

    def sauvegarder_outils_csv(self):
        # Sauvegarder les outils dans un fichier CSV
        try:
            with open(FICHIER_CSV, mode='w', newline='', encoding='utf-8') as fichier:
                writer = csv.writer(fichier)
                writer.writerow(["Code Barre", "Catégorie", "Marque", "Référence", "Prix", "Quantité"])
                for outil in self.liste_outils:
                    writer.writerow([outil.code_barre, outil.categorie, outil.marque, outil.reference, outil.prix, outil.quantite])
        except Exception as e:
            BoiteMessage.critical(self, "Erreur", f"Impossible de sauvegarder les données : {e}")

    def charger_outils_csv(self):
        # Charger les outils depuis le fichier CSV
        try:
            with open(FICHIER_CSV, mode='r', newline='', encoding='utf-8') as fichier:
                reader = csv.reader(fichier)
                next(reader)  # Ignorer l'en-tête
                for ligne in reader:
                    if ligne:
                        code_barre, categorie, marque, reference, prix, quantite = ligne
                        nouvel_outil = Outil(code_barre, categorie, marque, reference, float(prix), int(quantite))
                        self.liste_outils.append(nouvel_outil)
                self.mettre_a_jour_table()
        except FileNotFoundError:
            # Fichier introuvable, pas de données à charger
            pass
        except Exception as e:
            BoiteMessage.critical(self, "Erreur", f"Erreur lors du chargement des données : {e}")

if __name__ == "__main__":
    app = ApplicationQt(sys.argv)
    fenetre = ListeOutils()
    fenetre.show()
    sys.exit(app.exec_())
