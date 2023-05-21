import dataclasses

class Eleve:
    Eleve = None

    def __init__(self, nom, anneeNaissance, atelier, master):
        self.nom = nom
        self.anneeNaissance = anneeNaissance
        self.atelier = atelier
        self.master = master

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom
        
    def dessiner(self):
        print(self.nom + " dessine dans l'atelier " + self.atelier.getNom())

    def apprentissage(self):
        print(self.nom + " apprend à dessiner dans l'atelier " + self.atelier.getNom())
