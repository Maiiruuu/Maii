import sys
import random
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class RouletteGame(QWidget):
    def __init__(self):
        super().__init__()

        self.solde_utilisateur = 100
        self.mise_initiale = 2
        self.gain = self.mise_initiale
        self.tour = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Jeu de Roulette")
        self.setGeometry(100, 100, 400, 300)

        self.label_solde = QLabel(f"Solde: {self.solde_utilisateur}€", self)
        self.label_prob = QLabel("Probabilité de victoire: Calcul en cours...", self)
        self.label_resultat = QLabel("", self)

        self.btn_lancer = QPushButton("Lancer le Tour", self)
        self.btn_lancer.clicked.connect(self.lancer_tour)

        self.btn_quitter = QPushButton("Quitter", self)
        self.btn_quitter.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label_solde)
        layout.addWidget(self.label_prob)
        layout.addWidget(self.label_resultat)
        layout.addWidget(self.btn_lancer)
        layout.addWidget(self.btn_quitter)

        self.setLayout(layout)

    def fonction_rudh_godgerg(self, tour, solde_utilisateur):
        base = math.sin(tour / 10)
        ajustement = random.uniform(-0.05, 0.05)
        return 0.4 + (base + ajustement) * (solde_utilisateur / 1000)

    def lancer_tour(self):
        self.tour += 1
        prob_victoire = self.fonction_rudh_godgerg(self.tour, self.solde_utilisateur)
        self.label_prob.setText(f"Probabilité de victoire: {prob_victoire:.4f}")

        if random.random() < prob_victoire:
            self.solde_utilisateur += self.gain
            self.label_resultat.setText(f"Vous avez gagné! Vous avez reçu {self.gain}€.")
            self.gain *= 2
        else:
            self.solde_utilisateur -= 10
            self.label_resultat.setText("La banque a gagné! Vous avez perdu 10€.")

        self.label_solde.setText(f"Solde: {self.solde_utilisateur}€")

        if self.solde_utilisateur < self.mise_initiale:
            self.label_resultat.setText("Vous n'avez plus assez d'argent pour continuer à jouer.")
            self.btn_lancer.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    game = RouletteGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
