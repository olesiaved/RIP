#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit


class Ligne(object):
    def Produire(self, aDate : int) -> None:
        pass
    def __init__(self,n):
        self._numero=n                  #numero de la ligne
        self._listes_commandes = []     # liste des commandes attribuées à la ligne (qui doivent donc y être produites)


    def affichage(self):
        print ("Ligne", self.___numero)

        for element in self._listes_commandes:
            element.affichage()

#fabrication de l'ensemble des produits attribués à la ligne de prod

#pour ce faire : étape 1 : accès à la première commande de la liste des commandes à produire sur la ligne de prod

#production de l'ensemble des produits appartenant à la liste "produits à faire" de cette commande

#passage à la commande suivante

    def calcul_date_produit(self):
        date = 0
        changer_outils=True

        for i in self._listes_commandes:
            m = i._liste_produits_afaire
            for j in range(len(m)):
                if(changer_outils==True):
                    date=date+m[j]._type.s
                m[j]._dateDebutProd =date
                date=m[j]._type.p+date
                m[j]._dateFinProd=date
                #print(m[j]._dateDebutProd)
                i._liste_produits_finis.append(m[j])
                if j+1<len(m) :
                    if m[j+1]._type!=m[j]._type:
                        changer_outils=True
                    else:
                        changer_outils=False
            m.clear()
