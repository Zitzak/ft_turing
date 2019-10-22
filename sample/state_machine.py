# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    state_machine.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 11:48:52 by mgross         #+#    #+#                 #
#    Updated: 2019/10/22 16:04:48 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #


class Tape(object):
	'''	comment on tape'''
	
	def __init__(self, tape_s = ""):
		self.tape = dict((enumerate(tape_s)))

class StateMachine(object):
	
	def __init__(self):
		# self.transitions = {}
		self.initial_state = ""
		# self.finals = []
		# self.blank = ""
		self.tape = {}
		
	def add_input(self, tape):
		self.tape = dict((enumerate(tape)))

	def add_initial_state(self, name):
		self.initial_state = name

	def update_current_state(self, new_state):
		self.current_state = new_state
	
   