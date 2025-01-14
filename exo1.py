class EquipementReseau:
    def __init__(self, nom, adresse_ip):
        self.nom = nom
        self.adresse_ip = adresse_ip

    def afficher_info(self):
        print(f"Nom: {self.nom}, Adresse IP: {self.adresse_ip}")


class ConnexionReseau:
    def __init__(self, equipement1, equipement2, type_connexion):
        self.equipement1 = equipement1  # Objet de type EquipementReseau
        self.equipement2 = equipement2  # Objet de type EquipementReseau
        self.type_connexion = type_connexion

    def afficher_details(self):
        print("Détails de la connexion :")
        print("Équipement 1 :")
        self.equipement1.afficher_info()
        print("Équipement 2 :")
        self.equipement2.afficher_info()
        print(f"Type de connexion : {self.type_connexion}")



# Création des équipements réseau
equipement1 = EquipementReseau("Switch01", "192.168.1.1")
equipement2 = EquipementReseau("Router01", "192.168.1.254")

# Création d'une connexion réseau
connexion = ConnexionReseau(equipement1, equipement2, "Ethernet")

# Affichage des détails de la connexion
connexion.afficher_details()

