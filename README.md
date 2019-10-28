# ft_turing
## Project of Codam Coding College - 42 Network
For this project I'm building a universal, single tape, turing machine. By giving the machine a set of instruction and a way to interpret them, it can process/compute any kind of information.

The program takes two arguments. The first argument is a .json file with the instructions for the machine. A valid example can be seen underneath.
```
{
	"name"    : "unary_sub",
	"alphabet": [ "1", ".", "-", "=" ],
	"blank"   : ".",
	"states"  : [ "scanright", "eraseone", "subone", "skip", "HALT"],
	"initial" : "scanright",
	"finals"  : [ "HALT" ],
 
	"transitions" : {
	
		"scanright": [
			{ "read" : ".", "to_state": "scanright", "write": ".", "action": "RIGHT"},
			{ "read" : "1", "to_state": "scanright", "write": "1", "action": "RIGHT"},
			{ "read" : "-", "to_state": "scanright", "write": "-", "action": "RIGHT"},
			{ "read" : "=", "to_state": "eraseone" , "write": ".", "action": "LEFT" }
		],
 
		"eraseone": [
			{ "read" : "1", "to_state": "subone", "write": "=", "action": "LEFT"},
			{ "read" : "-", "to_state": "HALT"  , "write": ".", "action": "LEFT"}
		],
 
		"subone": [
			{ "read" : "1", "to_state": "subone", "write": "1", "action": "LEFT"},
			{ "read" : "-", "to_state": "skip"  , "write": "-", "action": "LEFT"}
		],
 
		"skip": [
		{ "read" : ".", "to_state": "skip"     , "write": ".", "action": "LEFT"},
		{ "read" : "1", "to_state": "scanright", "write": ".", "action": "RIGHT"}
		]
	}
}
```

The second argument is a string of symbols the turing machine has to process with the instructions taken from the input file.

Further information can be found inside the subject PDF

# Execution
python3 ./sample/ft_turing.py ./machine_config/unary_sub.json 111-11=
 
