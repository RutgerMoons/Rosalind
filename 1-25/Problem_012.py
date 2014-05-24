__author__ = 'rutger'


a = open("file_012.txt").readlines()
label = ""
sequence = ""
solutions = []
for line in a:
    if line[0] == ">":
        solutions.append((label, sequence))
        label = line[1:(len(line) - 1)]
        sequence = ""
    else:
        sequence += line.replace("\n", "")
solutions.append((label, sequence))
solutions.pop(0)

k = 3

sol = set()
for t1 in solutions:
    for t2 in solutions:
        if t1 != t2 and (t2[1].endswith(t1[1][0:k])):
            sol.add((t2[0], t1[0]))

for tuple in sol:
    print("%s %s" % (tuple[0], tuple[1]))

