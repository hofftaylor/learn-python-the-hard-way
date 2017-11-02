# Exercise 17.1 - More Files (Compressed)
# Trimmmed the fat for Study Drill 1, compressed it down to Study Drill 2.
from sys import argv ; script, from_file, to_file = argv ; print(f"Copying from {from_file} to {to_file}") ; in_file = open(from_file) ; indata = in_file.read() ; out_file = open(to_file, 'w') ; out_file.write(indata) ; print("File copied successfully.") ; out_file.close() ; in_file.close()
