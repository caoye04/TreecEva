import math

def transform_value(x):
    # Irrelevant transformation (dead function)
    return (x ** 2 + 3 * x + 1) % 100

def decode_signal(signal):
    # Distractor: complex-looking but unused decoding
    decoded = []
    for s in signal:
        if s % 3 == 0:
            decoded.append(s // 3)
        elif s % 5 == 0:
            decoded.append(s // 5)
        else:
            decoded.append(s)
    return [d for d in decoded if d % 2 == 0]

def analyze_pattern(seq):
    # Heavily distracting analysis with no impact on final result
    stats = {
        'max': max(seq),
        'min': min(seq),
        'range': max(seq) - min(seq),
        'median': sorted(seq)[len(seq)//2],
        'mode': max(set(seq), key=seq.count),
        'entropy': 0.0
    }
    total = 0
    for item in seq:
        if item > 0:
            total += item * math.log(item)
    stats['entropy'] = round(total, 4)
    
    # Fake aggregation path
    temp_agg = 0
    for i in range(len(seq)):
        if i % 2 == 0 and seq[i] % 4 == 0:
            temp_agg += seq[i]
    stats['temp_agg'] = temp_agg
    
    return stats

def filter_critical_data(stream):
    # Real filtering logic buried in noise
    result = []
    threshold = sum(stream) / len(stream)
    for val in stream:
        if val >= threshold and val % 2 == 1:  # Only odd values above average
            result.append(val)
    return result

def recursive_compress(arr, depth=0):
    # Actual relevant recursive function
    if depth >= 3 or len(arr) <= 1:
        return arr[0] if arr else 1
    compressed = []
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            compressed.append((arr[i] + arr[i+1]) // 2)
        else:
            compressed.append(arr[i])
    return recursive_compress(compressed, depth + 1)

def calculate_entropy_score(values):
    # Another decoy function that looks important
    if not values:
        return 0.0
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    score = 0.0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        score -= p * math.log2(p)
    return round(score, 4)

def process_sequence(data):
    # Core logic mixed with distractions
    temp_data = data.copy()
    
    # Distractor block: complex dictionary operations
    diagnostics = {
        'input_length': len(temp_data),
        'initial_sum': sum(temp_data),
        'flags': [False, True, False],
        'history': {},
        'snapshot': tuple(temp_data[:5])
    }
    
    # Irrelevant conditional path
    if len(temp_data) > 100:
        sample = temp_data[::10]
        diagnostics['sample_avg'] = sum(sample) / len(sample)
    else:
        diagnostics['complex_flag'] = (len(temp_data) ** 2) > 50
    
    # Real computation begins here — buried in noise
    filtered = filter_critical_data(temp_data)
    
    # More red herring: fake entropy usage
    diagnostics['entropy_estimate'] = calculate_entropy_score(filtered)
    
    # Key transformation
    adjusted = [f * 2 for f in filtered if f != 7]  # Exclude 7s
    
    # Dead code: never used
    if any(x > 50 for x in adjusted):
        diagnostics['overflow_risk'] = True
    
    # Actual core: recursive compression determines final output
    raw_result = recursive_compress(adjusted)
    
    # Final adjustment using unrelated constant
    multiplier = len(diagnostics['flags'])  # Always 3
    final_value = raw_result * multiplier
    
    # This is the actual answer variable
    final_output = int(final_value)
    
    # Print required at end
    print(f"Target result: {final_output}")
    return final_output

# Main execution
if __name__ == '__main__':
    # Input data with meaningful structure
    data_stream = [5, 8, 12, 15, 21, 22, 25, 26, 28, 33, 35, 39, 40, 42, 45]
    
    # Decoy variables and computations
    baseline = 17
    offset_correction = []
    for x in data_stream:
        offset_correction.append((x + baseline) % 13)
    
    # Unused transformed version
    signal_input = [x * 3 + 2 for x in offset_correction if x % 2 == 0]
    
    # Real call that produces the answer
    final_output = process_sequence(data_stream)
