def analyze_pattern(sequence):
    return sum(x ** 2 for x in sequence if x % 2 == 0)

# Irrelevant helper function (dead code path)
def deprecated_normalization(data):
    return [x / max(data) for x in data]

def compute_entropy(values):
    from math import log2
    total = 0.0
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    for count in freq_map.values():
        p = count / len(values)
        total -= p * log2(p) if p > 0 else 0
    return round(total, 6)

# Misleading preprocessing block (distractor)
temp_log = [128, 64, 32, 16, 8]
scaling_factor = 0.5
adjusted_log = []
for val in temp_log:
    adjusted_log.append(int(val * scaling_factor))

# Unused transformation map (red herring)
symbol_mapping = {i: chr(65 + (i % 26)) for i in range(50)}

# Simulated sensor readings with embedded logic
sensor_data = [5, 10, 15, 20, 25, 30]
calibration_factor = 3
offset_correction = sum([i for i in range(3)])  # equals 3, distractor

# Decoy statistical calculation
mean_value = sum(sensor_data) / len(sensor_data)  # 17.5
variance_proxy = sum((x - mean_value) ** 2 for x in sensor_data) / len(sensor_data)

# Conditional expression usage (required feature)
threshold_status = 'high' if variance_proxy > 50 else 'normal'

# Core processing function with nested logic
def process_readings(readings, factor):
    base_shift = factor * 2
    transformed = []
    
    for val in readings:
        if val % 5 == 0:
            # Apply bit manipulation only on multiples of 5
            modified = (val ^ factor) + base_shift  # XOR then add
            if modified > 25:
                modified = modified >> 1  # Right shift if large
            transformed.append(modified)
        else:
            transformed.append(val)
    
    # Dictionary-based state tracking (cross-concept)
    status_count = {
        'elevated': 0,
        'normal': 0
    }
    
    for t in transformed:
        # Nested conditionals with conditional expression
        category = 'elevated' if t >= 16 else 'normal'
        status_count[category] += 1
    
    # Set-based uniqueness check (distractor)
    unique_flags = set(transformed)
    
    # Critical computation path
    raw_sum = sum(transformed)
    adjustment = len(unique_flags) if len(unique_flags) < 10 else 10
    
    # Final derivation using multiple concepts
    intermediate = raw_sum // adjustment  # Integer division
    
    # Secondary correction based on control flow history
    if status_count['elevated'] >= 3:
        intermediate = int(intermediate * 1.2)
    else:
        intermediate = int(intermediate * 0.9)
    
    # Final result derived through layered logic
    final_score = intermediate + (factor % 4)
    
    # Another red herring: unused recursive function inside scope
def hidden_reducer(n):
    return n if n <= 1 else n + hidden_reducer(n-2)

# Key execution point
final_diagnostic = process_readings(sensor_data, calibration_factor)

print(f"Result: {final_diagnostic}")