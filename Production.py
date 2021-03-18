#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Box_manager import Box_manager
from Scheduling import Scheduling
from Commande import Commande
from Type_produit import Type_produit
from Ligne import Ligne
from Type_box import Type_box

class Production(object):
    def simulation_production(self,filename):
        self.Lecture_fichier(filename)
        self.create_Lignes()
        self.create_Commandes()
        self.create_Type_box()
        self.create_Type_produit()
    def Calcul_cout_delay(self, aCmd : Commande):
        pass
    #une méthode qui s'occupe de la lecture du fichier txt. L'argument est un chemin relatif pour ceux fichier
    def Lecture_fichier(self,filename):
        production_list=[]
        with open(filename, newline='') as csvfile:
            for line in csvfile:
                production_list.append(line.strip().split())
            self._lecture_txt=production_list

    def create_Type_produit(self):
        list_Type_produit=[]
        for i in range (int(self._lecture_txt[0][0])):
            list_Type_produit.append(Type_produit(self._lecture_txt[i+1][0], int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]),int(self._lecture_txt[i+1][4]), int(self._lecture_txt[i+1][5]) ))
        self.box_manager._listes_types_produit=list_Type_produit

    def create_Commandes(self):
        list_Commande = []
        a = int(self._lecture_txt[0][0])
        b = int(self._lecture_txt[0][1])
        for i in range(a, a + b):
            list_produit=[]
            for j in range(4,len(self._lecture_txt[i+1])):
                list_produit.append(int(self._lecture_txt[i+1][j]))
            list_Commande.append(Commande(self._lecture_txt[i + 1][0], int(self._lecture_txt[i + 1][1]),
                                          int(self._lecture_txt[i + 1][2]), int(self._lecture_txt[i + 1][3]), list_produit))
        self._schedule._liste_commandes=list_Commande

    def create_Type_box(self):
        list_Type_box=[]
        a=int(self._lecture_txt[0][0])
        b=int(self._lecture_txt[0][1])
        c=int(self._lecture_txt[0][3])
        for i in range(a+b,a+b+c):
            list_Type_box.append(Type_box(self._lecture_txt[i+1][0], int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]) ))
        self.box_manager._listes_types_box=list_Type_box

    def create_Lignes(self):
        list_Lignes = []
        c = int(self._lecture_txt[0][2])
        for i in range(c):
            list_Lignes.append(Ligne(i))
        self._schedule._liste_lignes=list_Lignes

    def Ecriture_fichier(self):
        pass
    def Calcul_cout_retard(self):
        k=0
        m=self._schedule._liste_commandes
        for i in m:
            k=k+abs(i.dateReel-i.datePrevue)*i.penalite
        self._cout+=k
    def Calcul_cout_box(self):
        k=0
        for i in self._schedule._liste_commandes:
            for j in range(len(self.box_manager._listes_types_produit)):
                k=k+i.nbproduits[j]*self.box_manager._listes_types_produit[j].type_box.prix_box
        self._cout=self._cout+k


    def Calcul_cout_conteneur(self):
        pass

    def __init__(self):
        self._cout = 0
        self.box_manager=Box_manager()
        """# @AssociationMultiplicity 1"""
        self._schedule=Scheduling()
        """# @AssociationMultiplicity 1"""
        self._lecture_txt=None
