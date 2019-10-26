# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    utillitie.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:43:29 by mgross         #+#    #+#                 #
#    Updated: 2019/10/25 13:37:12 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse

# def get_args():
# 	''' Get's passed arguments -> return args.'''

# 	parser = argparse.ArgumentParser(description=None, usage='%(prog)s [-h] jsonfile input')
# 	parser.add_argument('filename', type=str, help='json description of the machine')
# 	parser.add_argument('input', type=str, help='input of the machine')
# 	args = parser.parse_args()
# 	return args

def print_machine_config(machine_config):
	''' Prints the opening and all the input from the.json file.'''

	print_name(machine_config.name)
	print_alphabet(machine_config.alphabet)
	print_states(machine_config.states)
	print_initial(machine_config.initial)
	print_finals(machine_config.finals)
	print_transitions(machine_config.transitions)
	print_star_line()

def	print_alphabet(alphabet):
	''' Prints alphabet input.'''

	print("Alphabet: [ ", end = "")
	print(*alphabet, sep = ", ", end = "")
	print(" ]")

def print_states(states):
	''' Prints states input.'''

	print("States  : [ ", end = "")
	print(*states, sep=", ", end = "")
	print(" ]")

def print_initial(initial):
	''' Prints initial input.'''

	print("Initial : " + initial)

def	print_finals(finals):
	''' Prints finals input.'''

	print("Finals  : [ ", end ="")
	print(*finals, end = "")
	print(" ]")

def	print_star_line():
	''' Prints a line with astrix ("*").'''

	for i in range(79):
		print("*", end='')
	print("*")

def	print_current_transition(entries, i, key):
	'''Prints a list from a dictonary. dict->key->list.'''

	print("(" + key + ", " + entries[i]['read'] + ") -> (" + entries[i]['to_state'] 
	+ ", " + entries[i]['write'] + ", " + entries[i]['action'] + ")")

def print_transitions(transitions):
	''' Prints all the transitions from the input'''

	for key in transitions.keys():
		entries = transitions[key]
		for i in range(len(entries)):
			print_current_transition(entries, i, key)

def	print_tape(turing_machine):
	''' Print the tape with current head postion highlighted.'''

	print("[", end = "")
	for i in range(len(turing_machine.tape)):
		if i == turing_machine.head_index:
			print("\033[0;104m" + turing_machine.tape[i] + "\033[0m", end ="")
	
		else:
			print(turing_machine.tape[i], end ="")
	print("] ", end = "")

def print_tape_and_transition(turing_machine, x):
	''' Prints tape plus current transition.'''

	print_tape(turing_machine)
	print_current_transition(turing_machine.transitions[turing_machine.current_state], x, turing_machine.current_state)


def	print_name(name):
	'''Print the name at the beginning of the output.'''
	x = int((80 - len(name)) / 2)
	print_star_line()
	print("*", end="")
	for c in range(78):
		print(" ", end='')
	print("*")
	print("*", end="")
	for i in range(x):
		print(" ", end='')
	print(name, end="")
	for i in range(x - 1):
		print(" ", end='')
	print("*")
	print("*", end="")
	for c in range(78):
		print(" ", end='')
	print("*")
	print_star_line()
