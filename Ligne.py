#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit

# classe ligne de production
class Ligne(object):
    def Produire(self, aDate : int) -> None:
        pass
    def __init__(self,n):
        self._numero=n                  # numero de la ligne
        self._listes_commandes = []     # liste des commandes attribuées à la ligne (qui doivent donc y être produites)


    def affichage(self):
        print ("Ligne", self.___numero)

        for element in self._listes_commandes:
            element.affichage()




#"fabrication" de l'ensemble des produits attribués à la ligne de prod (=mise à jour de la date de prod. du produit en question)

#pour ce faire : étape 1 : accès à la première commande de la liste des commandes à produire ici

#"production" de l'ensemble des produits appartenant à la liste "produits à faire" de cette commande (=mise à jour de la date de prod.)

#passage à la commande suivante et ainsi de suite

    def calcul_date_produit(self):
        date = 0
        k=self._listes_commandes[0]._liste_produits_afaire[0]
        changer_commande=False
        changer_outils=True

        for i in self._listes_commandes:
            m = i._liste_produits_afaire
            for j in range(len(m)):

                if(k._type.id!=m[j]._type.id)and(changer_commande==True): # verification s'il y a eu lieu un chagement de commande
                    changer_outils = True

                if(changer_outils==True):                                 # verification s'il faut changer les outils
                    date=date+m[j]._type.s

                m[j]._dateDebutProd =date
                date=m[j]._type.p+date                                    # incrementation de la date
                m[j]._dateFinProd=date
                i._liste_produits_finis.append(m[j])

                if j+1<len(m):                                            # verification de la fin de commande
                    changer_commande=False                                # verification du changement des outils
                    if m[j+1]._type.id==m[j]._type.id:
                        changer_outils = False
                    else:
                        changer_outils=True
                else:
                    k=m[j]
                    changer_commande=True
            m.clear()
