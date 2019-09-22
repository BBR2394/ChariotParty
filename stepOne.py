# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-09-17 13:21:41
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-09-22 23:06:25

#! /usr/local/bin/python3

from interface import *
import random

step_one_plate = [1, 1, 3, 3, 3, 2, 1, 3, 3, 1, 2, 3, 3, 3, 3, 1, 3, 3, 3, 3]
step_one_player = [ {'position' : 3, 'charbon' : 4, 'or' : 0, 'id' : 0}, 
					{'position' : 8, 'charbon' : 10, 'or' : 0, 'id' : 1}, 
					{'position' : 16, 'charbon' : 3, 'or' : 1, 'id' : 2}, 
					{'position' : 7, 'charbon' : 0, 'or' : 0, 'id' : 3}]

def game_loop():
	input("click enter to end the program")

def free_program():
	effacePlateau()

def step_one():
	creePlateau(step_one_plate)
	creeJoueurs(step_one_player, step_one_plate)
	placeOr(24, step_one_plate)
	game_loop()
	free_program()

step_one()
