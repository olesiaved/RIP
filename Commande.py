#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit 

class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self, id, stock, dP, p,list_prod):
        self._id = id                   #nom de la commande
        self._stockMin = stock          #temps mini dans la zone de stockage après production
        self._datePrevue = dP           #date de livraison prévue
        self._penalite = p              #penalités en cas de retard
        self._dateReel =None            #date réelle de livraison

        self._list_prod = list_prod     # tableau synthèse des objets à produire: [NombreProduitTypeA, NombreProduitTypeB, NombreProduitTypeC...]

        self._num_ligne : int = None    # pour la solution simpliste : 1 ligne de prod = 1 commande

        self._liste_produits_afaire = []# liste d'entités objets non terminés correspondants à la commande
        self._liste_produits_finis = [] # liste d'entités objets terminés correspondants à la commande



    def affichage(self):
        print ("Commande", self._id, " ", self._stockMin, " ", self._datePrevue, " ", self._dateReel, "",self._penalite," ",self._list_prod)


    def DateEnvoieFin(self):
        #uptade de la date reelle de livraison en fonction de la date de fin du dernier article + delais mini à attendre en stock
        print(self._stockMin)
        self._dateReel = self._liste_produits_finis[len(self._liste_produits_finis)-1]._dateFinProd + self._stockMin