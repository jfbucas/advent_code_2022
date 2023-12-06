#!/usr/bin/python3

f = open( "automatinput.txt", "r")

# We define a grid
W = 500
H = 500
grid = [ 0 ] * (W*H)

# We start from the middle of the grid
Hx = W//2
Hy = H//2
Tx = Hx
Ty = Hy

for line in f.readlines():
	line = line.strip()
	line = line.split(" ")

	direction = line[0]
	steps = int(line[1])


	for s in range(steps):
		# Move the Head
		if direction == "U":
			Hy -= 1
		elif direction == "R":
			Hx += 1
		elif direction == "D":
			Hy += 1
		elif direction == "L":
			Hx -= 1

		# Get the tail to follow
		if Hy == Ty and Hx == Tx:
			pass

		# U R D L
		elif Ty == Hy and Tx == Hx-2:
			Tx += 1
		elif Ty == Hy and Tx == Hx+2:
			Tx -= 1
		elif Ty == Hy-2 and Tx == Hx:
			Ty += 1
		elif Ty == Hy+2 and Tx == Hx:
			Ty -= 1

		# Diagonal
		elif Ty == Hy-1 and Tx == Hx-2:
			Tx += 1
			Ty += 1
		elif Ty == Hy+1 and Tx == Hx-2:
			Tx += 1
			Ty -= 1
		elif Ty == Hy-1 and Tx == Hx+2:
			Tx -= 1
			Ty += 1
		elif Ty == Hy+1 and Tx == Hx+2:
			Tx -= 1
			Ty -= 1
		elif Ty == Hy-2 and Tx == Hx-1:
			Tx += 1
			Ty += 1
		elif Ty == Hy-2 and Tx == Hx+1:
			Tx -= 1
			Ty += 1
		elif Ty == Hy+2 and Tx == Hx-1:
			Tx += 1
			Ty -= 1
		elif Ty == Hy+2 and Tx == Hx+1:
			Tx -= 1
			Ty -= 1

		grid[Tx+Ty*W] = 1


print(sum(grid))
