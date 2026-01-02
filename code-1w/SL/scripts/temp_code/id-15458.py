from itertools import accumulate

def calculate_network_load():
    base_signals = [3, -1, 4, 1, -5, 9, 2]
    filtered = [x if x > 0 else 0 for x in base_signals]
    
    # Simulate cumulative propagation across network nodes
    propagated = list(accumulate(filtered, lambda acc, x: acc + x if acc + x < 10 else 5))
    
    # Rolling window effect over 3-node segments
    rolling_loads = []
    for i in range(len(propagated) - 2):
        rolling_loads.append(sum(propagated[i:i+3]))
    
    peak_capacity = max(rolling_loads)
    
    # Irrelevant diagnostic metric (distractor)
    avg_signal = sum(base_signals) / len(base_signals)
    
    print(f"Result: {peak_capacity}")

calculate_network_load()