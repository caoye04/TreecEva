import heapq
import statistics

def process_financial_data():
    raw_transactions = [120.5, -89.3, 450.2, -1200.7, 330.1, 220.8, -310.4]
    normalized = [(x - statistics.mean(raw_transactions)) / statistics.stdev(raw_transactions) for x in raw_transactions]
    outliers_removed = [x for x in normalized if abs(x) <= 2]
    squared_deviations = list(map(lambda x: x**2, outliers_removed))
    
    # Max-heap implementation using negative values
    max_heap = []
    for dev in squared_deviations:
        heapq.heappush(max_heap, -dev)
    
    # Extract top 3 volatility measures
    top_volatilities = [-heapq.heappop(max_heap) for _ in range(min(3, len(max_heap)))]
    peak_volatility = sum(top_volatilities) / len(top_volatilities) if top_volatilities else 0
    
    return peak_volatility

result = process_financial_data()
print(f"Result: {result}")