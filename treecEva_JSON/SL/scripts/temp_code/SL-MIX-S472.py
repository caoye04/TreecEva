from math import gcd
from functools import reduce
from collections import defaultdict

def compute_sync_score(peaks):
    if len(peaks) <= 1:
        return len(peaks)
    
    # Calculate all pairwise absolute differences
    differences = set()
    for i in range(len(peaks)):
        for j in range(i+1, len(peaks)):
            diff = abs(peaks[i] - peaks[j])
            if diff > 0:
                differences.add(diff)
    
    # If all differences are zero (should not happen if len>1 and distinct), return count
    if not differences:
        return len(peaks)
    
    # Compute GCD of all differences
    sync_score = reduce(gcd, differences)
    return sync_score

# Timestamps of detected signal peaks
signal_peaks = [12, 28, 44, 60, 76]

sync_score = compute_sync_score(signal_peaks)
print(f"Result: {sync_score}")