# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    utillitie.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:43:29 by mgross         #+#    #+#                 #
#    Updated: 2019/10/21 19:38:55 by mgross        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def validat_initial(config):
	if config.initial in config.states:
		config.states.remove(config.initial)
	else:
		print('"Initial" state not found in list with states')
		exit()

def validate_finals(config):
	print(1, config.states)
	# length = len(config.finals)
	for elem in config.finals:
		if elem in config.states:
			config.states.remove(elem)
		else:
			print('"Finals" state not found in list with states')
			exit()
	print(2, config.states)

def validate_blank(config):
	if config.blank in config.alphabet:
		config.alphabet.remove(config.blank)
	else:
		print('"Blank" symbol not found in list alphabet')
		exit()
	# print(config.alphabet)

def	validate_input(config):
	validat_initial(config)
	validate_finals(config)
	validate_blank(config)

# def get_args():
# 	parser = argparse.ArgumentParser(description=None, usage='%(prog)s [-h] jsonfile input')
# 	parser.add_argument('filename', type=str, help='json description of the machine')
# 	parser.add_argument('input', type=str, help='input of the machine')
# 	args = parser.parse_args()
# 	return (args)

# def get_input():
# 	get_args()

	# with open(args.filename, 'r') as f:
	# 	machine_config = json.load(f)

	# for  in 

	# content = json.load(args.filename)
	# print(content.scanright)
	# if args.filename is not None:
	# 	config = open(args.filename, 'r')
	# 	print(config.read())

	# 	print(config)

	# return (args)
	# if args.filename is not None:
	# 	print(args.filename)
	# print(args.input)