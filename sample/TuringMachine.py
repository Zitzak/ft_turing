# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    TuringMachine.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 11:48:52 by mgross         #+#    #+#                 #
#    Updated: 2019/10/27 18:54:51 by Marvin        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
from argparser import ArgumentParser

class TuringMachine(object):
	''' '''

	def	__init__(self, args):
		''' Init vars in TuringMachine.'''
		
		self.name = self.assign_value_from_machine_config(args, "name")
		self.alphabet = self.assign_value_from_machine_config(args, "alphabet")
		self.blank = self.assign_value_from_machine_config(args, "blank")
		self.states = self.assign_value_from_machine_config(args, "states")
		self.initial = self.assign_value_from_machine_config(args, "initial")
		self.finals = self.assign_value_from_machine_config(args, "finals")
		self.transitions = self.assign_value_from_machine_config(args, "transitions")
		self.current_state = ""
		self.current_symbol = ""
		self.head_index = 0
		self.length_header = 80
		self.tape = args.input + "." * (len(args.input) * 2)

		self.add_extra_state_in_states("REJECT")
		self.add_extra_state_in_finals("REJECT")
		self.validate_machine_config()
		self.update_current_state(self.initial)

	def __str__(self):
		'''str method.'''

		pass

	def assign_value_from_machine_config(self, args, string):
			''' Try if "string" is in the .json file and if so, assign it.'''

			try:
				value = args.machine_config[string]
			except:
				print('Error - No {} field in .json file.' .format(string))
				sys.exit()
			return value

	def	add_extra_state_in_states(self, state):
		'''Adds extra elem to_list'''
		self.states = self.states + [state]

	def	add_extra_state_in_finals(self, state):
		'''Adds extra elem to_list'''
		self.finals = self.finals + [state]

	def validate_machine_config(self):
		''' Validates all the machine config input.'''

		self.validate_string_in_lists(self.blank, self.alphabet, "alphabet")
		self.validate_string_in_lists(self.initial, self.states, "states")
		self.validate_list_in_list(self.finals, self.states, "states")
		self.validate_values_in_instruction_dictionary(self.transitions, "transitions")

	def validate_string_in_lists(self, value, config, name):
		''' Validates that value is inside the list config.'''

		if value not in config:
			self.print_error_and_exit('Error - {} not found in list ' .format(value) + name + ".")

	def	validate_list_in_list(self, value, config, name):
		''' Validates that all elements of list value are also in list config.'''

		for elem in value:
			if elem not in config:
				self.print_error_and_exit('Error - {} not found in list ' .format(value) + name + ".")

	def validate_values_in_instruction_dictionary(self, dictionary, name):
		''' Validates thats certan values are inside lists inside dictionary.'''
		
		for key in dictionary:
			for elem in dictionary[key]:
				self.validate_string_in_lists(elem['read'], self.alphabet, "alphabet. Error at transitions -> {} -> 'read' -> {}" .format(key, elem['read']))
				self.validate_string_in_lists(elem['write'], self.alphabet, "alphabet. Error at transitions -> {} -> 'write' -> {}" .format(key, elem['write']))
				self.validate_string_in_lists(elem['to_state'], self.states, "states. Error at transitions -> {} -> 'to_state' -> {}" .format(key, elem['to_state']))
				self.validate_string_in_lists(elem['action'], ['LEFT', 'RIGHT'], "states. Error at transitions -> {} -> 'action' -> {}" .format(key, elem['action']))
				self.validate_string_in_lists(elem['action'], ['LEFT', 'RIGHT'], "states. Error at transitions -> {} -> 'action' -> {}" .format(key, elem['action']))

	def print_error_and_exit(self, error_message):
		'''Prints the error messages given and exits.'''

		print(error_message)
		sys.exit()

	def print_machine_config(self):
		'''Outputs the given machine output in a specified format'''
		
		self.print_header_with_name()
		self.print_list(self.alphabet, "Alphabet", "")
		self.print_list(self.states, "States", "  ")
		self.print_string(self.initial, "Initial", " ")
		self.print_list(self.finals, "Finals", "  ")
		self.print_transitions(self.transitions)
		self.print_astrix_line()

	def print_header_with_name(self):
		'''Prints header with name.'''

		self.print_astrix_line()
		self.print_astrix_and_spaces_line()
		self.print_name_line(self.name)
		self.print_astrix_and_spaces_line()
		self.print_astrix_line()
		

	def	print_astrix_line(self):
		'''Prints a line of astrixes size of length_header.'''
		
		for index in range(self.length_header - 1):
			print("*", end='')
		print("*")


	def print_astrix_and_spaces_line(self):
		'''Print line with astrix at start en end of line, spaces in the middel.'''

		print("*", end="")
		for index in range(self.length_header - 2):
			print(" ", end='')
		print("*")

	def print_name_line(self, name):
		'''Prints line with astrix at start and end, spaces and in the middel the name.'''
		
		num_spaces = int(((self.length_header - len(name)) / 2) - 2)
		index = 0

		print("*", end="")
		while index < (self.length_header - 1):
			if index == num_spaces:
				print(name, end = "")
				index += len(name)
			else:
				print(" ", end = "")
			index += 1
		print("*")

	def print_list(self, list_to_print, name_list, spaces):
		'''Print all elements in a list'''

		print("{}{}: [ ". format(name_list, spaces), end = "")
		print(*list_to_print, sep = ", ", end = "")
		print(" ]")

	def print_string(self, string_to_print, name_string, spaces):
		'''Print string in a certan fromat.'''

		print("{}{}:   {} ". format(name_string, spaces, string_to_print))

	def print_transitions(self, transitions):
		''' Prints all the transitions from the input'''

		for key in self.transitions.keys():
			entries = self.transitions[key]
			for index in range(len(entries)):
				self.print_current_transition(entries, index, key)

	def	print_current_transition(self, entries, index, key):
		'''Prints a list from a dictonary. dict->key->list.'''

		print("(" + key + ", " + entries[index]['read'] + ") -> (" + entries[index]['to_state'] 
		+ ", " + entries[index]['write'] + ", " + entries[index]['action'] + ")")

	def print_tape_with_head_position(self):
		''' Prints the tape with the current head position highlighted.'''

		print("[", end = "")
		for index in range(len(self.tape)):
			if index == self.head_index:
				print("\033[0;104m" + self.tape[index] + "\033[0m", end ="")
			else:
				print(self.tape[index], end ="")
		print("] ", end = "")

	def print_tape_and_transition(self, index):
		'''Prints the tape and the current configuration of the Turing Machine.'''

		self.print_tape_with_head_position()
		self.print_current_transition(self.transitions[self.current_state], index, self.current_state)
				
	def update_current_state(self, new_state):
		'''Update current state.'''

		self.current_state = new_state

	def read_symbol(self):
		'''Reads symbole form tape.'''

		self.current_symbol = self.tape[self.head_index]

	def write_symbol(self, index):
		'''Writes symbol to tape.'''

		char = self.transitions[self.current_state][index]['write']
		temp_list = list(self.tape)
		temp_list[self.head_index] = self.transitions[self.current_state][index]['write']
		self.tape = "".join(temp_list)

	def	move_head(self, index):
		''' Moves the head_index.'''

		if self.transitions[self.current_state][index]['action'] == "RIGHT":
			self.head_index += 1
		elif self.transitions[self.current_state][index]['action'] == "LEFT" and self.head_index != 0:
			self.head_index -= 1
		else:
			self.update_current_state("REJECT")
	
	def get_index(self):
		'''Checks for the list that has the current_symbol.'''

		for index in range(len(self.transitions[self.current_state])):
			if self.current_symbol == self.transitions[self.current_state][index]['read']:
				return index
		self.current_state = "REJECT"
		return False


	def between_states(self):
		'''Manages everything that happens in between states'''

		self.read_symbol()
		index = self.get_index()
		if index is not False:
			self.print_tape_and_transition(index)
			self.write_symbol(index)
			self.move_head(index)
			self.update_current_state(self.transitions[self.current_state][index]['to_state'])
		else:
			return

	def run(self):
		'''Runs the Turing Machine.'''

		while self.current_state not in self.finals:
			self.between_states()
		
		if self.current_state == "REJECT":
			self.print_error_and_exit("\nREJECT - Invalid symbol on tape.")