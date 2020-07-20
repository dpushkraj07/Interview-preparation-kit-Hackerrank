# n,m = map(int,input().split())
# # print(n)
# # print(m)
# # #ab=[]
# l = [0]*n
# # #
# # for i in range(m):
# #     #print(i)
# #     for j in range(3):
# #             col = []
# #             #print(j)
# #             col.append(map(int,input().split()))
# #     ab.append(col)
# # print(ab)
# rows, cols = (m, 3)
# arr=[]
# k = []
# for i in range(rows):
#     arr.append(list(map(int,input().split())))
#     k.append(arr[i][2])
#
# # for i in range((arr[i][0]-1),arr[i][1]):
# #     if l[arr[i][0]-1] == 0:
# #         l[arr[i][0]-1] = k[i]
# #     else:
# #         l[arr[i][0]-1] = l[arr[i][0]-1] + k[i]
# #
# # print(max(l))
# for i in range(len(arr)):
#     s = arr[i][0] - 1
#     for j in range(s,arr[i][1]):
#         if l[j] == 0:
#             l[j] = arr[i][2]
#         else:
#             l[j] = l[j] + arr[i][2]
# print(max(l))

n, inputs = map(int,input().split())
list = [0]*(n+1)
#print(list)
for _ in range(inputs):
    x, y, incr = map(int,input().split())
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
    #print(list)
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)
