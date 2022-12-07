#!/usr/bin/python3

#f = open( "miniinepute.txt", "r" )
f = open( "inepute.txt", "r" )

tree = {}
cwd = []

def get_tree_ptr():
	ptr = tree 
	for d in cwd:
		ptr = ptr[d]["children"]
	return ptr

def recurs_sum_branch_size(branch):
	if branch["type"] == "file":
		return branch["size"]
	elif branch["type"] == "dir":
		branch["size"] = 0
		for child in branch["children"].keys():
			branch["size"] += recurs_sum_branch_size(branch["children"][child])
		return branch["size"]
	
def recurs_find_small_dirs(branch, maxsize=0):
	if branch["type"] == "file":
		return []
	elif branch["type"] == "dir":
		if branch["size"] < maxsize:
			result = [ branch["size"] ]
			for child in branch["children"].keys():
				result.extend( recurs_find_small_dirs(branch["children"][child], maxsize) )
			return result
		else:
			result = []
			for child in branch["children"].keys():
				result.extend( recurs_find_small_dirs(branch["children"][child], maxsize) )
			return result
	
def recurs_find_required_space(branch, minsize=0):
	if branch["type"] == "file":
		return []
	elif branch["type"] == "dir":
		if branch["size"] > minsize:
			result = [ branch["size"] ]
			for child in branch["children"].keys():
				result.extend( recurs_find_required_space(branch["children"][child], minsize) )
			return result
		else:
			result = []
			for child in branch["children"].keys():
				result.extend( recurs_find_required_space(branch["children"][child], minsize) )
			return result
	

for line in f.readlines():
	line = line.strip()

	if line.startswith("$ ls"):
		continue
	elif line.startswith("$ cd"):
		folder = line.replace("$ cd ", "")
		if folder == "..":
			cwd.pop()
		else:
			tree_pointer = get_tree_ptr()
			tree_pointer[folder] = { "type":"dir", "size": 0, "children":{} }
			cwd.append(folder)
		continue
	elif line.startswith("dir "):
		continue
	else:
		line = line.split(" ")
		size = int(line[0])
		name = line[1]

		tree_pointer = get_tree_ptr()
		tree_pointer[name] = { "type":"file", "size": size, "children": None }


#print(tree)
recurs_sum_branch_size(tree["/"])

#print(tree)

print(sum(recurs_find_small_dirs(tree["/"], maxsize=100000)))

total_space = 70000000
required_space = 30000000
space_to_find = required_space - (total_space - tree["/"]["size"])

print(tree["/"]["size"])
print(space_to_find)

print(min(recurs_find_required_space(tree["/"], minsize=space_to_find)))

#print(result)
