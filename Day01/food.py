#!/usr/bin/python3

f = open("food.txt", "r")

elf_le_plus_fort = 0
total = 0
for n in f.readlines():
	n = n.strip()
	if n != "":
		total += int(n)
	else:
		if total > elf_le_plus_fort:
			elf_le_plus_fort = total
			print( "Max!!!", elf_le_plus_fort )
		total = 0

print( elf_le_plus_fort )
