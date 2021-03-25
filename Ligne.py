#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit


class Ligne(object):
    def Produire(self, aDate : int) -> None:
        pass
    def __init__(self,n):
        self._numero=n
        self.___produit_en_Cours : Produit = None
        self.___dernier_Produit_fini : Produit = None
        self._listes_commandes = []

    def affichage(self):
        print ("Ligne", self.___numero)

        for element in self._listes_commandes:
            element.affichage()


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
                m[j].affichage()
                i._liste_produits_finis.append(m[j])
                if j+1<len(m):
                    if m[j+1]._type.id==m[j]._type.id:
                        changer_outils = False
                    else:
                        changer_outils=True
                        print(1)
                else:
                    changer_outils = True
            m.clear()
