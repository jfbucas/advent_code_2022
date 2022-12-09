#!/usr/bin/python3

f = open( "automatinput.txt", "r")

# We define a grid
W = 500
H = 500
grid = [ 0 ] * (W*H)

# We start from the middle of the grid
nb_knots = 3
ropeX = [W//2] * nb_knots
ropeY = [H//2] * nb_knots

for line in f.readlines():
	line = line.strip()
	line = line.split(" ")

	direction = line[0]
	steps = int(line[1])

	for s in range(steps):

		# Move the Head
		if direction == "U":
			ropeY[0] -= 1
		elif direction == "R":
			ropeX[0] += 1
		elif direction == "D":
			ropeY[0] += 1
		elif direction == "L":
			ropeX[0] -= 1

		print(set(zip(ropeX,ropeY)))
		for k in range(1, nb_knots):

			Hx = ropeX[k-1]
			Hy = ropeY[k-1]

			# Get the tail to follow
			if Hy == ropeY[k] and Hx == ropeX[k]:
				pass

			# U R D L
			elif ropeY[k] == Hy and ropeX[k] == Hx-2:
				ropeX[k] += 1
			elif ropeY[k] == Hy and ropeX[k] == Hx+2:
				ropeX[k] -= 1
			elif ropeY[k] == Hy-2 and ropeX[k] == Hx:
				ropeY[k] += 1
			elif ropeY[k] == Hy+2 and ropeX[k] == Hx:
				ropeY[k] -= 1

			# Diagonal
			elif ropeY[k] == Hy-1 and ropeX[k] == Hx-2:
				ropeX[k] += 1
				ropeY[k] += 1
			elif ropeY[k] == Hy+1 and ropeX[k] == Hx-2:
				ropeX[k] += 1
				ropeY[k] -= 1
			elif ropeY[k] == Hy-1 and ropeX[k] == Hx+2:
				ropeX[k] -= 1
				ropeY[k] += 1
			elif ropeY[k] == Hy+1 and ropeX[k] == Hx+2:
				ropeX[k] -= 1
				ropeY[k] -= 1
			elif ropeY[k] == Hy-2 and ropeX[k] == Hx-1:
				ropeX[k] += 1
				ropeY[k] += 1
			elif ropeY[k] == Hy-2 and ropeX[k] == Hx+1:
				ropeX[k] -= 1
				ropeY[k] += 1
			elif ropeY[k] == Hy+2 and ropeX[k] == Hx-1:
				ropeX[k] += 1
				ropeY[k] -= 1
			elif ropeY[k] == Hy+2 and ropeX[k] == Hx+1:
				ropeX[k] -= 1
				ropeY[k] -= 1


		grid[ropeX[nb_knots-1]+ropeY[nb_knots-1]*W] = 1


print(sum(grid))
