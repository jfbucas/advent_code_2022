#!/usr/bin/python3

f = open( "RPS.txt", "r" )

signs_score = { "rock": 1,  "paper": 2, "scissors": 3 }
elf1_signs = { "A":"rock", "B":"paper", "C":"scissors" }
elf2_signs = { "X":"rock", "Y":"paper", "Z":"scissors" }

win = 6
draw = 3
loose = 0

rules = {
	"rock"     : { "rock": draw , "paper": loose, "scissors": win  },
	"paper"    : { "rock": win  , "paper": draw,  "scissors": loose},
	"scissors" : { "rock": loose, "paper": win,   "scissors": draw },
}


score_elf2 = 0

for line in f.readlines():
	line = line.strip()
	elf1 = elf1_signs[ line[0] ]
	elf2 = elf2_signs[ line[2] ]

	# Score for the shape chosen
	score_elf2 += signs_score[ elf2 ] + rules[ elf2 ][ elf1 ]
	
			
print(score_elf2)
	
