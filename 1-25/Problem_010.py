__author__ = 'rutger'

dict = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}

dict2 = {
    0: "A",
    1: "C",
    2: "G",
    3: "T"
}

f = open("file_010.txt").readlines()

sequence = ""
seq = []
for line in f:
    if line[0] == ">":
        seq.append(sequence)
        sequence = ""
    else:
        sequence += line.replace("\n", "")
seq.append(sequence)
seq.pop(0)

count = []

for i in range(len(seq[0])):
    tmp = [0,0,0,0]
    for j in range(len(seq)):
        tmp[dict[seq[j][i]]] += 1
    count.append(tmp)

consensus = ""
for row in count:
    consensus += dict2[row.index(max(row))]

print(consensus)
a = ""
c = ""
g = ""
t = ""
for i in range(len(seq[0])):
    a += " " + str(count[i][0])
    c += " " + str(count[i][1])
    g += " " + str(count[i][2])
    t += " " + str(count[i][3])

print("A:" + a)
print("C:" + c)
print("G:" + g)
print("T:" + t)