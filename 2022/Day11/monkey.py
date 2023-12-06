#!/usr/bin/python3

f = open("situtation.txt")
#f = open("minisitutation.txt")

situation = []
for s in f.readlines():
	situation.append(s.strip())

Monkeys = { }

for s in situation:
	if s.startswith("Monkey"):
		monkey = int(s.split(":")[0].split(" ")[1])
		Monkeys[monkey] = {}
		Monkeys[monkey]["business"] = 0
	elif s.startswith("Starting items"):
		Monkeys[monkey]["items"] = eval("["+s.split(":")[1]+"]")
	elif s.startswith("Operation"):
		Monkeys[monkey]["operation"] = s.split("=")[1].replace("old", "item")
	elif s.startswith("Test"):
		Monkeys[monkey]["test"] = int(s.split(" ")[-1])
	elif s.startswith("If true"):
		Monkeys[monkey][True] = int(s.split(" ")[-1])
	elif s.startswith("If false"):
		Monkeys[monkey][False] = int(s.split(" ")[-1])


#print(Monkeys)

for rounders in range(0,20):
	for monkey in Monkeys.keys():
		for item in Monkeys[monkey]["items"]:
			worry = eval(Monkeys[monkey]["operation"])

			worry3 = worry // 3
			to_monkey = Monkeys[monkey][ (worry3 % Monkeys[monkey]["test"] == 0) ]

			Monkeys[to_monkey]["items"].append(worry3)
			Monkeys[monkey]["business"] += 1

			#print(monkey, item, worry, worry3, to_monkey)

		Monkeys[monkey]["items"] = []


business = []
for monkey in Monkeys.keys():
	business.append( Monkeys[monkey]["business"] )

business.sort()
#print(business)
print(business[-1]*business[-2])
