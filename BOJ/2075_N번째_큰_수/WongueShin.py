import sys
import heapq

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
heap = []

for _ in range(N):
	nums = list(map(int, read().split()))

	if not heap:
		for num in nums:
			heapq.heappush(heap, num)
        
	else:
		for num in nums:
			if heap[0] < num:
				heapq.heappush(heap, num)
				heapq.heappop(heap)

print(heap[0])