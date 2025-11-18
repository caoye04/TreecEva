import heapq

ingredients = [42, 18, 73, 29, 55, 64, 37]
selected = []
heap = [-x for x in ingredients]
heapq.heapify(heap)

for _ in range(3):
    selected.append(-heapq.heappop(heap))

total_priority = sum(selected)
print(f"Result: {total_priority}")