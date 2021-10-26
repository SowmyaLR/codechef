'''
There are N students living in the dormitory of Berland State University. Each of them sometimes wants to use the kitchen, so the head of the dormitory came up with a timetable for kitchen's usage in order to avoid the conflicts:

The first student starts to use the kitchen at the time 0 and should finish the cooking not later than at the time A1.
The second student starts to use the kitchen at the time A1 and should finish the cooking not later than at the time A2.
And so on.
The N-th student starts to use the kitchen at the time AN-1 and should finish the cooking not later than at the time AN
The holidays in Berland are approaching, so today each of these N students wants to cook some pancakes. The i-th student needs Bi units of time to cook.

The students have understood that probably not all of them will be able to cook everything they want. How many students will be able to cook without violating the schedule?
'''


test = int(input())
while test>0:
    n = int(input())
    a = input().split()
    b = input().split()
    # print(a)
    a = [int(x) for x in a]
    b = [int(y) for y in b]
    tim = 0
    cnt = 0
    for t in range(0, n):
        tim = a[t] - tim
        if b[t]<=tim:
            cnt += 1
        tim = a[t]
    print(cnt)
    test -= 1


