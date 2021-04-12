#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit

# classe commande
class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self, id, stock, dP, p,list_prod):
        self._id = id                   # nom de la commande
        self._stockMin = stock          # temps mini dans la zone de stockage après production
        self._datePrevue = dP           # date de livraison prévue
        self._penalite = p              # penalités en cas de retard
        self._dateReel =None            # date réelle de livraison

        self._list_prod = list_prod     # tableau synthèse des objets à produire: [NombreProduitTypeA, NombreProduitTypeB, NombreProduitTypeC...]

        self._liste_produits_afaire = [] # liste d'entités des produits de la commandes [Produit1  Produit2  Produit3 ...]



    def affichage(self):
        print ("Commande", self._id, " ", self._stockMin, " ", self._datePrevue, " ", self._dateReel, "",self._penalite," ",self._list_prod)

    # calcul de la date d'envoie de la commande : date fabrication la plus tardive + delais d'attente minimum
    def DateEnvoieFin(self):
        max=self._liste_produits_afaire[0]

        for i in self._liste_produits_afaire:
            if i._dateFinProd>max._dateFinProd:
                max=i

        self._dateReel = max._dateFinProd + self._stockMin
