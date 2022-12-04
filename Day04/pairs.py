#!/usr/bin/python3

f = open( "ranges.txt", "r" )

overlap = 0
fulloverlap = 0

for line in f.readlines():
	line = line.strip()
	groups = line.split(",")

	group1 = groups[0].split("-")
	group2 = groups[1].split("-")


	sg1 = int(group1[0])
	eg1 = int(group1[1])
	sg2 = int(group2[0])
	eg2 = int(group2[1])

	if sg1<=sg2 and eg1>=eg2:
		print(group1, "contains", group2)
		fulloverlap += 1

	elif sg2<=sg1 and eg2>=eg1:
		print(group2, "contains", group1)
		fulloverlap += 1


	if (sg1<=sg2 and eg1>=sg2) or (sg1<=eg2 and eg1>=eg2):
		overlap += 1

	elif (sg2<=sg1 and eg2>=sg1) or (sg2<=eg1 and eg2>=eg1):
		overlap += 1

print(fulloverlap, overlap)
	
