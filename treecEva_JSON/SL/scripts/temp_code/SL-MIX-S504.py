import math
from contextlib import contextmanager

@contextmanager
def signal_processor():
    stats = {'processed': 0}
    try:
        yield stats
    finally:
        print(f"Processed {stats['processed']} candidates")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

candidates = [17, 28, 31, 49, 53, 64, 67, 81, 97]
frequency_pairs = [(a, b) for i, a in enumerate(candidates) for b in candidates[i+1:]]
valid_frequencies = [f for f in candidates if is_prime(f)]
valid_pairs = [(a,b) for a in valid_frequencies for b in valid_frequencies if a != b]

with signal_processor() as stats:
    stats['processed'] = len(candidates)
    # Dictionary comprehension for LCM computation
    lcm_map = {pair: (pair[0] * pair[1]) // math.gcd(pair[0], pair[1]) for pair in valid_pairs}
    
    # Merge with GCD map for analysis
    gcd_map = {pair: math.gcd(pair[0], pair[1]) for pair in valid_pairs}
    analysis_map = lcm_map | gcd_map
    
    # Harmonious pairs condition: LCM(a,b) == a*b implies GCD(a,b) == 1
    harmonious_pairs_count = sum(1 for pair, lcm_val in lcm_map.items() if lcm_val == pair[0] * pair[1])

print(f"Result: {harmonious_pairs_count}")