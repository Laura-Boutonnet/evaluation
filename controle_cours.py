# q1 

def sup21(): 

    i = 1
    while i< 22:
        print(i)
        i+=1 

sup21() 

#q2

def pairs(): 

    nb = [ n**2 for n in NB if n%2 != 0] 

    return nb


#q3
def ajout4(liste): 

    li = liste.append(4) 

    return li 

#q4 
def to_strings(di):
  lis = []
  for a,b in di.items():
    for i in range(b):
      lis.append(a)

  return lis
#q5
def extremites(liste1):
  li1 = liste1[c(1,2,-1,-2)]
  return li1

#q6
class Mot(): 

    def __init__(self, mot, lettre): 
        self.mot = mot 
        self.lettre = mot_len(lettre) 
    def comptelettre(self): 
        return f"Il y a {self.lettre} mettre dans le mot ({self.mot})" 

   

#q7
def tri_et_inverse(liste2):
  lis2 = liste2.sort()
  liste21 = liste2.reverse()
  return lis2,liste21

#q8
  #je ne sais pas faire
  
#q9

ville_nom_pays = {'Paris':'France', 'Berlin':'Allemagne', 'Madrid':'Espagne', 'Moscou':'Russie'}

#q10

class Pays:
  nom = ['France', 'Allemagne', 'Espagne' , 'Russie']
  visa = {'France':False,'Allemagne':False,'Espagne':False, 'Russie':True}
  def __init__(self,nom,visa,ville_pays):
    self.nom = nom
    self.visa = visa
    return f"{self.visa} and ({self.nom}) "

ville_pays = {'Paris':False, 'France':False, 'Berlin':False, 'Allemagne':False, 'Madrid':False,'Espagne':False, 'Moscou':True, 'Russie':True}    

if __name__ == "__main__": 

    import doctest 

    if True: 

        doctest.testmod(verbose=True, optionflags=512) 

    else: 

        doctest.testmod(verbose=True) 


