#!/usr/bin/python3

f = open( "RPS.txt", "r" )

score_elf2 = 0

for line in f.readlines():
	line = line.strip()
	elf1 = line[0]
	elf2 = line[2]
	


	# Adjust elf2 play
	if elf1 == "A":
		if elf2 == "X":
			elf2 = "Z"
		elif elf2 == "Y":
			elf2 = "X"
		elif elf2 == "Z":
			elf2 = "Y"

	elif elf1 == "B":
		if elf2 == "X":
			elf2 = "X"
		elif elf2 == "Y":
			elf2 = "Y"
		elif elf2 == "Z":
			elf2 = "Z"

	elif elf1 == "C":
		if elf2 == "X":
			elf2 = "Y"
		elif elf2 == "Y":
			elf2 = "Z"
		elif elf2 == "Z":
			elf2 = "X"
	
	
	
	
	# Score for the shape chosen
	if elf2 == "X":
		score_elf2 += 1
	elif elf2 == "Y":
		score_elf2 += 2
	elif elf2 == "Z":
		score_elf2 += 3	
	
	# Score against elf1
	if elf1 == "A":
		if elf2 == "X":
			score_elf2 += 3
		elif elf2 == "Y":
			score_elf2 += 6
		elif elf2 == "Z":
			score_elf2 += 0

	elif elf1 == "B":
		if elf2 == "X":
			score_elf2 += 0
		elif elf2 == "Y":
			score_elf2 += 3
		elif elf2 == "Z":
			score_elf2 += 6

	elif elf1 == "C":
		if elf2 == "X":
			score_elf2 += 6
		elif elf2 == "Y":
			score_elf2 += 0
		elif elf2 == "Z":
			score_elf2 += 3
			
print(score_elf2)
	
