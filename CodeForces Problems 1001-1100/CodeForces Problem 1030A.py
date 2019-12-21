n = int(input())
scores = [int(i) for i in input().split()]
if sum(scores) > 0:
    print('HARD')
else:
    print('EASY')
