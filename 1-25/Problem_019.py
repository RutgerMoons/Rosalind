__author__ = 'rutger'
import itertools

perm = 6
pos = []
for i in range(perm):
    pos.append(i+1)
a = set(itertools.permutations(pos, perm))
print(len(a))
for p in a:
    buildstr = ""
    for i in range(perm):
        buildstr += str(p[i]) + " "
    print(buildstr[0:-1])