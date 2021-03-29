#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit




# Afin d'implementer notre solution partielle il est nécessaire de run notre classe "Main"

# Dans cette classe Main le nom du fichier txt contenant les données y est précisé
# (ainsi le programme peut facilement être utilisé peu importe le nom du fichier txt)

# Dans le "Main" une entité "Production" est créée et sa fonction simulation_production est appelée afin de traiter les données
# créer et remplir le fichier solution (résolution de l'ensemble du problème informatique)







# classe commande
class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self, id, stock, dP, p,list_prod):
        self._id = id                   #nom de la commande
        self._stockMin = stock          #temps mini dans la zone de stockage après production
        self._datePrevue = dP           #date de livraison prévue
        self._penalite = p              #penalités en cas de retard
        self._dateReel =None            #date réelle de livraison

        self._list_prod = list_prod     #tableau synthèse des objets à produire: [NombreProduitTypeA, NombreProduitTypeB, NombreProduitTypeC...]

        self._num_ligne : int = None     #pour la solution simpliste : 1 ligne de prod = 1 commande

        self._liste_produits_afaire = [] # liste d'entités objets non terminés correspondants à la commande
        #objet non terminé = date de production du produit en question non renseignée avant passage dans la ligne de prod.

        self._liste_produits_finis = []  # liste d'entités objets terminés correspondants à la commande
        # objet terminé = date de production du produit en question renseignée après passage dans la ligne de prod.


    def affichage(self):
        print ("Commande", self._id, " ", self._stockMin, " ", self._datePrevue, " ", self._dateReel, "",self._penalite," ",self._list_prod)



        # Uptade de la date reelle de livraison de la commande :
        # date de fin du dernier article terminé de la commande + delais mini à attendre en stock pour la commande

    def DateEnvoieFin(self):
        print(self._stockMin)
        self._dateReel = self._liste_produits_finis[len(self._liste_produits_finis)-1]._dateFinProd + self._stockMin