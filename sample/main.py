# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:19:45 by mgross         #+#    #+#                 #
#    Updated: 2019/10/22 15:45:03 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse
import utillitie
import json
from state_machine import StateMachine

class InputConfig(object): #<-----moet hier object?
	''' Class from input json. ''' #<---------- beter omschrijven
	

	def __init__(self):	
		parser = argparse.ArgumentParser(description=None, usage='%(prog)s [-h] jsonfile input')
		parser.add_argument('filename', type=str, help='json description of the machine')
		parser.add_argument('input', type=str, help='input of the machine')
		args = parser.parse_args()
		with open(args.filename, 'r') as f:
			config = json.load(f)
			
		self.name = config['name']
		self.alphabet = config['alphabet']
		self.blank = config['blank']
		self.states = config['states']
		self.initial = config['initial']
		self.finals = config['finals']
		self.transitions = config['transitions']
		self.input = args.input

		f.close()

	def validat_initial(self):
		# print(1, self.states)
		if self.initial not in self.states:
			print('"Initial" state not found in list with states')
			exit()
		# print(2, self.states)

	def validate_finals(self):
		# print(1, self.states)		
		for elem in self.finals:
			if elem not in self.states:
				print('"Finals" state not found in list with states')
				exit()
		# print(2, self.states)		

	def validate_blank(self):
		# print(1, self.alphabet)
		if self.blank not in self.alphabet:
			print('"Blank" symbol not found in list alphabet')
			exit()
		
	def	validate_input(self):
		self.validat_initial()
		self.validate_finals()
		self.validate_blank()
	
		
if __name__ == '__main__':
	machine_config = InputConfig()
	machine_config.validate_input()
	turing_machine = StateMachine()
	turing_machine.add_input(machine_config.input)
	turing_machine.add_initial_state(machine_config.initial)
	print(turing_machine.initial_state)
	i = 0
	print(turing_machine.tape[i])
	i+=1
	print(turing_machine.tape[i])
	i-=1
	print(turing_machine.tape[i])
	# for elem in turing_machine.tape:
	# 	print(turing_machine.tape[it])
	# print(turing_machine.tape)

	# for i in machine_config.transitions[machine_config.states[2]]:
	# 	print(i)
	
	# print(machine_config.states)
	# print(machine_config.states)
	# length = len(machine_config.states)

	# for it in list(machine_config.transitions.keys()):
	# 	print(it)
	# 	for x in machine_config.transitions[it]:
	# 		print(x)


	# print(list(machine_config.transitions.keys()))
	# print(list(machine_config.transitions.values()))


