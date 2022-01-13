# https://codeforces.com/problemset/problem/1075/A
n = int(input())
x, y = map(int, input().split())
if x + y > n + 1:
    print('Black')
else:
    print('White')
