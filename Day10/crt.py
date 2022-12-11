#!/usr/bin/python3

f = open( "anput.txt", "r" )
#f = open( "minianput.txt", "r" )

instructions = []
for instruction in f.readlines():
	instruction = instruction.strip()
	instructions.append(instruction.split(" "))


cycle = 0
cycle_instruction = 0
ip = 0
RAX = 1
CRT_position = 0
CRT_output = [ ]
row = ""
checkpoints = []
while ip < len(instructions):
	cycle += 1
	if (cycle + 20) % 40 == 0:
		checkpoints.append(RAX*cycle)
		#print(cycle, RAX, RAX*cycle)

	if CRT_position in [ RAX-1, RAX+0, RAX+1 ]:
		row += "#"
	else:
		row += "."
	CRT_position += 1

	if CRT_position == 40:
		CRT_position = 0
		CRT_output.append( row )
		row = ""

	#print(instructions[ip])
	if instructions[ip][0] == "noop":
		if cycle_instruction == 0:
			#cycle_instruction += 1
		#elif cycle_instruction == 1:
			ip += 1
			cycle_instruction = 0

	elif instructions[ip][0] == "addx":
		if cycle_instruction == 0:
			cycle_instruction += 1
		elif cycle_instruction == 1:
			RAX += int(instructions[ip][1])
			ip += 1
			cycle_instruction = 0
	
	
print(sum(checkpoints[0:6]))

for r in CRT_output:
	print(r)
