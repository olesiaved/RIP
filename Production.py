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
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, './Donnee1.txt')
        with open(filename, newline='') as csvfile:
            for line in csvfile:
                production_list.append(line.strip().split())
            self._lecture_txt=production_list
    def create_Type_produit(self):
        list_Type_produit=[]
        for i in range (int(self._lecture_txt[0][0])):
            list_Type_produit.append(Type_produit(self._lecture_txt[i+1][0], int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]),int(self._lecture_txt[i+1][4]), int(self._lecture_txt[i+1][5]) ))
        self.box_manager._listes_types_produit=list_Type_produit
    def create_Type_box(self):
        list_Type_box=[]
        a=int(self._lecture_txt[0][0])
        b=int(self._lecture_txt[0][1])
        c=int(self._lecture_txt[0][3])
        for i in range(a+b,a+b+c):
            list_Type_box.append(Type_box(self._lecture_txt[i+1][0], int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]) ))
        return list_Type_box

            

    def Ecriture_fichier(self):
        pass

    def Calcul_cout_box(self):
        pass

    def Calcul_cout_conteneur(self):
        pass

    def Calcul_nbdeBoxes(self):
        pass

    def __init__(self):
        self._cout = 1
        self.box_manager=Box_manager()
        """# @AssociationMultiplicity 1"""
        self._schedule : Scheduling = None
        """# @AssociationMultiplicity 1"""
        self._lecture_txt=None
