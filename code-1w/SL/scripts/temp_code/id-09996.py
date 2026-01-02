import math

# Simulated sensor data processing with embedded logic chain
def collect_readings():
    raw = [i * 0.5 + (i % 7) for i in range(15)]
    offset = 3.14
    adjusted = []
    for val in raw:
        if val > 10:
            adjusted.append(val + offset)
        elif val < 4:
            adjusted.append(val * 1.5)
        else:
            adjusted.append(val + 0.1)
    return adjusted

# Irrelevant transformation - red herring
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Distractor function - never called in execution path
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Another decoy - processes unrelated synthetic sequence
def generate_synthetic():
    seq = []
    a, b = 1, 1
    for _ in range(10):
        seq.append(a)
        a, b = b, a + b
    return [x * 0.1 for x in seq]

# Core transformation - actually used
def transform_sequence(signal):
    shifted = [math.sin(x) * 100 for x in signal]
    filtered = [y for y in shifted if abs(y) > 10]
    normalized = []
    max_val = max(abs(min(filtered)), abs(max(filtered)))
    for val in filtered:
        normalized.append(round(val / max_val * 50))
    return normalized

# Auxiliary diagnostic (distractor)
def assess_stability(pattern):
    diffs = [pattern[i+1] - pattern[i] for i in range(len(pattern)-1)]
    variance = sum(d**2 for d in diffs) / len(diffs)
    return variance < 5

# Main analysis function with critical computation
prev_cache = {}
def analyze_pattern(data):
    global prev_cache
    result = 0
    temp_log = []
    
    # Complex conditional accumulation
    for i, val in enumerate(data):
        if i % 3 == 0 and val > 0:
            result += int(val) // 3
        elif i % 4 == 0 and val < 0:
            result -= abs(int(val)) % 7
        else:
            result += (val * i) % 5
        
        # Logging irrelevant intermediate
        temp_log.append(f"Step {i}: {result}")
    
    # Secondary adjustment based on bit properties
    bit_score = 0
    binary_rep = bin(abs(result))[2:]
    for j, bit in enumerate(binary_rep):
        if bit == '1':
            bit_score += j * (-1)**j
    
    final_adjustment = 0
    # Conditional override that doesn't trigger due to logic
    if len(binary_rep) > 10 and result % 2 == 0:
        final_adjustment = 50
    else:
        final_adjustment = -25
    
    # Actual answer contribution
    checksum = sum(int(d) for d in str(abs(result))[:3])
    return result + bit_score + final_adjustment + checksum

# Unused buffer initialization - dead code path
buffer_pool = [[0]*8 for _ in range(4)]

# Entry point
if __name__ == "__main__":
    readings = collect_readings()
    
    # Apply actual transformation
    transformed_data = transform_sequence(readings)
    
    # Multiple unused computations - distractions
    dummy_1 = smooth_signal(readings)
    dummy_2 = generate_synthetic()
    dummy_3 = [math.cos(x) for x in readings[:5]]
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")