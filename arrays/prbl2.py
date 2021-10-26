# https://www.codechef.com/problems/TLG

n = int(input())
p1 = []
p2 = []
agg_score = -1
player = None

agg1 = []
agg2 = []
for i in range(0, n):
    a = input().split()
    p1.append(int(a[0]))
    p2.append(int(a[1]))
agg1.append(p1[0])
agg2.append(p2[0])
for i in range(1, n):
    agg1.append(agg1[i - 1] + p1[i])
    agg2.append(agg2[i - 1] + p2[i])
# print(agg1)
# print(agg2)
for i in range(0, n):
    a1 = agg1[i] - agg2[i]
    a2 = agg2[i] - agg1[i]
    if a1 > a2 and a1 > agg_score:
        player = 1
        agg_score = agg1[i] - agg2[i]
    elif a2 > a1 and a2 > agg_score:
        player = 2
        agg_score = agg2[i] - agg1[i]
print(str(player) + " " + str(agg_score))
