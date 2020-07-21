from collections import Counter
magazine = input().rstrip().split()

note = input().rstrip().split()
# y = []
# flag = 0
# for i in note:
#     if i in magazine:
#         flag = 1
#     else:
#         flag = 0
#
#
# if flag == 1:
#     print("Yes")
# else:
#     print("No")
#

if (Counter(note) - Counter(magazine)) == {}:
    print("Yes")
else:
    print("No")
