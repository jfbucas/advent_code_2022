#!/usr/bin/python3

f = open( "inchpouchteu.txt", "r" )
#f = open( "miniinchpouchteu.txt", "r" )

forest = []
visible = []

width = 0
height = 0

for line in f.readlines():
	line = line.strip()
	width = len(line)

	forest.append(line)

	height += 1


visible.extend(  [ 0 ] * (width*height) )

# From top to bottom, and from bottom to top
for mydir in [ range(0, height), range(height-1, -1, -1) ]:
	maxheight = [ -1 ] * width
	for y in mydir:
		for x in range(0, width):
			treeheight = int(forest[y][x])
			if treeheight > maxheight[x]:
				maxheight[x] = treeheight
				visible[y*width+x] = 1

# From left to right, and from right to left
for mydir in [ range(0, height), range(height-1, -1, -1) ]:
	maxheight = [ -1 ] * height
	for x in mydir:
		for y in range(0, width):
			treeheight = int(forest[y][x])
			if treeheight > maxheight[y]:
				maxheight[y] = treeheight
				visible[y*width+x] = 1


print(sum(visible))

views = [ 0 ] * (width*height)
for y in mydir:
	for x in range(0, width):
		treeheight = int(forest[y][x])

		# North view
		northview = 0
		if y > 0:
			north = y-1
			viewheight = int(forest[north][x])
			while (north > 0) and (treeheight>viewheight):
				north -= 1
				viewheight = int(forest[north][x])
			northview = y - north
			
		# South view
		southview = 0
		if y < height-1:
			south = y+1
			viewheight = int(forest[south][x])
			while (south < height-1) and (treeheight>viewheight):
				south += 1
				viewheight = int(forest[south][x])
			southview = south - y
	
		# West view
		westview = 0
		if x > 0:
			west = x-1
			viewheight = int(forest[y][west])
			while (west > 0) and (treeheight>viewheight):
				west -= 1
				viewheight = int(forest[y][west])
			westview = x - west
			
		# East view
		eastview = 0
		if x < width-1:
			east = x+1
			viewheight = int(forest[y][east])
			while (east < width-1) and (treeheight>viewheight):
				east += 1
				viewheight = int(forest[y][east])
			eastview = east - x

		views[x+y*width] = northview * southview * westview * eastview

print(views)
print(max(views))
