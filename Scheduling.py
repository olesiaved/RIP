#!/usr/bin/python
# -*- coding: UTF-8 -*-
from operator import attrgetter

from Box_manager import Box_manager

# classe de gestion des production de toutes les commandes, produits, attribution de box et gestion des boxs
# 2nd classe principale après la classe Production
class Scheduling(object):

	def __init__(self):
		self._liste_commandes = []			# liste de l'ensemble des commandes à gérer
		"""# @AssociationMultiplicity 1..*"""
		"""# @AssociationMultiplicity 1..*"""
		self._liste_lignes = []				# liste de lignes de de production à disposition
		"""# @AssociationMultiplicity 1..*"""
		self.box_manager = Box_manager()	# gestion du parc de box (achats, attribution des produits dans les boxs, réutilisation...)
		"""# @AssociationMultiplicity 1"""

	# Lancement du tri
	def InitialasiationTri(self):
		self.TriProduit(self._liste_commandes)

	# production de tous les produits après attribution sur une ligne(=mise à jour date de prod)
	def calcul_date_prod(self):
		for i in self._liste_lignes:
			i.calcul_date_produit_opt()



	# attribution des produits de l'ensemble des commandes sur les lignes de production
	def TriProduit(self,ListTypeProd):
		# Etape 1 : ordonancement des commandes entre elles en fonction du ratio datePrevue / CoutJourRetard
		# cf rapport RIP partie III. B.

		# Etape 2 : ajustement de l'ordonnancement en #1 : rejet en dernières positions des commandes au coût journalier de retard négligeable
		# cf rapport RIP partie III. B.

		# Etape 3 : répartition des produits de toutes les commandes  (sur les lignes de prod) dans l'ordre de traitement choisi en #2


		ListTypeProd = self.box_manager._listes_types_produit	# liste des types de produits existants
		ListTraitementCommande = []								# liste des commandes à traiter ordonnancées après #1
		ListTraitementCommandeFinal = []						# liste des commandes à traiter ordonnanceées après #3



		# Etape 1 : ordonancement des commandes entre elles en fonction du ratio datePrevue / CoutJourRetard
		while (len(ListTraitementCommande) < len(self._liste_commandes)):
			LocalVar = -1
			minimumLoc = self._liste_commandes[0]
			ii = None

			for i in (self._liste_commandes):
				if (i not in ListTraitementCommande):
					if (LocalVar == -1):
						minimumLoc = i
						LocalVar = 0

					elif (i._datePrevue/(i._penalite+0.01))<= (minimumLoc._datePrevue/(minimumLoc._penalite+0.01)):
						minimumLoc = i

			ListTraitementCommande.append(minimumLoc)
			# Etape 2 : ajustement de l'ordonnancement en #1 par placement en dernières positions des commandes
			# au cout journalier de retard "négligeable"
			#
			# attribution des commandes dans l'ordre dans le tableau ListTraitementCommandeFinal

			# négligeable <=> CoutJourRetard < CoutRetardMoyen

			# Etape 2.0 : calcul du prix moyen des couts d'une journée de pénalité pour toutes les commandes
			somlocalprix=0

		for element in ListTraitementCommande:
			somlocalprix+=i._penalite

		prixmoyendelais = somlocalprix / len(ListTraitementCommande)

		# Etape 2.1 : comparaison des couts journalier de retard de chaque commande au cout journalier de retard moyen
		for ii in range(len(ListTraitementCommande)):
			if (ListTraitementCommande[ii] not in ListTraitementCommandeFinal):
				if (ListTraitementCommande[ii]._penalite > prixmoyendelais / 1):
					ListTraitementCommandeFinal.append(ListTraitementCommande[ii])

		for iii in range(len(ListTraitementCommande)):
			if (ListTraitementCommande[iii] not in ListTraitementCommandeFinal):
				if (ListTraitementCommande[iii]._penalite <= prixmoyendelais / 1):
					ListTraitementCommandeFinal.append(ListTraitementCommande[iii])

		# Etape 3 : traitement de toutes les commandes dans l'ordre précédement définit
		for p in ListTraitementCommandeFinal:
			self.FastestLineGivenOrder(p, ListTypeProd)

		self.AffichageEtatLignes()


	def FastestLineGivenOrder(self,CommandeTraitee,ListTypeProd):
		# ORDER = variable qui contient les commandes
		TypePreviousProd = None
		PreviousLine = None

	# on considère les commandes dans l'ordre précedemment défini
	# les produits de même type au sein de la commande considérée sont traités ensemble

	# ex: si dans la commande 12 il y a 45 prod type A 		34 prod type B 		63 prod type C
	# tous les produits A seront d'abord attribués sur les lignes puis type B puis type C

	# le produit dont "c'est le tour" est attribué à une ligne de prod directement ou indirectement
	# en fonction des différents cas de figure détaillés par la suite

	# Soit un type de produit considéré
		for pdtype in ListTypeProd:

			#selection des produit de la commandes du type considéré
			for products in CommandeTraitee._liste_produits_afaire:
				if(products._type==pdtype):

					# + Si le produit considéré n'est pas le premier à être traité de la commande considéré
					if(PreviousLine!=None):

						# 2 cas de figures : le produit considéré et celui produit juste avant sont de même type /// ne le sont pas

						# si le type du produit précédement fabriqué est le même que celui du produit actuellement considéré:
						if(TypePreviousProd != None):
							if(TypePreviousProd == products._type):


							# 2 cas de figures : ajouter ce produit à la même ligne de prod que le produit précédent
							# permet de respecter les delais attendus?



							#si oui : ajout du produit ici considéré à la ligne où le produit d'avant a été attribué
								if (PreviousLine.LocalDelay + products._type.p <= ORDER._datePrevue ):
									PreviousLine.AddProdAfaire(products)


							# sinon : ajout du produit ici considéré à la ligne où le delais est le plus faible
								elif (PreviousLine.LocalDelay + products._type.p > ORDER._datePrevue):
									PreviousLine = self.FastestLineGivenProduct(products)

						# Si le produit actuellement considéré est de type différent de celui d'avant : choisir la ligne avec le delais minimum
							elif(TypePreviousProd != products._type):
								PreviousLine = self.FastestLineGivenProduct(products)

				# Si aucun produit de même type n'a précédement été fabriqué :  choisir la ligne avec le delais minimum
						else:
							PreviousLine = self.FastestLineGivenProduct(products)

					else:
						PreviousLine =self.FastestLineGivenProduct(products)


				TypePreviousProd=products._type



# méthode choix de la ligne où le delais est plus court
	def FastestLineGivenProduct(self, PRODTEST):
		BestDelayLine = None
		LigneReference= None

		for LocalLigne in self._liste_lignes:
		# CALCUL DU  NOUVEAU DELAIS EN CAS D'AJOUT DU PRODUIT CONSIDERE SUR LA LIGNE TESTEE
			if(LocalLigne.LastestProdAdded==PRODTEST._type):
				# si pas de temps de set up
				LocalDelayLine = LocalLigne.LocalDelay + PRODTEST._type.p

			elif (LocalLigne.LastestProdAdded != PRODTEST._type):
				# si temps de set up
				LocalDelayLine = LocalLigne.LocalDelay + PRODTEST._type.p + PRODTEST._type.s


		# COMPARAISON DE TOUS LES DELAIS THEORIQUES EN CAS D'AJOUT, COMPARAISON, CHOIX
			if(BestDelayLine!=None):
				if((LocalDelayLine<BestDelayLine) or (LigneReference==None)):
					BestDelayLine=LocalDelayLine
					LigneReference=LocalLigne

			elif(BestDelayLine==None):
				BestDelayLine = LocalDelayLine
				LigneReference = LocalLigne


		#Ajoue du produit sur la ligne
		LigneReference.AddProdAfaire(PRODTEST)

		#le retour sert à mettre à jour la ligne où a été produit le dernier produit
		return LigneReference





	def AffichageEtatCommande(self):
		for element in self._liste_commandes:
			element.affichage()

	def AffichageEtatLignes(self):
		for element in self._liste_lignes:
			element.affichage()





# Calcul de la date réelle d'envoie pour chaque commande
#basée sur la classe ligne
	def date_fin_prod(self):
		for element in self._liste_commandes:
			element.DateEnvoieFin()




#attribution de produits dans les boxs après production
	def recherche_date_suivante(self):
		liste_date_envoie = []
		for i in self._liste_commandes:
			liste_date_envoie.append(i._dateReel)

		liste_date_envoie.sort()

		date = 0
		stop = False
		y = 0
		while (stop == False):
			liste = []

			for o in self._liste_commandes:
				if o._dateReel == liste_date_envoie[y]:
					com = o
			if date >= liste_date_envoie[y]:
				for h in self._liste_commandes:
					if h._dateReel == liste_date_envoie[y]:
						self.box_manager.Vider_box_commande_envoye(h)

				y = y + 1

			for i in self._liste_lignes:
				liste.append(i.recherche_date_suivante(date))
				liste = list(filter(None, liste))
			if liste != []:
				min = liste[0]
				for k in liste:
					if k._dateFinProd < min._dateFinProd:
						min = k

				self.box_manager.gestion_produit_finis(min)

				date = min._dateFinProd
			else:
				stop = True





