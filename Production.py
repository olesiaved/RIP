#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Box_manager 
import Scheduling
import Commande
import os
import csv

class Production(object):
    def Calcul_cout_delay(self, aCmd : Commande):
        pass

    def Lecture_fichier(self):
        display_list=[]
        with open(r"C:\Users\lesya\OneDrive\Documents\Etudes\s2\RIP\Donnee.txt", newline='') as csvfile:
            for line in csvfile:
                display_list.append(line.strip().split(';'))
            print(display_list)


            

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

if __name__ == '__main__':
    pr=Production()
    pr.Lecture_fichier()