from sys import stdin

def input():
    return stdin.readline().rstrip()

N = int(input())
A = []
A += list(map(int, input().split()))
A_dict = {}
for ele in A:
    A_dict[ele] = True
M = int(input())
B = []
B += list(map(int, input().split()))

for ele in B:
    if ele in A_dict:
        print('1')
    else:
        print('0')