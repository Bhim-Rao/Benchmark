from datetime import datetime
from sys import argv

arguments = argv

if not arguments[1].endswith(".py"):
	print("Incorrect or Nonexistent Filename")
	exit()

try:
	f = open(arguments[1], "r")
except FileNotFoundError:
	print("File Not Found")
	exit()

content = f.read()
a = datetime.now()
output = exec(content)
b = datetime.now()
print()
print(f"{(b - a).microseconds/1000} ms")

# python -m PyInstaller -F benchmark.py to compile