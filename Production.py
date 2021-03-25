#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Box_manager import Box_manager
from Scheduling import Scheduling
from Commande import Commande
from Type_produit import Type_produit
from Ligne import Ligne
from Type_box import Type_box
from Produit import Produit

#NEWNEWNEW
class Production(object):
    def simulation_production(self,filename):
        self.Lecture_fichier(filename)
        self.create_Lignes()
        self.create_Type_box()
        self.create_Type_produit()
        self.create_Commandes()
        self._schedule.box_manager.Attribution_type()
        self._schedule.InitialasiationTri()
        self._schedule.calcul_date_prod()
        self._schedule.numero_box_pour_produit()
        self._schedule.date_fin_prod()
        self.Calcul_cout_retard()
        self.Calcul_cout_box()
        print(self._cout)

    def __init__(self):
        self._cout = 0

        self._schedule = Scheduling()
        """# @AssociationMultiplicity 1"""
        self._lecture_txt = None

    def Lecture_fichier(self,filename):
        production_list=[]
        with open(filename, newline='') as csvfile:
            for line in csvfile:
                production_list.append(line.strip().split())
            self._lecture_txt=production_list

    def EcritureResult(self, filename):

        file_name = filename
        print(file_name)
        index = file_name.index('.txt')
        file_name = file_name[:index]
        file_name = file_name + ".sol"
        f = open(file_name, "w")
        f = open(file_name, "a")
        f.write(str(self._cout))
        f.write('\n')

        for i in range(len(self._schedule.box_manager._listes_box)):
            f.write(str(self._schedule.box_manager._listes_types_box[i].type)+" "+str(self._schedule.box_manager._listes_box[i]))
            f.write('\n')

        for element in self._schedule._liste_commandes:
            f.write(str(element._id) + " " + str(element._dateReel))
            f.write('\n')


        for elt in self._schedule._liste_commandes:
            for elt2 in elt._liste_produits_finis :
                f.write(str(elt._id) + " " +str(elt2._type.id)+" "+str(elt._num_ligne)+" "+str(elt2._dateFinProd)+" "+str(str(elt2._type.type_box.type))+" "+str(elt2._num_box))
                f.write('\n')




    def create_Type_produit(self):
        list_Type_produit=[]
        for i in range (int(self._lecture_txt[0][0])):
            list_Type_produit.append(Type_produit(self._lecture_txt[i+1][0], int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]),int(self._lecture_txt[i+1][4]), int(self._lecture_txt[i+1][5]) ))
        self._schedule.box_manager._listes_types_produit=list_Type_produit



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

        self._schedule._liste_commandes = list_Commande

        """COMMANDE créées avant cette ligne mais laissées vides (en terme de produit)
        Commande remplie ci-dessous (grâce à la création de l'ensemble des produits composants de la commande):"""

        for cc in range(len(self._schedule._liste_commandes)):

            for aa in range(len(self._schedule.box_manager._listes_types_produit)) :

                for bb in range(self._schedule._liste_commandes[cc]._list_prod[aa]) :

                    self._schedule._liste_commandes[cc]._liste_produits_afaire.append(Produit(self._schedule._liste_commandes[cc]._id,(self._schedule.box_manager._listes_types_produit[aa])))






    def create_Type_box(self):
        list_Type_box=[]
        a=int(self._lecture_txt[0][0])
        b=int(self._lecture_txt[0][1])
        c=int(self._lecture_txt[0][3])
        for i in range(a+b,a+b+c):
            list_Type_box.append(Type_box(self._lecture_txt[i+1][0], int(self._lecture_txt[i+1][1]),int(self._lecture_txt[i+1][2]),int(self._lecture_txt[i+1][3]) ))
        self._schedule.box_manager._listes_types_box=list_Type_box

    def create_Lignes(self):
        list_Lignes = []
        c = int(self._lecture_txt[0][2])
        for i in range(c):
            list_Lignes.append(Ligne(i))
        self._schedule._liste_lignes=list_Lignes


    def Calcul_cout_retard(self):
        k=0
        m=self._schedule._liste_commandes
        for i in m:
            k=k+abs(i._dateReel-i._datePrevue)*i._penalite
        self._cout+=k


    def Calcul_cout_box(self):
        k=0
        for i in self._schedule._liste_commandes:
            for j in range(len(self._schedule.box_manager._listes_types_produit)):
                k=k+i._list_prod[j]*self._schedule.box_manager._listes_types_produit[j].type_box.prix_box
        self._cout=self._cout+k

