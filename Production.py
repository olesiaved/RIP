#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Box_manager import Box_manager
from Scheduling import Scheduling
from Commande import Commande
from Type_produit import Type_produit
from Type_box import Type_box
import os
import csv

class Production(object):
    def Calcul_cout_delay(self, aCmd : Commande):
        pass

    def Lecture_fichier(self):
        production_list=[]
        with open(r"C:\Users\lesya\OneDrive\Documents\Etudes\s2\RIP\Donnee.txt", newline='') as csvfile:
            for line in csvfile:
                production_list.append(line.strip().split())
            self._lecture_txt=production_list
    def create_Type_produit(self):
        list_Type_produit=[]
        for i in range (int(self._lecture_txt[0][0])):
            list_Type_produit.append(Type_produit(self._lecture_txt[i+1][0].replace("P",""), int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]),int(self._lecture_txt[i+1][4]), int(self._lecture_txt[i+1][5]) ))
        return list_Type_produit



            

    def Ecriture_fichier(self):
        pass

    def Calcul_cout_box(self):
        pass

    def Calcul_cout_conteneur(self):
        pass

    def Calcul_nbdeBoxes(self):
        pass

    def __init__(self):
        self.___cout = 1
        self._box_manager : Box_manager = None
        """# @AssociationMultiplicity 1"""
        self._schedule : Scheduling = None
        """# @AssociationMultiplicity 1"""
        self._lecture_txt=None

if __name__ == '__main__':
    pr=Production()
    pr.Lecture_fichier()
    list_Type_pr=pr.create_Type_produit()
    print(len(list_Type_pr))
    for Type in list_Type_pr:
        print(Type.affichage())