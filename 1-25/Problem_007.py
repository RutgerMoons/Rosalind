__author__ = 'rutger'

def prob(a, b):
    return ((a[0] or b[0]) + (a[0] or b[1]) + (a[1] or b[0]) + (a[1] or b[1])) / 4

k = 29
m = 29
n = 26

genes = []
for i in range(k):
    genes.append((True, True))

for i in range(m):
    genes.append((True, False))

for i in range(n):
    genes.append((False, False))

counter = 0
for i in range(len(genes)):
    for j in range(len(genes)):
        if i != j:
            counter += prob(genes[i], genes[j])
print(counter)

print(counter/(len(genes) * (len(genes) - 1)))