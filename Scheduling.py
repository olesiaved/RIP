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

	# production de toutes les produits après attribution sur une ligne
	def calcul_date_prod(self):
		for i in self._liste_lignes:
			i.calcul_date_produit_opt()



	# attribution des produits de l'ensemble des commandes sur les lignes de production
	def TriProduit(self,ListTypeProd):
		# Etape 1 : ordonancement des commandes entre elles en fonction des dates attendues les plus proches
		# Etape 2 : ordonancement des commandes entre elles en fonction de leur date attendues et des couts en cas de retard (méthode détaillée par la suite)
		# Etape 3 : répartition des produits de la 1e commande à traiter sur les lignes de prod (méthode détaillée par la suite)
		# Etape 4 : répartition des produits de toutes les commandes  (sur les lignes de prod) dans l'ordre

		ListTypeProd = self.box_manager._listes_types_produit	# liste des types de produits existants
		ListTraitementCommande = []								# liste des commandes à traiter ordonnancées en fonction de leurs date de prod
		ListTraitementCommandeFinal = []						# liste des commandes à traiter ordonnancement final (méthode développée par la suite)



		# Etape 1 : ordonancement des commandes entre elles en fonction des dates attendues les plus proches
		# attribution des commandes dans la variable ListTraitementCommande
		while (len(ListTraitementCommande) < len(self._liste_commandes)):
			LocalVar = -1
			minimumLoc = self._liste_commandes[0]
			ii = None

			for i in (self._liste_commandes):
				if (i not in ListTraitementCommande):
					if (LocalVar == -1):
						minimumLoc = i
						LocalVar = 0

					elif (1/((1/i._datePrevue)*(i._penalite+0.01))<= 1/((1/minimumLoc._datePrevue)*(minimumLoc._penalite+0.01))):
						minimumLoc = i

			ListTraitementCommande.append(minimumLoc)
			# Etape 2 : ordonancement des commandes entre elles en fonction de leur date attendues et des couts en cas de retard
			# attribution des commandes dans la variable ListTraitementCommandeFinal

			#objectif de la méthode :
			# faire les commandes couteuses en premiers (prise en compte du delais à dispo et du cout en cas de retard)


			#méthode d'ordonancement :
			#1 : considération des commandes dans l'ordre par date attendue la plus proche

			#2 : Soit la commande en i-ème position dans l'odre initial:
			# si le cout en cas de retard de cette commande et inférieur à :  0.5 * cout moyen en cas de retard
			# alors cette commande est considérée comme "d'impact négligeable en cas de retard"
			#
			#elle est de fait placée à la fin de la liste d'ordre de traitement des commandes

			# exemple : passage de 1 2 3 4 5 6 7 à 1 2 4 7 3 5 6




			#calcul du prix moyen des couts d'une journée de pénalité pour toutes les commandes
			prixmoyendelais=0
			somlocalprix=0

		for element in ListTraitementCommande:
			somlocalprix+=i._penalite
			#element.affichage()
			print('\n')

		prixmoyendelais = somlocalprix / len(ListTraitementCommande)

		# comparaison des couts en cas de retard de chaque commande au cout de retard moyen
		for ii in range(len(ListTraitementCommande)):
			if (ListTraitementCommande[ii] not in ListTraitementCommandeFinal):
				if (ListTraitementCommande[ii]._penalite > prixmoyendelais / 1):
					ListTraitementCommandeFinal.append(ListTraitementCommande[ii])

		for iii in range(len(ListTraitementCommande)):
			if (ListTraitementCommande[iii] not in ListTraitementCommandeFinal):
				if (ListTraitementCommande[iii]._penalite <= prixmoyendelais / 1):
					ListTraitementCommandeFinal.append(ListTraitementCommande[iii])

		# traitement de toutes les commandes dans l'ordre précédement définit par la méthode FastestLineGivenOrder détaillée par la suite
		for p in ListTraitementCommandeFinal:
			self.FastestLineGivenOrder(p, ListTypeProd)

		self.AffichageEtatLignes()


	def FastestLineGivenOrder(self,ORDER,ListTypeProd):
		TypePreviousProd = None
		PreviousLine = None

	# les produits ne sont  pas produits ici ils sont attribués sur les lignes de prod.

	# on considère une commande dans l'ordre précedemment définie
	# les produits de même type au sein de la commande considérée sont traités ensemble

	# ex: si dans la commande 12 il y a 45 prod type A 		34 prod type B 		63 prod type C
	# tous les produits A seront d'abord attribués sur les lignes puis type B puis type C

	# le produit dont "c'est le tour" est attribués à une ligne de prod directement ou indirectement (méthode FastestLineGivenProduct)
	# en fonction des différents cas de figure

	#méthode FastestLineGivenProduct : attribue le produit donné à la ligne où le delais sera le plus cours après attribution
	# (sans considération du délais global) avec prise en compte du temps de changement d'outil


	# Soit un type de produit considéré
		for pdtype in ListTypeProd:

			#choix d'un produit de la ligne
			for products in ORDER._liste_produits_afaire:

				# si le produit considéré de la commande est du type donné on le considère maintenant sinon tour suivant
				if(products._type==pdtype):

					# + Si le produit considéré n'est pas le premier attribué de la commande considéré
					if(PreviousLine!=None):

						# 2 cas de figures : le produit considéré et celui produit juste avant sont de même type
						# ils sont de même type

						# si le type du produit précédent est le même du produit actuellement considéré:
						if(TypePreviousProd != None):
							if(TypePreviousProd == products._type):

							# 2 cas de vigures : ajouter ce produit à la ligne de prod du produit précédent (de même type)
							# permet de respecter les delais attendus?



							#si oui : ajout du e produit ici considéré à la ligne où le produit d'avant a été attribué
								if (PreviousLine.LocalDelay + products._type.p <= ORDER._datePrevue ):
									PreviousLine.AddProdAfaire(products)


							# sinon : ajout du produit ici considéré à la ligne où le delais est le plus faible
								elif (PreviousLine.LocalDelay + products._type.p > ORDER._datePrevue):
									PreviousLine = self.FastestLineGivenProduct(products)

						# Si le produit actuellement considéré est de type différent de celui d'avant : choisir la ligne avec le delais minimum
							elif(TypePreviousProd != products._type):
								PreviousLine = self.FastestLineGivenProduct(products)

				# Si aucun produit de même type n'a précédement été fait :  choisir la ligne avec le delais minimum
						else:
							PreviousLine = self.FastestLineGivenProduct(products)

					else:
						PreviousLine =self.FastestLineGivenProduct(products)


				TypePreviousProd=products._type




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


		# COMPARAISON DE TOUS LES DELAIS THEORIQUES EN CAS D'AJOUE, COMPARAISON, CHOIX
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

	def date_fin_prod(self):
		for element in self._liste_commandes:
			element.DateEnvoieFin()




#méthode utilisé pour l'attribution de produits dans les boxs après production
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





