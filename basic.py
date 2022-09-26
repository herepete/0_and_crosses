#!/usr/bin/python3


line_all=["-","-","-","-","-","-","-","-","-"]
no_winner=0
computers_go=1

import random
import os
os.system('clear')
print ("Welcome to our game of 0 and X")

def game_template():
	print (line_all[0],end="")
	print ("  ",end="")
	print (line_all[1],end="")
	print ("  ",end="")
	print (line_all[2],end="")
	print ("  ")
	print (line_all[3],end="")
	print ("  ",end="")
	print (line_all[4],end="")
	print ("  ",end="")
	print (line_all[5],end="")
	print ("  ")
	print (line_all[6],end="")
	print ("  ",end="")
	print (line_all[7],end="")
	print ("  ",end="")
	print (line_all[8])


def game_winner_check():

	global no_winner

	if line_all[0]=="X" and line_all[1]=="X" and line_all[2]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[3]=="X" and line_all[4]=="X" and line_all[5]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[6]=="X" and line_all[7]=="X" and line_all[8]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[0]=="0" and line_all[1]=="0" and line_all[2]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[3]=="0" and line_all[4]=="0" and line_all[5]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[6]=="0" and line_all[7]=="0" and line_all[8]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[0]=="0" and line_all[3]=="0" and line_all[6]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[0]=="0" and line_all[3]=="0" and line_all[6]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[1]=="0" and line_all[4]=="0" and line_all[7]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[1]=="X" and line_all[4]=="X" and line_all[7]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[2]=="X" and line_all[5]=="X" and line_all[8]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[2]=="X" and line_all[5]=="X" and line_all[8]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[0]=="0" and line_all[4]=="0" and line_all[8]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[2]=="0" and line_all[4]=="0" and line_all[6]=="0":
		print ("Game winner")
		no_winner=1
	elif line_all[0]=="X" and line_all[4]=="X" and line_all[8]=="X":
		print ("Game winner")
		no_winner=1
	elif line_all[2]=="X" and line_all[4]=="X" and line_all[6]=="X":
		print ("Game winner")
		no_winner=1
	else:
		pass

def game_drawn_check():
	if "-" not in  line_all:
		print ("no places left to choose so a draw")
		no_winner=1
	

def computer_go():
	while True:
		line_all_rn=random.randint(0,8)
		#print (line_all_rn)
		if line_all[line_all_rn]=="-":
			line_all[line_all_rn]="X"
			break
			
		
while True:
	if computers_go==1:
		game_template()
		computer_go()
		print("===Computer Go===")
		game_template()
		computers_go=0
	else:
		user_choice=int(input("Which do you want your 0?"))
		if line_all[user_choice]=="-":
			print("===Your Go===")
			line_all[user_choice]="0"
			computers_go=1
		else:
			print ("Invliad chioce please try again")
	
	game_winner_check()
	if no_winner==1:
		print ("===Final board===")
		game_template()
		break
	game_drawn_check()
	if no_winner==1:
		print ("===Final board===")
		game_template()
		break
