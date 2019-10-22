# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    state_machine.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 11:48:52 by mgross         #+#    #+#                 #
#    Updated: 2019/10/22 22:59:05 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import copy
import sys
from utillitie import print_tape_and_transition


class TuringMachine(object):
	
	def	__init__(self):
		''' Init vars in TuringMachine.'''
		
		self.transitions = {}
		self.finals = []
		self.blank = ""
		self.states = []
		self.tape = []
		self.current_state = ""
		self.current_symbol = ""
		self.head_index = 0

	def add_tape(self, tape):
		''' Adds tape.'''

		self.tape = list(tape)

	def	add_transitions(self, transitions):
		''' Adds transitions.'''

		self.transitions = transitions

	def add_final_states(self, finals):
		'''Adds final states and adds "REJECT" state.'''

		if "REJECT" not in finals:
			finals = finals + ["REJECT"]
		self.finals = copy.copy(finals)

	def add_blank(self, blank):
		'''Adds blank char.'''
		
		self.blank = blank

	def update_current_state(self, new_state):
		'''Update current state.'''

		self.current_state = new_state

	def read_symbol(self):
		'''Reads symbole form tape.'''

		self.current_symbol = self.tape[self.head_index]

	def write_symbol(self, index):
		'''Writes symbol to tape.'''
		self.tape[self.head_index] = self.transitions[self.current_state][index]['write']
	
	def	move_head(self, index):
		''' Moves the head_index.'''

		if self.transitions[self.current_state][index]['action'] == "RIGHT":
			self.head_index += 1
		elif self.transitions[self.current_state][index]['action'] == "LEFT" and self.head_index != 0:
			self.head_index -= 1
		else:
			self.update_current_state("REJECT")
			print("Error - Tape REJECT")
			sys.exit()
		

	def between_states(self):
		'''Manages everything that happens in between states'''

		index = 0
		self.read_symbol()
		for x in range(len(self.transitions[self.current_state])):
			if self.current_symbol == self.transitions[self.current_state][x]['read']:
				index = x
		print_tape_and_transition(self, index)
		if self.transitions[self.current_state][index]['read'] != self.current_symbol:
			self.update_current_state("REJECT")
			print("Error - Tape REJECT")
		if self.current_state != "REJECT":
			self.write_symbol(index)
			self.move_head(index)
			self.update_current_state(self.transitions[self.current_state][index]['to_state'])
