# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    TuringMachine.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 11:48:52 by mgross         #+#    #+#                 #
#    Updated: 2019/10/25 14:52:58 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import copy
import sys
from argparser import ArgumentParser

class TuringMachine(object):
	
	def	__init__(self, args):
		''' Init vars in TuringMachine.'''
		
		try:
			self.name = args.machine_config['name']
		except:
			print('Error - No name field in .json file.')
			sys.exit()
		try:
			self.alphabet = args.machine_config['alphabet']
		except:
			print('Error - No alphabet field in .json file.')
			sys.exit()
		try:
			self.blank = args.machine_config['blank']
		except:
			print('Error - No blank field in .json file.')
			sys.exit()
		try:
			self.states = args.machine_config['states']
		except:
			print('Error - No states field in .json file.')
			sys.exit()
		try:
			self.initial = args.machine_config['initial']
		except:
			print('Error - No initial field in .json file.')
			sys.exit()
		try:
			self.finals = args.machine_config['finals']
		except:
			print('Error - No finals field in .json file.')
			sys.exit()
		try:
			self.transitions = args.machine_config['transitions']
		except:
			print('Error - No transitions field in .json file.')
			sys.exit()

		if self.blank not in self.alphabet:
			print('Error - "Blank" symbol not found in list alphabet')
			sys.exit()
		
		for elem in self.finals:
			if elem not in self.states:
				print('Error - "Finals" state not found in list with states')
				sys.exit()

		if self.initial not in self.states:
			print('Error - "Initial" state not found in list with states')
			sys.exit()

		for key in self.transitions:
			for elem in self.transitions[key]:
				if elem['read'] not in self.alphabet:
					print('Error - wrong "read" symbol in transition->{} machine configuration' .format(key))
					sys.exit()
				if elem['write'] not in self.alphabet:
					print('Error - wrong "write" symbol in transition->{} machine configuration' .format(key))
					sys.exit()
		# 	for value in self.transitions[key]['read']:
		# 		print(value)
		# print(self.transitions['subone']['read'])
	# def add_tape(self, tape):
	# 	''' Adds tape.'''

	# 	self.tape = list(tape)

	# def	add_transitions(self, transitions):
	# 	''' Adds transitions.'''

	# 	self.transitions = transitions

	# def add_final_states(self, finals):
	# 	'''Adds final states and adds "REJECT" state.'''

	# 	if "REJECT" not in finals:
	# 		finals = finals + ["REJECT"]
	# 	self.finals = copy.copy(finals)

	# def add_blank(self, blank):
	# 	'''Adds blank char.'''
		
	# 	self.blank = blank

	# def update_current_state(self, new_state):
	# 	'''Update current state.'''

	# 	self.current_state = new_state

	# def read_symbol(self):
	# 	'''Reads symbole form tape.'''

	# 	self.current_symbol = self.tape[self.head_index]

	# def write_symbol(self, index):
	# 	'''Writes symbol to tape.'''
	# 	self.tape[self.head_index] = self.transitions[self.current_state][index]['write']
	
	# def	move_head(self, index):
	# 	''' Moves the head_index.'''

	# 	if self.transitions[self.current_state][index]['action'] == "RIGHT":
	# 		self.head_index += 1
	# 	elif self.transitions[self.current_state][index]['action'] == "LEFT" and self.head_index != 0:
	# 		self.head_index -= 1
	# 	else:
	# 		self.update_current_state("REJECT")
	# 		print("Error - Tape REJECT")
	# 		sys.exit()
		

	# def between_states(self):
	# 	'''Manages everything that happens in between states'''

	# 	index = 0
	# 	self.read_symbol()
	# 	for x in range(len(self.transitions[self.current_state])):
	# 		if self.current_symbol == self.transitions[self.current_state][x]['read']:
	# 			index = x
	# 	print_tape_and_transition(self, index)
	# 	if self.transitions[self.current_state][index]['read'] != self.current_symbol:
	# 		self.update_current_state("REJECT")
	# 		print("Error - Tape REJECT")
	# 	if self.current_state != "REJECT":
	# 		self.write_symbol(index)
	# 		self.move_head(index)
	# 		self.update_current_state(self.transitions[self.current_state][index]['to_state'])
