# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    argparser.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/25 13:36:51 by mgross         #+#    #+#                 #
#    Updated: 2019/10/27 18:06:54 by Marvin        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
import json

class ArgumentParser(object):
	''' Gets arguments. '''

	def __init__(self):
		''' Init variables from argparser.'''
		parser = argparse.ArgumentParser(description=None, usage='%(prog)s [-h] jsonfile input')
		parser.add_argument('machine_config', type=str, help='json description of the machine')
		parser.add_argument('input', type=str, help='input of the machine')
		args = parser.parse_args()
		
		self.input = args.input
		with open(args.machine_config, 'r') as f:
			try:
				self.machine_config = json.load(f)
			except:
				print('Error - No .json file.')
				f.close()
				sys.exit()
		f.close()
