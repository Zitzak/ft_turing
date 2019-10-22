# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:19:45 by mgross         #+#    #+#                 #
#    Updated: 2019/10/22 23:02:19 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import json
from state_machine import TuringMachine
from utillitie import get_args
from utillitie import print_machine_config

class InputConfig(object):
	''' Class for input from json. ''' 
	
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
		''' Reads file and calls functions for assigning input'''

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
		self.input = args.input + "." * (len(args.input) * 2)
		f.close()
	
	def	check_for_name(self, config, string):
		''' Check if "name is in the .json file and if so, assign it.'''

		try:
			self.name = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_alphabet(self, config, string):
		''' Check if "alphabet" is in the .json file and if so, assign it.'''

		try:
			self.alphabet = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_blank(self, config, string):
		''' Check if "blank" is in the .json file and if so, assign it.'''

		try:
			self.blank = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_states(self, config, string):
		''' Check if "states" is in the .json file and if so, assign it.'''

		try:
			self.states = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_initial(self, config, string):
		''' Check if "initial" is in the .json file and if so, assign it.'''

		try:
			self.initial = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_finals(self, config, string):
		''' Check if "finals" is in the .json file and if so, assign it.'''

		try:
			self.finals = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def	check_for_transitions(self, config, string):
		''' Check if "transitions" is in the .json file and if so, assign it.'''

		try:
			self.transitions = config[string]
		except:
			print('Error - No {} field in .json file.' .format(string))
			sys.exit()

	def validat_initial(self):
		''' Checks for valid input in states.'''

		if self.initial not in self.states:
			print('Error - "Initial" state not found in list with states')
			exit()

	def validate_finals(self):
		''' Checks for valid input in finals.'''

		for elem in self.finals:
			if elem not in self.states:
				print('Error - "Finals" state not found in list with states')
				exit()

	def validate_blank(self):
		''' Checks for valid input in alphabet.'''

		if self.blank not in self.alphabet:
			print('Error - "Blank" symbol not found in list alphabet')
			exit()
		
	def	validate_input(self):
		''' Redirect to validation functions.'''
		self.validat_initial()
		self.validate_finals()
		self.validate_blank()

		
if __name__ == '__main__':
	machine_config = InputConfig()
	machine_config.get_input(get_args())
	machine_config.validate_input()
	turing_machine = TuringMachine()
	turing_machine.add_tape(machine_config.input)
	turing_machine.update_current_state(machine_config.initial)
	turing_machine.add_transitions(machine_config.transitions)
	turing_machine.add_final_states(machine_config.finals)
	turing_machine.add_blank(machine_config.blank)
	print_machine_config(machine_config)

	while turing_machine.current_state not in turing_machine.finals:
		turing_machine.between_states()
