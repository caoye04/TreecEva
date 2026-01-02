from collections import Counter

def find_unique_element(pairs, choices):
    # Compute XOR of all pair results
    pair_xor = 0
    for a, b in pairs:
        pair_xor ^= (a * 2) ^ b

    # Find candidate whose frequency is odd
    freq = Counter(choices)
    odd_freq_value = None
    for val, count in freq.items():
        if count % 2 == 1:
            odd_freq_value = val
            break
    
    # Final result combines XOR logic and frequency anomaly
    result = pair_xor + odd_freq_value
    return result

# Input data
xor_pairs = [(12, 8), (7, 3), (12, 5), (9, 8)]
candidates = [5, 5, 12, 12, 12, 3, 3]

# Additional unrelated variables (minimal interference)
dummy_flag = True
temp_buffer = [0] * 4

result = find_unique_element(xor_pairs, candidates)
print(f"Result: {result}")