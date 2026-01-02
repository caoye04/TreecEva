def filter_anomalies(readings_set):
    # Irrelevant transformation: converts to string and back
    str_converted = {str(x) for x in readings_set}
    reconverted = {int(x) for x in str_converted}
    
    # Distractor: unused statistical calculation
    mean_val = sum(reconverted) / len(reconverted) if reconverted else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in reconverted) / len(reconverted) if reconverted else 0
    
    # Actual filtering logic (only even numbers above threshold)
    filtered = {x for x in reconverted if x > 30 and x % 2 == 0}
    return filtered


def decode_signature(signal_tuple):
    # Dead code path — never executed in main flow
    a, b, c = signal_tuple
    if a < b < c:
        return a * 2 + b - c
    return 0


def aggregate_patterns(values):
    # Complex-looking but irrelevant grouping
    groups = {}
    for v in values:
        key = v // 10
        groups.setdefault(key, []).append(v)
    
    # Another decoy computation
    flat_sorted = sorted([item for group in groups.values() for item in group])
    
    # Real aggregation: sum of squares
    return sum(x * x for x in values)


def analyze_readings(valid_set):
    if not valid_set:
        return -1
    
    # Tuple unpacking red herring
    try:
        first, *middle, last = sorted(valid_set)
    except ValueError:
        first = last = list(valid_set)[0] if valid_set else 0
    
    # Bit manipulation distraction
    bit_encoded = 0
    for x in valid_set:
        bit_encoded ^= (x << 2) | (x >> 1)
    
    # Decoy recursive function that's defined but unused
    def recur_energy(n, acc=0):
        return acc if n <= 0 else recur_energy(n - 1, acc + n * 0.5)
    
    # Real diagnostic logic: count elements divisible by 4 minus min element
    count_div4 = sum(1 for x in valid_set if x % 4 == 0)
    min_value = min(valid_set)
    
    # Core result
    diagnostic_score = count_div4 * 100 - min_value
    
    # Multiple returns — only one matters
    if diagnostic_score < 0:
        return 0
    elif len(valid_set) > 5:
        return diagnostic_score + 50
    else:
        return diagnostic_score

# Main execution sequence
raw_data = {12, 15, 25, 32, 36, 41, 44, 48, 55, 63, 72}

# Unused derived sets — distractors
complement_set = {x for x in range(10, 80) if x not in raw_data}
squared_projections = {x**2 for x in raw_data if x < 50}

# Chain of processing
stable_readings = filter_anomalies(raw_data)

# Unused tuple operations
signature_triplet = (len(raw_data), sum(raw_data)//10, len(stable_readings))
decoded_sig = decode_signature(signature_triplet)  # Dead call

# Actual analysis
final_diagnostic = analyze_readings(stable_readings)

# Print final result as required
print(f"Result: {final_diagnostic}")