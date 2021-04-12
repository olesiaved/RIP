#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Box import Box
from Type_box import Type_box
from Type_produit import Type_produit
import random

#gestion attribution des box et types de box aux produits
class Box_manager(object):

# la fonction Attribution_type cherche le box le moins cher possible parmis ceux de taille superieur à la taille d'un type de produit donné
# Par la suite le type de box déterminé est conservé dans un attribut de Type_Produit qui s'appelle type_box


    def Attribution_type(self):
        for i in self._listes_types_produit:                                      # iteration sur une liste des types de produit
            b = self._listes_types_box[0]
            c = self._listes_types_box[0]       # Un choix arbitraire d'un box
            for j in self._listes_types_box:
                if i.nbEmpileMax*i.htype<=j.hbox and b.lbox<=j.lbox:
                    b=j                                                                 # iteration sur une liste des types de box afin de rechercher le meilleur pour un type de produit donné
            for k in self._listes_types_box:
                if k.prix_box<c.prix_box and i.htype<=k.hbox and i.ltype<=k.lbox :                   # verification des conditions et comparaison des prix des box
                     c=k
            c.affichage()
            b.affichage()
            if c.prix_box>=b.prix_box:
                i.type_box=b
            else:
                i.type_box = c

#calcul de la place libre restante dans une box compte tenu des produits déjà à l'intérieur
    def calcul_place_libre(self, box):
        long= box._type.lbox
        place_ocupee=0
        for i in range (len(box._type_pile)):
            if box._produit[i]!=0:
                place_ocupee+=box._type_pile[i].ltype
        return long-place_ocupee

#prochainement utile (solution complète)
    def Available_Box_Type(self, p) :
        box=None
        trouve=False
        for j in self._listes_box:
            if (j._id_commande == p._id_commande) and (trouve==False):
                for t in range(len(j._type_pile)):
                    if p._type==j._type_pile[t]:
                        i=t
                        if j._produit[i]<p._type.nbEmpileMax:
                            if j._type.hbox-j._produit[i]*p._type.htype>p._type.htype:
                                trouve=True
                                box = j
                                box._produit[i] += 1
                                p._box = box
        if trouve==False:
            for j in self._listes_box:
                if j._id_commande == p._id_commande and p._type.ltype < self.calcul_place_libre(j)and trouve==False:
                    trouve=True
                    box=j
                    p._box=box
                    box._produit.append(1)
                    box._type_pile.append(p._type)
                if trouve==True:
                    break
        if trouve == False:
            for j in self._listes_box:
                if j._id_commande == None :
                    trouve=True
                    box=j
                    p._box=box
                    box._produit.append(1)
                    box._type_pile.append(p._type)
                    box._id_commande=p._id_commande
                if trouve==True:
                    break
        return box

    def Vider_box_commande_envoye(self, com):
        for i in self._listes_box:
            if i._id_commande==com._id:
                i.ViderBox()




# Achat d'un box correspondant au produit
# Incrementation du compteur des box
    def Achat_Box_Type(self, p ):

        i =self._listes_types_box.index(p._type.type_box)
        self._compteur_box[i]+=1
        box=Box(self._compteur_box[i],self._listes_types_box[i])
        self._listes_box.append(box)
        box._id_commande=p._id_commande
        box._type_pile.append(p._type)
        box._produit.append(1)
        p._box=box
        box._numero=self._compteur_box[i]

    def gestion_produit_finis(self, p):

        b=self.Available_Box_Type(p)
        if b==None:
            self.Achat_Box_Type(p)



    def __init__(self):
        self._listes_box = []     # compteur des box achetés par type
        self._listes_types_produit = []
        self._listes_types_box = []
        self._compteur_box=[]

    
    