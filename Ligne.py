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
        self._produits_afaire = []      # liste de produits attribués à cette ligne
        self.LocalDelay=0               # delais de production de la ligne (temps necessaire à tout produire)
        self.LastestProdAdded=None      # dernier produit ajouté à la ligne

    def affichage(self):
        print ("Ligne", self._numero,self.LocalDelay)


    # attribution d'un produit à la ligne de production avec prise en compte du produit précédent pour savoir si temps de set up ou non

    # actualisation du produit précédent
    # actualisation du delais de production de la ligne (temps necessaire à tout produire)
    def AddProdAfaire(self,i):
        self._produits_afaire.append(i)
        if (self.LastestProdAdded == None or self.LastestProdAdded != i._type):
            self.LocalDelay = self.LocalDelay + i._type.s + i._type.p

        elif (self.LocalDelay == i._type):
            self.LocalDelay = self.LocalDelay + i._type.p
        self.LastestProdAdded = i




    # "fabrication" de l'ensemble des produits attribués à la ligne de prod (=mise à jour de la date de prod. )
    def calcul_date_produit_opt (self):
        date = 0
        changer_outils = True
        m = self._produits_afaire
        for j in range(len(m)):
            if (changer_outils == True):         # verification de la nécessité de changement d'outils ou non (set up)
                    date = date + m[j]._type.s
            m[j]._dateDebutProd = date
            date = m[j]._type.p + date          # incrementation de la date
            m[j]._dateFinProd = date
            m[j]._numligne=self._numero
            if j + 1 < len(m):                   # verification de la fin de la production (tous les produits sont terminés)
                if m[j + 1]._type.id == m[j]._type.id:
                    changer_outils = False
                else:
                        changer_outils = True


   #
    def recherche_date_suivante(self, date):
        choix=None
        for i in self._produits_afaire:
            if i._dateFinProd>=date and i._box==None :
                choix=i
                break
        return choix