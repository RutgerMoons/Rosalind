__author__ = 'rutger'

def gc(s):
    if len(s) <= 0:
        return 0
    return (s.count("C") + s.count("G")) / len(s)

a = open("file_005.txt").readlines()
label = ""
sequence = ""
solutions = []
for line in a:
    if line[0] == ">":
        solutions.append((label, gc(sequence)))
        label = line
        sequence = ""
    else:
        sequence += line.replace("\n", "")
solutions.append((label, gc(sequence)))

max = solutions[0]
for i in range(1, len(solutions)):
    if solutions[i][1] > max[1]:
        max = solutions[i]

print("%s%f" % (max[0].replace(">", ""), max[1] * 100))
