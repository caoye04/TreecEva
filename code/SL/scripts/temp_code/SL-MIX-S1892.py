import heapq
from collections import namedtuple
from contextlib import contextmanager

event_data = namedtuple('Event', ['timestamp', 'rate', 'volume'])

@contextmanager
def exchange_monitor():
    print("Initializing exchange monitor...")
    yield
    print("Exchange monitoring completed.")

def calculate_threshold(base_rate):
    return lambda fluctuation: base_rate * (1 + fluctuation / 100)

events = [
    event_data(1, 1.20, 1000),
    event_data(2, 1.25, 1500),
    event_data(3, 1.18, 800),
    event_data(4, 1.30, 2000),
    event_data(5, 1.22, 1200),
    event_data(6, 1.28, 900),
    event_data(7, 1.19, 700)
]

with exchange_monitor():
    max_heap = []  # Using negative values for max heap simulation
    min_heap = []
    base_rate = events[0].rate
    threshold_func = calculate_threshold(base_rate)
    profit_tracker = 0
    optimal_profit = 0
    
    for event in events:
        if event.rate > threshold_func(2):  # 2% threshold
            heapq.heappush(max_heap, -event.rate)
        elif event.rate < threshold_func(-1):  # -1% threshold
            heapq.heappush(min_heap, event.rate)
        
        if len(max_heap) > 2 and len(min_heap) > 1:
            best_sell = -heapq.heappop(max_heap)
            best_buy = heapq.heappop(min_heap)
            profit_tracker += (best_sell - best_buy) * min(event.volume, 1000)
            if profit_tracker > optimal_profit:
                optimal_profit = profit_tracker
            else:
                break  # Early termination if no improvement
        
        # Update threshold dynamically
        if len(max_heap) > 0:
            base_rate = -max_heap[0]
            threshold_func = calculate_threshold(base_rate)

print(f"Result: {optimal_profit}")