import heapq

def fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Asset performance returns
asset_returns = [0.05, 0.03, 0.07, 0.02, 0.06]
weights = [fibonacci(i+1) for i in range(len(asset_returns))]
weighted_returns = [ret * weight for ret, weight in zip(asset_returns, weights)]

# Min-heap to keep top 3 assets
portfolio_heap = []
for wr in weighted_returns:
    if len(portfolio_heap) < 3:
        heapq.heappush(portfolio_heap, wr)
    elif wr > portfolio_heap[0]:
        heapq.heapreplace(portfolio_heap, wr)

top_asset_weight = max(portfolio_heap)
print(f"Result: {top_asset_weight}")