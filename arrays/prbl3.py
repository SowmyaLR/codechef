# https://www.codechef.com/problems/WATSCORE

t = int(input())
while t > 0:
    n = int(input())
    score = {}
    val = 0
    for i in range(0, n):
        ip = input().split()
        p = int(ip[0])
        s = int(ip[1])
        if p in score:
            if s > score[p]:
                score[p] = s
        else:
            score[p] = s
    # print(score)
    for i in range(1, 9):
        if i in score:
            val += score[i]
    print(val)
    t -= 1
