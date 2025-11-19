import itertools
from collections import defaultdict

# Signal strength matrix: rows=frequency bands, columns=time intervals
signal_matrix = [
    [3, 1, 4, 1, 5],
    [9, 2, 6, 5, 3],
    [5, 8, 9, 7, 9],
    [3, 2, 3, 8, 4]
]

threshold = 4
critical_energy = 50
signal_alerts = 0

for band in signal_matrix:
    # Check for consecutive signals above threshold
    consecutive_high = False
    for i in range(len(band) - 1):
        if band[i] > threshold and band[i+1] > threshold:
            consecutive_high = True
            break
    
    # Calculate total energy if consecutive high signals found
    if consecutive_high:
        energy = sum(x**2 for x in band)
        if energy > critical_energy:
            signal_alerts += 1

print(f"Result: {signal_alerts}")