import math

def analyze_signal_strength(signal):
    # Irrelevant analysis function (dead code path)
    if len(signal) == 0:
        return 0
    peak = max(abs(x) for x in signal)
    return round(peak * 1.05, 2)

def transform_coordinates(coords):
    # Distractor: unused coordinate transformation
    transformed = []
    for x, y in coords:
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        transformed.append((r, theta))
    return transformed

def compute_entropy(sequence):
    # Misleading computation: looks important but unused
    from collections import Counter
    freq = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def recursive_filter(values, threshold, depth=0):
    # Recursion with early termination (used in main logic)
    if depth >= 5 or len(values) == 0:
        return [v for v in values if v > threshold * 0.75]
    filtered = [v for v in values if v > threshold]
    if len(filtered) < 2:
        return recursive_filter([v+1 for v in values], threshold, depth+1)
    return filtered

def decode_sequence(text_data):
    # String processing: used to distract and add complexity
    cleaned = text_data.strip().lower()
    tokens = cleaned.split(',')
    numeric_parts = []
    for token in tokens:
        stripped = token.strip()
        if stripped.isdigit():
            numeric_parts.append(int(stripped))
        elif stripped.replace('.', '').isdigit():
            numeric_parts.append(float(stripped))
    return numeric_parts

def validate_checksum(items):
    # Decoy validation function that's never called
    checksum = 0
    for item in items:
        if isinstance(item, int):
            checksum ^= item
        elif isinstance(item, float):
            checksum += int(item)
    return checksum % 17 == 0

def process_pipeline(raw_input):
    # Main processing chain with key logic embedded
    segment_a = [x * 1.5 for x in raw_input if x % 2 == 0]
    segment_b = [x for x in raw_input if x % 3 == 0 and x % 2 != 0]
    
    # Conditional expression: python idiom
    base_values = segment_a if len(segment_a) > len(segment_b) else segment_b + [0]
    
    # Apply recursive filtering (critical step)
    refined = recursive_filter(base_values, threshold=8.0)
    
    # Some irrelevant transformations
    stats = {
        'count': len(refined),
        'sum': sum(refined),
        'max': max(refined) if refined else 0,
        'flag': 'valid' if len(refined) > 3 else 'low_res'
    }
    
    # Bit manipulation red herring
    magic_key = 0
    for i in range(len(refined)):
        magic_key ^= int(refined[i]) << 1
        magic_key |= (i & 3)
    
    # Core calculation disguised among distractors
    temp_result = 0
    for val in refined:
        if val > 10:
            temp_result += int(val) // 2
        else:
            temp_result += int(val) * 2
    
    # Final adjustment using string method as distraction
    tag = "output_v2".upper().replace('_', '')
    version_code = sum(ord(c) for c in tag) % 19
    
    # Actual answer formation
    final_value = temp_result - version_code
    
    # Dead code: never reached
    if final_value < 0:
        backup = math.gamma(final_value + 5)
        return int(backup)
        
    return final_value

# Simulated sensor data chunk (real input)
data_chunk = [4, 6, 9, 12, 15, 18, 7, 21]

# Irrelevant pre-processing (distractor)
signal_data = [-1.2, 0.5, 3.8, 2.1, -0.9]
coordinate_grid = [(1,1), (2,3), (4,2)]
raw_text_stream = "12, 3.5, abc, 7, 9.1, x"

# Unused entropy computation (misdirection)
entropy_metric = compute_entropy([1,1,2,3,3,3,4])

# Key execution point
final_output = process_pipeline(data_chunk)

# Output result as required
print(f"Result: {final_output}")