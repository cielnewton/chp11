class PeripheriqueIoT:
    def __init__(self, nom, adresse_mac, statut="Inactif"):
        self.nom = nom
        self.adresse_mac = adresse_mac
        self.statut = statut

    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut

    def afficher_info(self):
        # print("La méthode afficher de la classe PeripheriqueIoT")
        print(f"Nom: {self.nom}, Adresse MAC: {self.adresse_mac}, Statut: {self.statut}")


class GestionIoT:
    def __init__(self):
        self.peripheriques = []

    def ajouter_peripherique(self, peripherique):
        self.peripheriques.append(peripherique)

    def afficher_tous_peripheriques(self):
        if not self.peripheriques:
            print("Aucun périphérique enregistré.")
            return
        for peripherique in self.peripheriques:
            peripherique.afficher_info()


# Programme principal
gestion = GestionIoT()


iot1 = PeripheriqueIoT("Capteur Température", "00:1B:44:11:3A:B7")
iot2 = PeripheriqueIoT("Camera Sécurité", "00:1B:44:11:3A:B8", "Actif")


gestion.ajouter_peripherique(iot1)
gestion.ajouter_peripherique(iot2)

iot1.changer_statut("Actif")

gestion.afficher_tous_peripheriques()
