#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit

# classe ligne de production
class Ligne(object):
    def Produire(self, aDate : int) -> None:
        pass
    def __init__(self,n):
        self._numero=n                  # numero de la ligne
        self._listes_commandes = []  # liste des commandes attribuées à la ligne (qui doivent donc y être produites)
        self._produits_afaire = []
        self.LocalDelay=0
        self.LastestProdAdded=None

    def affichage(self):
        print ("Ligne", self.___numero)

        for element in self._listes_commandes:
            element.affichage()


    def AddProdAfaire(self,i):
        self._produits_afaire.append(i)
        if (self.LastestProdAdded == None or self.LastestProdAdded != i._type):
            self.LocalDelay = self.LocalDelay + i._type.s + i._type.p

        elif (self.LocalDelay == i._type):
            self.LocalDelay = self.LocalDelay + i._type.p
        self.LastestProdAdded = i

    # "fabrication" de l'ensemble des produits attribués à la ligne de prod (=mise à jour de la date de prod. du produit en question)

    # pour ce faire : étape 1 : accès à la première commande de la liste des commandes à produire ici

    # "production" de l'ensemble des produits appartenant à la liste "produits à faire" de cette commande (=mise à jour de la date de prod.)

    # passage à la commande suivante et ainsi de suite

    def calcul_date_produit(self):
        date = 0
        k = None
        m = None
        for i in self._produits_afaire:
            m = i._type
            if (k == None or k != m):
                i._dateDebutProd = date
                date = date + i._type.s + i._type.p
                i._dateFinProd = date


            elif (k == m):
                i._dateDebutProd = date
                date = date + i._type.p
                i._dateFinProd = date
            print(date)
            k = i._type

    def calcul_date_produit_opt (self):
        date = 0
        changer_outils = True
        m = self._produits_afaire
        for j in range(len(m)):
            if (changer_outils == True):  # verification s'il faut changer les outils
                    date = date + m[j]._type.s
            m[j]._dateDebutProd = date
            date = m[j]._type.p + date  # incrementation de la date
            m[j]._dateFinProd = date
            if j + 1 < len(m):  # verification de la fin de commande
                if m[j + 1]._type.id == m[j]._type.id:
                    changer_outils = False
                else:
                        changer_outils = True

    def recherche_date_suivante(self, date):
        choix=None
        for i in self._produits_afaire:
            if i._dateFinProd>=date and i._box==None :
                choix=i
                break
        return choix