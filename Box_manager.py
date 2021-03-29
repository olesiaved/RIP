#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Box import Box
from Type_box import Type_box
from Type_produit import Type_produit

# Afin d'implementer notre solution partielle il est nécessaire de run notre classe Main

# Dans cette classe Main le nom du fichier txt contenant les données y est précisé
# (ainsi le programme peut facilement être utilisé peu importe le nom du fichier txt)

# Dans le main une entitée Production est créée et sa fonction simulation_production est appelée afin de traiter les données
# créer et remplir le fichier solution (résolution de l'ensemble du problème informatique)






#gestion attribution des box et types de box aux produits
class Box_manager(object):

# Pour la solution triviale nous avons un produit = un box

# la fonction Attribution_type cherche le box le moins cher possible parmis ceux de taille superieur à la taille d'un type de produit donné
# Par la suite le type de box déterminé est conservé dans un attribut de Type_Produit qui s'appelle type_box

    def Attribution_type(self):
        for i in self._listes_types_produit:                                          # iteration sur une liste des types de produit
            b = self._listes_types_box[0]                                             # Un choix arbitraire d'un box
            for j in self._listes_types_box:                                          # iteration sur une liste des types de box afin de rechercher le meilleur pour un type de produit donné
                if i.htype<=j.hbox and i.ltype<=j.lbox and j.prix_box<b.prix_box :    # verification des conditions et comparaison des prix des box
                    b=j
            i.type_box=b


#prochainement utile (solution complète)
    def Available_Box_Type(self, aBB ) :
        pass


# Achat d'un box correspondant au produit
# Incrementation du compteur des box
    def Achat_Box_Type(self, p ):
        i=self._listes_types_box.index(p._type.type_box)
        self._listes_box[i]+=1
        p._num_box=self._listes_box[i]


    def __init__(self):
        self._listes_box = []                 # compteur des box achetés par type
        self._listes_types_produit = []
        self._listes_types_box = []


    
    