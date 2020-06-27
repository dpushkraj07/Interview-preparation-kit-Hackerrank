nd = input().split()

n = int(nd[0])

d = int(nd[1])
p1 = []
p2 = []
a = list(map(int, input().rstrip().split()))
s = n-d
p2 = a[-s:]

for i in a[:d]:
    p1.append(i)



print(p2+p1)

#
# a = [1, 2, 3, 4, 5]
# print(a[-1:])
def rotLeft(n, a, d):
    p1 = []
    p2 = []
    s = n-d
    p2 = a[-s:]

    for i in a[:d]:
        p1.append(i)

    return(p2+p1)
