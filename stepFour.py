# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-09-17 13:21:41
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-09-20 15:47:58

#!/usr/local/bin/python3

from interface import *
from random import randint
from time import sleep
from datetime import date, datetime

test_four_player = [ {'position' : 0, 'charbon' : 24, 'or' : 1, 'id' : 0}, 
					{'position' : 0, 'charbon' : 5, 'or' : 1, 'id' : 1}, 
					{'position' : 0, 'charbon' : 5, 'or' : 1, 'id' : 2}, 
					{'position' : 0, 'charbon' : 1, 'or' : 0, 'id' : 3}]

nbJoueurs = 0
nbTours = 0
nbCases = 0

glb_lst_player = []
glb_board = []
glb_gold = 0

#just to slow the execution
glb_timer = 0.1

def gen_case():
	return randint(1,3)

def initalisationPlateau(nb_case):
	board  = []
	for i in range(nb_case):
		board.append(gen_case())
	print("the board ", board)
	return board

def gen_gold(nb_case, min):
	return randint(min, nb_case-1)

def free_program():
	effacePlateau()

def intialisationJoueurs(nb_player):
	x = 0
	lst_player = []
	for i in range(x, nb_player):
		lst_player.append({'position' : 0, 'charbon' : 5, 'or' : 0, 'id' : x})
		x += 1
	#to print all the player
	#print("list de dico des joueurs : ", lst_player)
	return lst_player



def checkNumberOfPlayers():
	nbJoueurs = -1
	while nbJoueurs < 0:
		nbJoueurs = inputUInt("Combien de joueurs (entre 1 et 4) voules vous ?\n-> ")
		if nbJoueurs < 1 or nbJoueurs > 4:
			print("-> nombre de joueurs incorecte : ce doit etre un nombre entre 1 et 4")
			nbJoueurs = -1
	return nbJoueurs 

def checkNumberOfTurn():
	nbTours = -1
	while nbTours < 0:
		nbTours = inputUInt("combien de tour de jeux voulez vous ? Un nombre qui doit etre au moins 1\n-> ")
		#if nbJoueurs >= 100:
		if nbTours < 1:
			print("-> nombre de tour incorecte : il doit etre au moins de 1")
			nbTours = -1
	return nbTours

def checkNumberOfCases():
	nbCases = -1
	while nbCases < 0:
		nbCases = inputUInt("Combien de case pour le plateau de jeux voulez vous ? ce doit etre un nombre entre 4 et 20 et doit etre divisible par 4\n-> ")
		if (nbCases % 4 != 0 or nbCases < 1 or nbCases > 20) and nbCases != -1:
			print("-> nombre de case incorecte : il doit etre plus grand que 0, inferieur a 20 et divisible par 4")
			nbCases = -1
	return nbCases

def inputUInt(question):
	nb = input(question)
	try : 
		nb = int(nb)
		return nb
	except ValueError:
		print("entrez un nombre corect",)
		return -1
			
def lanceDe(nbFaces):
	dice = randint(1, nbFaces)
	return dice

def check_same_position_gold_player():
	global glb_lst_player, glb_gold
	#for i in glb_lst_player:

def check_buy_gold():
	answer_possible_ok = ['Oui', 'Yes']
	answer_possible_not_ok = ['Non', 'No']
	check_answer = False
	while check_answer == False:
		answer = input("voulez vous acheter le lingot [Oui:Non]\n-> ")
		check_answer = answer in answer_possible_ok
		if check_answer == True:
			return True
		if check_answer == False:
			check_answer = answer in answer_possible_not_ok
			if check_answer == True:
				return False

def check_same_position_gold_player(lst_player, pos_gold):
	for i in lst_player:
		if i['position'] == pos_gold:
			return False
	return True

def replace_gold():
	global glb_lst_player, glb_gold, glb_board
	print("Pas sur de la position : \n", glb_lst_player, "\n", glb_gold)
	while check_same_position_gold_player(glb_lst_player, glb_gold) == False:
		glb_gold = positionGold(len(glb_board))
	placeOr(glb_gold, glb_board)

def acheteLingot(id_player):
	global glb_lst_player, glb_gold, glb_board
	#to print what the player has
	#print("vous avez : ", glb_lst_player[id_player]['charbon'], "charbon(s)")
	if glb_lst_player[id_player]['charbon'] < 10:
		print("vous n'avez pas suffisament de charbon, vous ne pouvez pas acheter le lingot :-/")
	else:
		if check_buy_gold():
			glb_lst_player[id_player]['or'] += 1
			glb_lst_player[id_player]['charbon'] -= 10
			replace_gold()

def effetCase(joueur, plateau):
	global glb_lst_player
	print("la case du plateau est :", plateau[glb_lst_player[joueur]['position']])
	if plateau[glb_lst_player[joueur]['position']] == 1: #green +3 
		glb_lst_player[joueur]['charbon'] += 3
		print("le joueur : ", glb_lst_player[joueur], "a gagné 3 charbon")
	elif plateau[glb_lst_player[joueur]['position']] == 2: #red -3 
		glb_lst_player[joueur]['charbon'] -= 3
		if glb_lst_player[joueur]['charbon'] < 0:
			glb_lst_player[joueur]['charbon'] = 0
		print("le joueur : ", glb_lst_player[joueur], "a perdu 3 charbon")
	#elif plateau[glb_lst_player[joueur]['position']] == 3: #blue nothing

def timer(tm):
	sleep(tm)

# joueur -> if of the player
# nbCases -> number of case to moove
# plateau -> list of the case of the plate
def deplaceJoueur(joueur, nbCases, plateau):
	global nbTours, nbJoueurs
	global glb_lst_player, glb_gold
	global glb_timer
	print("in deplaceJoueur function : ", len(plateau), " player n° ", joueur, " number of case to moove : ", nbCases)
	for i in range(nbCases):
		glb_lst_player[joueur]['position'] += 1
		#to go back to the start case
		if glb_lst_player[joueur]['position'] >= len(plateau):
			glb_lst_player[joueur]['position'] = 0
		bougeJoueur(glb_lst_player[joueur], plateau)
		#if on gold during mooving
		if glb_lst_player[joueur]['position'] == glb_gold:
			acheteLingot(joueur)
		timer(glb_timer)


def tourJoueur(joueur, plateau):
	#print("-> player ", glb_lst_player[id_lst]['id'], "to play")
	print("-> player ", joueur['id'], "to play")
	dice_result = lanceDe(6)
	print("result of the dice\n-> : ", dice_result)
	deplaceJoueur(joueur['id'], dice_result, plateau)
	#event according to the case when the player stop
	effetCase(joueur['id'], plateau)

#joueurs -> list of the player
def tourDeJeu(joueurs):
	global glb_board
	for i in joueurs:
		tourJoueur(i, glb_board)

#nbTours -> number of turn
#joueurs -> list of the player
def partie(nbTours, joueurs):
	global glb_lst_player, glb_board, glb_gold
	print("the game loop")
	for j in range(nbTours):
		print("tour : ", j)
		tourDeJeu(glb_lst_player)

def positionGold(nbCases):
	return gen_gold(nbCases, 0)

def configuration():
	global nbTours
	global nbJoueurs
	global nbCases
	nbJoueurs = checkNumberOfPlayers()
	nbTours = checkNumberOfTurn()
	nbCases = checkNumberOfCases()

def initialisation():
	global nbTours, nbJoueurs, nbCases
	global glb_lst_player, glb_board, glb_gold
	glb_lst_player = intialisationJoueurs(nbJoueurs)
	glb_board = initalisationPlateau(nbCases)
	glb_gold = positionGold(nbCases)
	creePlateau(glb_board)
	creeJoueurs(glb_lst_player, glb_board)
	placeOr(glb_gold, glb_board)


def compStuff(stuff1, stuff2):
	if stuff1 > stuff2:
		return 1
	elif stuff1  < stuff2:
		return -1
	return 0

def compJoueurs(joueur1, joueur2):
	char = compStuff(joueur1['charbon'], joueur2['charbon']) 
	gold = compStuff(joueur1['or'], joueur2['or'])
	if gold == 1: 
		return 1
	elif gold == 0:
		if char == 1:
			return 1
		if char == 0 and gold == 0:
			return 0
	return -1

def print_player_list(lst):
	print("la liste des joueus :")
	for i in lst:
		print(i['id'], " -> ", i)
	print("---------------------------------")

def order_player(lst_player):
	rtr = 0
	if len(lst_player) <= 1:
		return True
	i = 0
	while i < len(lst_player)-1:
		rtr = compJoueurs(lst_player[i], lst_player[i+1])
		if rtr == 1:
			first = lst_player.pop(i)
			second = lst_player.pop(i)
			lst_player.insert(i, first)
			lst_player.insert(i, second)
			i = 0
		else :
			i += 1

#Numéro  3  : Joueur  3  avec  0  lingot(s) d'or et  3 charbon(s)
def afficheClassement(joueurs):
	today = date.today()
	nb_player = len(joueurs)
	for i in joueurs:
		print("Numéro " + str(nb_player) + "  : Joueur  " + str(i['id']+1) + "  avec  " + str(i['or']) + "  lingot(s) d'or et  " + str(i['charbon']) + " charbon(s)")
		nb_player -= 1

def open_a_file(file_name):
	try:
		fd = open(file_name, 'w')
		return fd
	except  :
		print("an error occured when opening/creating the file")
		return -1

def sauvegardeResultats(joueurs):
	today = datetime.today()
	nb_player = len(joueurs)
	file_name = "chariot-party-" + '{:02d}'.format(today.day) + "-" + '{:02d}'.format(today.month) + "-" + str(today.year) + "-" + '{:02d}'.format(today.hour) + "-" + '{:02d}'.format(today.minute) + ".txt"
	grading = ""
	for i in joueurs:
		grading += "Numéro " + str(nb_player) + "  : Joueur  " + str(i['id']+1) + "  avec  " + str(i['or']) + "  lingot(s) d'or et  " + str(i['charbon']) + " charbon(s)" + '\n'
		nb_player -= 1	
	fd = open_a_file(file_name)
	if fd != -1:
		fd.write(grading)
		fd.close()
	

def main():
	global nbTours, nbJoueurs
	global glb_lst_player, glb_board, glb_gold

	configuration()
	initialisation()
	partie(nbTours, glb_lst_player)

	order_player(glb_lst_player)
	afficheClassement(glb_lst_player)
	sauvegardeResultats(glb_lst_player)
	
	free_program()

main()
