import json
from main import machine_configuration

with open('mach.json', 'r') as f:
	test = json.load(f)

conf = test['states']
mach = 