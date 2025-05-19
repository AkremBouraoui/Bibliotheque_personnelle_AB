import json
import os

nom_fichier = "bibliotheque.json"

def charger_livres():
    if os.path.exists(nom_fichier):
        with open(nom_fichier, "r") as f:
            return json.load(f)
    return []

def sauvegarder_livres(livres):
    with open(nom_fichier, "w") as f:
        json.dump(livres, f, indent=4)

def voir_livres(livres):
    if len(livres) == 0:
        print("Y'a pas encore de livres.")
        return
    for livre in livres:
        print("ID:", livre["ID"])
        print("Titre:", livre["Titre"])
        print("Auteur:", livre["Auteur"])
        print("Année:", livre["Année"])
        print("Lu:", "Oui" if livre["Lu"] else "Non")
        print("Note:", livre["Note"] if livre["Note"] else "Pas de note")
        print("----------------------")

def ajouter_livre(livres):
    titre = input("Titre du livre : ")
    auteur = input("Auteur du livre : ")
    annee = input("Année de publication : ")

    if len(livres) == 0:
        nouvel_id = 1
    else:
        nouvel_id = livres[-1]["ID"] + 1

    nouveau_livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }

    livres.append(nouveau_livre)
    print("Livre ajouté avec succès.")

def supprimer_livre(livres):
    try:
        id_supprimer = int(input("ID du livre à supprimer : "))
        for livre in livres:
            if livre["ID"] == id_supprimer:
                livres.remove(livre)
                print("Livre supprimé avec succès.")
                return
        print("Aucun livre trouvé avec cet ID.")
    except:
        print("Entrée invalide. Donne un numéro.")

def rechercher_livre(livres):
    mot_cle = input("Entrez un mot-clé (titre ou auteur) : ").lower()
    trouve = False
    for livre in livres:
        if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower():
            print("ID:", livre["ID"])
            print("Titre:", livre["Titre"])
            print("Auteur:", livre["Auteur"])
            print("Année:", livre["Année"])
            print("Lu:", "Oui" if livre["Lu"] else "Non")
            print("Note:", livre["Note"] if livre["Note"] else "Pas de note")
            print("-" * 20)
            trouve = True
    if not trouve:
        print("Aucun livre trouvé avec ce mot.")

def afficher_lus_ou_non_lus(livres):
    choix = input("Afficher les livres (1) lus ou (2) non lus ? ")
    if choix == "1":
        livres_filtres = [livre for livre in livres if livre["Lu"]]
    elif choix == "2":
        livres_filtres = [livre for livre in livres if not livre["Lu"]]
    else:
        print("Choix invalide.")
        return

    if not livres_filtres:
        print("Aucun livre trouvé.")
        return

    for livre in livres_filtres:
        print("ID:", livre["ID"])
        print("Titre:", livre["Titre"])
        print("Auteur:", livre["Auteur"])
        print("Année:", livre["Année"])
        print("Lu:", "Oui" if livre["Lu"] else "Non")
        print("Note:", livre["Note"] if livre["Note"] else "Pas de note")
        print("-" * 20)

def trier_par_annee(livres):
    if not livres:
        print("Aucun livre à trier.")
        return
    
    livres_tries = sorted(livres, key=lambda x: int(x["Année"]))
    print("\n=== Livres triés par année ===")
    for livre in livres_tries:
        print("Titre:", livre["Titre"])
        print("Auteur:", livre["Auteur"])
        print("Année:", livre["Année"])
        print("-" * 20)

def marquer_comme_lu(livres):
    try:
        id_choisi = int(input("Entrez l'ID du livre que vous avez lu : "))
        for livre in livres:
            if livre["ID"] == id_choisi:
                livre["Lu"] = True
                print("Livre marqué comme lu.")
                noter = input("Voulez-vous donner une note ? (oui/non) : ").lower()
                if noter == "oui":
                    try:
                        note = int(input("Note sur 10 : "))
                        if 0 <= note <= 10:
                            livre["Note"] = note
                            print("Note ajoutée.")
                        else:
                            print("Note invalide. Elle doit être entre 0 et 10.")
                    except:
                        print("Entrée invalide pour la note.")
                return
        print("Aucun livre trouvé avec cet ID.")
    except:
        print("Entrée invalide.")



def menu():
    print("\n=== Ma Bibliothèque ===")
    print("1. Voir les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Quitter")
    print("5. Rechercher un livre")
    print("6. Voir les livres lus ou non lus")
    print("7. Trier les livres par année")
    print("8. Marquer un livre comme lu et noter")


    
def main():
    mes_livres = charger_livres()

    while True:
        menu()
        choix = input("Ton choix : ")

        if choix == "1":
            voir_livres(mes_livres)
        elif choix == "2":
            ajouter_livre(mes_livres)
        elif choix == "3":
            supprimer_livre(mes_livres)
        elif choix == "4":
            sauvegarder_livres(mes_livres)
            print("Bye !")
            break
        elif choix == "5":
            rechercher_livre(mes_livres)
        elif choix == "6":
            afficher_lus_ou_non_lus(mes_livres)
        elif choix == "7":
            trier_par_annee(mes_livres)
        elif choix == "8":
            marquer_comme_lu(mes_livres)
        else:
            print("Choix invalide. Essaie encore.")
        
 

main()

