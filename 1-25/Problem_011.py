__author__ = 'rutger'

months = 89
death = 20

a = [0] * (death - 1) + [1]
for i in range(0, months):
    babies = 0
    for j in range(1, len(a)):
        babies += a[j]
    for j in range(len(a) - 1, 0, -1):
        a[j] = a[j - 1]
    a[0] = babies

print(sum(a))