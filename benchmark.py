from datetime import datetime
from sys import argv

arguments = argv
flags = []

class Config:
	def __init__(self):
		#This value sets if the target file's output is displayed
		self.display = True
		#set's what unit the time will be displayed as. Acceptable values are [ms, mcs, s]
		self.units = "ms"
		self.repeats = 1
		self.verbose = False

config = Config()

def unit_output(outputs):
	for time in outputs:
		if config.units == "s":
			time = f"\n{time.microseconds/1000000} s"
		if config.units == "ms":
			print(f"\n{time.microseconds/1000} ms")
		if config.units == "mcs":
			print(f"\n{time.microseconds} mcs")

def init_flags():
	units_set = 0
	skip = False
	for i in range(0, len(arguments)):
		if skip:
			skip = False
			pass
		if arguments[i].startswith("-") or arguments[i].startswith("--"):
			if arguments[i] == "-r":
				skip = True
				flags.append(arguments[i])
				flags.append(arguments[i + 1])
			else:
				flags.append(arguments[i])
	skip = False
	for i in range(0, len(flags)):
		if skip:
			skip = False
			pass
		match flags[i]:
			case "-p":
				config.display = False
			case "--print":
				config.display = False
			case "-r":
				config.repeats = int(flags[i+1])
				skip = True
			case "-s":
				config.units = "s"
				units_set += 1
			case "-ms":
				config.units = "ms"
				units_set += 1
			case "-mcs":
				config.units = "mcs"
				units_set += 1

		arguments.remove(flags[i])

		if units_set > 1:
			print("More than one unit set")
			exit()

def checks(fn):
	if not fn.endswith(".py"):
		print("Incorrect or Nonexistent Filename")
		exit()

	try:
		f = open(fn, "r")
	except FileNotFoundError:
		print("File Not Found")
		exit()

	return f.read()

def time(content):
	a = datetime.now()
	exec(content)
	b = datetime.now()
	return (b-a)

def main(fn):
	content = checks(fn)
	outputs = []
	for i in range(0, config.repeats):
		if config.display:
			out = time(content)
		else:
			out = time(f"enable_print = print\ndisable_print = lambda *x, **y: None\nprint = disable_print\n{content}\nprint = enable_print")
		outputs.append(out)
	unit_output(outputs)

init_flags()
main(arguments[1])


# python -m PyInstaller -F benchmark.py to compile
