import heapq
from collections import deque

def calculate_bundle_profit(bundle):
    if len(bundle) <= 1:
        return sum(bundle)
    mid = len(bundle) // 2
    left_profit = calculate_bundle_profit(bundle[:mid])
    right_profit = calculate_bundle_profit(bundle[mid:])
    return left_profit + right_profit + (bundle[mid-1] * bundle[mid] if mid > 0 and mid < len(bundle) else 0)

class TransactionTracker:
    def __init__(self):
        self.transactions = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.transactions.clear()
    
    def add_transaction(self, profit):
        self.transactions.append(profit)
    
    def get_max_profit(self):
        profit_heap = []
        for profit in self.transactions:
            heapq.heappush(profit_heap, -profit)  # Max heap
        
        total = 0
        while profit_heap:
            current = -heapq.heappop(profit_heap)
            if current > 0:
                total += current
            else:
                break
        return total

def process_financial_data():
    exchange_rates = [1.02, 0.98, 1.05, 0.95, 1.03, 0.97, 1.01]
    profit_margins = []
    
    for i in range(1, len(exchange_rates)):
        margin = round((exchange_rates[i] - exchange_rates[i-1]) * 100, 2)
        profit_margins.append(margin)
    
    # Divide and conquer optimization on profit bundles
    optimized_margin = calculate_bundle_profit(profit_margins)
    
    # Greedy selection with priority queue
    with TransactionTracker() as tracker:
        tracker.add_transaction(optimized_margin)
        tracker.add_transaction(2.5)
        tracker.add_transaction(-1.2)
        tracker.add_transaction(3.7)
        tracker.add_transaction(-0.5)
        max_profit = tracker.get_max_profit()
    
    return max_profit

max_profit = process_financial_data()
print(f"Result: {max_profit}")