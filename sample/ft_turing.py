# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: mgross <mgross@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 11:19:45 by mgross         #+#    #+#                 #
#    Updated: 2019/10/27 18:52:02 by Marvin        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from TuringMachine import TuringMachine
from argparser import ArgumentParser
		
if __name__ == '__main__':
	args = ArgumentParser()
	turing_machine = TuringMachine(args)
	turing_machine.print_machine_config()
	turing_machine.run()
