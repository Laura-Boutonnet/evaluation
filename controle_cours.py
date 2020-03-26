#q1

def sup21(nbr):
    if nbr >= 21:
        print(True)
    else:
        print(False)

#q2
def pairs(li):
    return [nb for nb in li if nb % 2 == 0]

#q3
def ajout4(lis):
    return lis + [4]

#q4
def to_strings(dic):
    liste = []
    for a, b in dic.items():
        liste.append(str(a) + ":" + str(b))
    return liste

#q5
def extremites(liste2):
    return liste[2:] + liste[-2:]

class Mot():
    def __init__ (self, mot):
        self.mot = mot
    def mot(self, mot):
        self.mot = mot
    def comptelettre(self, lettre, mot):
        self.letter = lettre.lower
        for lettre in mot:
            if lettre.lower() in mot.lower():
                print(self.count(lettre.lower()))


def tri_et_inverse(liste):
    return (sorted(liste), reversed(liste))
       
        
def aller_a_paris(input_call=input):
    # code a remplir
    while input_call.lower() != 'paris':
        saisie = input_call('Question ')
    return saisie
    # quelque part dans le code de cette fonction: saisie = input_call('Question ')
    # en fonction de saisie on continue a demander ou on renvoie 'Paris'
    # Au lieu d'utiliser input comme en cours vous appelez input_call
    # par dÃ©faut elle vaut input donc vous pouvez appeller
    # aller_a_paris() pour tester a la main
    while True:
        return 0, 'Nulle Part'
  
#q9
ville_nom_pays = {
        'Paris':'France',
        'Berlin':'Allemagne',
        'Madrid':'Espagne',
        'Moscou':'Russie'
        } 

#q10
class Pays():
    def __init__ (self, nom, visa):
        self.nom = nom
        self.visa = visa


ville_pays = {
        'Paris':'France',
        'Berlin':'Allemagne',
        'Madrid':'Espagne',
        'Moscou':'Russie'
        }

if __name__ == "__main__": 

    import doctest 

    if True: 

        doctest.testmod(verbose=True, optionflags=512) 

    else: 

        doctest.testmod(verbose=True) 


