nk = input().split()

n = int(nk[0])

k = int(nk[1])

prices = list(map(int, input().rstrip().split()))


budget = sorted(prices)
print(budget)
cash = 0
product = 0
pr = 0

for i in budget:
    if cash <= k :
        cash+=i
        print(cash)
        pr+=1

print(pr-1)
