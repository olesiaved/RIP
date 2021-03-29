#!/usr/bin/python
# -*- coding: UTF-8 -*-



# Afin d'implementer notre solution partielle il est nécessaire de run notre classe "Main"

# Dans cette classe Main le nom du fichier txt contenant les données y est précisé
# (ainsi le programme peut facilement être utilisé peu importe le nom du fichier txt)

# Dans le "Main" une entité "Production" est créée et sa fonction simulation_production est appelée afin de traiter les données
# créer et remplir le fichier solution (résolution de l'ensemble du problème informatique)


#type de box et caractéristiques
class Type_box(object):

    def __init__(self, t, h, l, p):
        self.type = t       #type de box
        self.hbox = h       #hauteur de la box
        self.lbox = l       #longueur de la box
        self.prix_box = p   # prix de la box

    def affichage(self):
        print ("Type_box", self.type, " ", self.hbox, " ", self.lbox, " ", self.prix_box)