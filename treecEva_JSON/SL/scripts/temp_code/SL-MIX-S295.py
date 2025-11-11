from collections import deque
import math

def compute_volatility_score(fluctuations):
    window = deque(maxlen=5)
    squared_deviations = []
    
    for fluctuation in fluctuations:
        window.append(fluctuation)
        if len(window) == 5:
            mean_val = sum(window) / len(window)
            deviation_sum = sum((x - mean_val) ** 2 for x in window)
            squared_deviations.append(deviation_sum)
    
    if not squared_deviations:
        return 0.0
        
    max_dev = max(squared_deviations)
    min_dev = min(squared_deviations)
    
    if max_dev == min_dev:
        return 1.0
        
    current_dev = squared_deviations[-1]
    normalized_score = (current_dev - min_dev) / (max_dev - min_dev)
    return round(normalized_score, 6)

exchange_fluctuations = [0.02, -0.01, 0.03, -0.02, 0.01, 0.04, -0.03, 0.02, -0.01, 0.05]
normalized_score = compute_volatility_score(exchange_fluctuations)
print(f"Result: {normalized_score}")