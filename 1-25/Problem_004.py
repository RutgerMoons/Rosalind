__author__ = 'rutger'

k = 3
n = 30

aged = 1
unaged = 0

for i in range(n - 1):
    tmp = aged * 3
    aged += unaged
    unaged = tmp

print(aged)