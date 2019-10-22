# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:19:45 by mgross         #+#    #+#                 #
#    Updated: 2019/10/21 19:06:19 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse
import utillitie
import json

class inputConfig(object): #<-----moet hier object?
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
		
if __name__ == '__main__':
	machine_config = inputConfig()
	# print(machine_config.states)
	utillitie.validate_input(machine_config)
	# print(machine_config.states)
	# length = len(machine_config.states)
	# for i in configuration.transitions['scanright']:
	# 	print(i)
