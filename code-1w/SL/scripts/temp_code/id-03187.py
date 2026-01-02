def transform(values):
    # Irrelevant transformation (dead logic path)
    temp = [v * 1.5 for v in values if v % 2 == 0]
    adjusted = [x for x in values if x > 0]
    return adjusted[::-1]  # Reverse, but not used in final logic

def filter_and_shift(seq):
    # Distractor: complex-looking bit manipulation with no real impact
    masked = [(s << 1) ^ 3 for s in seq]
    cleaned = [s for s in seq if s % 3 != 0]
    shifted = cleaned[1:] + [cleaned[0]]  # Rotate left by 1
    return shifted  # Unused return

def compute_hash(chunk):
    # Meaningless hash-like computation (red herring)
    acc = 0
    for i, c in enumerate(chunk):
        acc += c * (i + 1) ^ 7
    return acc % 1000

def extract_features(series):
    # Real logic begins here — slice middle third
    n = len(series)
    start = n // 3
    end = 2 * n // 3
    segment = series[start:end]
    
    # Apply conditional doubling on even indices
    processed = []
    for i, val in enumerate(segment):
        if i % 2 == 0:
            processed.append(val * 2)
        else:
            processed.append(val)
    
    # Further slicing: take first half of processed
    mid = len(processed) // 2
    reduced = processed[:mid]
    
    # Sum with alternating signs
    total = 0
    for j, num in enumerate(reduced):
        if j % 2 == 0:
            total += num
        else:
            total -= num
    return total

def validate_structure(arr):
    # Dead code path — never called in execution
    if len(arr) < 5:
        return False
    return all(a <= b for a, b in zip(arr, arr[1:]))

def process_sequence(raw_data):
    # Entry point with distractions
    backup = raw_data.copy()
    backup.append(sum(raw_data))  # Fake data augmentation
    
    # Decoy operations
    dummy_pairs = [(x, y) for x in raw_data[:4] for y in raw_data[-4:] if x != y]
    pair_sum = sum(p[0] + p[1] for p in dummy_pairs[:10]) if len(dummy_pairs) > 5 else 0
    
    # Actual meaningful slicing
    trimmed = raw_data[2:-2]  # Remove two from front and back
    
    # Pass through filtering that doesn't change much
    filtered = [x for x in trimmed if x >= 0]
    
    # Now apply feature extraction which contains real logic
    result = extract_features(filtered)
    
    # Extra obfuscation: attempt to modify result with irrelevant math
    noise = compute_hash([len(filtered), pair_sum % 100])
    final_adjustment = (noise * 0.01) if noise > 500 else 0
    result = int(result - final_adjustment)  # final_adjustment is always 0 since noise < 500
    
    return result

# Main execution
if __name__ == '__main__':
    # Input sequence with purposeful structure
    data = [3, -1, 4, 1, 5, 9, 2, 6, -8, 3]
    
    # Call main processing function
    result = process_sequence(data)
    
    # Print result as required
    print(f"Result: {result}")