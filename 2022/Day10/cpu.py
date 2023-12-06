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
checkpoints = []
while ip < len(instructions):
	cycle += 1
	if (cycle + 20) % 40 == 0:
		checkpoints.append(RAX*cycle)
		#print(cycle, RAX, RAX*cycle)

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
