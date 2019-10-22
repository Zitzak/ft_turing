# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:19:45 by mgross         #+#    #+#                 #
#    Updated: 2019/10/22 18:06:56 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
import utillitie
import json
from state_machine import StateMachine
from utillitie import get_args

class InputConfig(object): #<-----moet hier object?
	''' Class from input json. ''' #<---------- beter omschrijven
	
	def __init__(self):
		''' Init class with input variables'''
		
		self.name = ""
		self.alphabet = []
		self.blank = ""
		self.states = []
		self.initial = ""
		self.finals = []
		self.transitions = {}


	def get_input(self, args):
		''' hier moet nog teskt'''
		with open(args.filename, 'r') as f:
			try:
				config = json.load(f)
			except:
				print('Error - No .json file.')
				f.close()
				sys.exit()
		self.check_for_name(config, "name")
		self.check_for_alphabet(config, "alphabet")
		self.check_for_blank(config, "blank")
		self.check_for_states(config, "states")
		self.check_for_initial(config, "initial")
		self.check_for_finals(config, "finals")
		self.check_for_transitions(config, "transitions")
		self.input = args.input
		f.close()
	
	def	check_for_name(self, config, string):
		''' Check if "name is in the .json file and if so, assign it'''
		try:
			self.name = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_alphabet(self, config, string):
		''' Check if "alphabet" is in the .json file and if so, assign it'''
		try:
			self.alphabet = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_blank(self, config, string):
		''' Check if "blank" is in the .json file and if so, assign it'''
		try:
			self.blank = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_states(self, config, string):
		''' Check if "states" is in the .json file and if so, assign it'''
		try:
			self.states = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_initial(self, config, string):
		''' Check if "initial" is in the .json file and if so, assign it'''
		try:
			self.initial = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_finals(self, config, string):
		''' Check if "finals" is in the .json file and if so, assign it'''
		try:
			self.finals = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_transitions(self, config, string):
		''' Check if "transitions" is in the .json file and if so, assign it'''
		try:
			self.transitions = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def validat_initial(self):
		if self.initial not in self.states:
			print('Error - "Initial" state not found in list with states')
			exit()

	def validate_finals(self):
		for elem in self.finals:
			if elem not in self.states:
				print('Error - "Finals" state not found in list with states')
				exit()

	def validate_blank(self):
		if self.blank not in self.alphabet:
			print('Error - "Blank" symbol not found in list alphabet')
			exit()
		
	def	validate_input(self):
		self.validat_initial()
		self.validate_finals()
		self.validate_blank()

		
if __name__ == '__main__':
	machine_config = InputConfig()
	machine_config.get_input(get_args())
	machine_config.validate_input()
	turing_machine = StateMachine()
	turing_machine.add_tape(machine_config.input)
	turing_machine.add_initial_state(machine_config.initial)
	print("name: ", machine_config.name)
	print("alphabet: ", machine_config.alphabet)
	print("blank: ", machine_config.blank)
	print("states: ", machine_config.states)
	print("initial: ", machine_config.initial)
	print("finals: ", machine_config.finals)
	for it in list(machine_config.transitions.keys()):
		print(it)
		for x in machine_config.transitions[it]:
			print(x)
	print(turing_machine.tape)
	# print(turing_machine.initial_state)
	# i = 0
	# print(turing_machine.tape[i])
	# i+=1
	# print(turing_machine.tape[i])
	# i-=1
	# print(turing_machine.tape[i])
	# for elem in turing_machine.tape:
	# 	print(turing_machine.tape[it])

	# for i in machine_config.transitions[machine_config.states[2]]:
	# 	print(i)
	
	# print(machine_config.states)
	# print(machine_config.states)
	# length = len(machine_config.states)



	# print(list(machine_config.transitions.keys()))
	# print(list(machine_config.transitions.values()))


