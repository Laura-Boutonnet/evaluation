
def creation_colis(categorie):
    print("creation {categorie} colis")
    if categorie == "enveloppe":
        poids = 0.5
        return {"categorie": categorie, "poids": poids}
    elif categorie == "petit":
        poids = 1
        return {"categorie": categorie, "poids": poids}
    elif categorie == "moyen":
        poids = 3
        return {"categorie": categorie, "poids": poids}
    elif categorie == "grand":
        poids = 5
        return {"categorie": categorie, "poids": poids}
    elif categorie == "enorme":
        poids = 10
        return {"categorie": categorie, "poids": poids}
    else:
        print("Erreur {categorie} est inconnu")
#Ici on cree nos differents colis avec leurs poids associes
        
def creation_colis2(categories):
    return [creation_colis(categorie) for categorie in categories]
#Ici on retourne chacun de nos colis cree avec leurs poids associes

ascenceur = {"colis2": [], "poids_max": 25}
#Ici on cree notre ascenceur avec un poids maximale de 25 kilos

def poids_restant_dans_l_ascenceur(ascenceur):
    return sledge["poids_max"] - sum(categorie["poids"] for categorie in ascenceur["categories"])
#Ici on calcule le poids restant dans l'ascenceur

def poids_dans_l_ascenceur(ascenceur):
      return sum(categorie["poids"] for categorie in ascenceur["categories"])
#Ici on calcule le poids qui est deja dans l'ascenceur

def prendre_colis(ascenceur, categorie):
    if categorie["poids"] <= poids_restant_dans_l_ascenceur(ascenceur):
        ascenceur["categories"].append(categorie)
        return 1
    else:
        return 0
 #Ici on regarde si on peut mettre un nouveau colis ou non, si la sortie est 0 le colis n'a pas pu etre mis, si la sortie est 1 nous avons pu mettre notre colis

def final_colis_poids(ascenceur):
    print(f"Dans l'ascenceur il y a {len(ascenceur['categorie'])} colis")
    print(f"L'ascenceur porte {poids_dans_l_ascenceur(ascenceur)} kg de colis")
 

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        nb_colis = int(sys.argv[1])
    else:
        nb_colis = 15
    from random import choices
    categorie = choices(["enveloppe", "petit", "moyen", "grand", "enorme"], k=nb_colis)
    creation_colis(categorie)

