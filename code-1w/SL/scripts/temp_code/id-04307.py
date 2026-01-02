import itertools

def generate_sequence(base, length):
    """Generate a misleading sequence for distraction."""
    return [base * (i ** 2) for i in range(1, length + 1)]

def apply_filter(data, limit):
    """Irrelevant filtering function that's never used in critical path."""
    return [x for x in data if x % 2 == 0 and x < limit]

def compute_checksum(values):
    """Decoy function: looks important but not part of final result."""
    checksum = 0
    for v in values:
        checksum ^= v
        checksum = (checksum + 17) % 97
    return checksum

def recursive_reduce(n, depth=0):
    """A red herring recursive function with exponential distraction."""
    if n <= 1 or depth > 5:
        return n
    return recursive_reduce(n // 2, depth + 1) + recursive_reduce(n // 3, depth + 1)

def transform_signal(raw):
    """Apply non-linear transformation to signal array."""
    adjusted = [(x * 1.5) + 2.0 for x in raw]
    smoothed = [sum(adjusted[i:i+3]) / 3 for i in range(len(adjusted) - 2)]
    return [round(x, 2) for x in smoothed]

def detect_anomalies(stream, sensitivity):
    """Another distractor: detects anomalies but result unused."""
    bounds = sensitivity * 3.5
    return [i for i, val in enumerate(stream) if abs(val) > bounds]

def analyze_pattern(seq, cutoff):
    """Core logic: counts alternating segments above cutoff."""
    count = 0
    in_segment = False
    last_was_high = False

    for val in seq:
        is_high = val > cutoff
        if is_high and not in_segment:
            count += 1
            in_segment = True
            last_was_high = True
        elif not is_high and in_segment:
            in_segment = False
            last_was_high = False
    
    # Secondary pattern: must have even number of transitions
    transition_count = sum(
        1 for a, b in zip(seq, seq[1:]) 
        if (a > cutoff) != (b > cutoff)
    )
    
    if transition_count % 2 == 0:
        count *= 2
    else:
        count += 5

    return count

# --- Main execution with heavy interference ---

# Irrelevant data generation
phantom_data = generate_sequence(7, 12)
dummy_checksum = compute_checksum(phantom_data[:8])
recursive_trace = recursive_reduce(27)

# Real input data (simulated sensor readings)
sensor_readings = [1.2, 4.8, 2.1, 6.3, 3.9, 5.5, 1.0, 4.4, 6.6]

# Apply actual transformation
transformed_data = transform_signal(sensor_readings)  # Result: [4.0, 5.4, 4.85, 5.9, 5.0, 5.5]

# Unused anomaly detection
anomaly_indices = detect_anomalies(transformed_data, sensitivity=4.0)

# Fake filter application on irrelevant data
junk_filtered = apply_filter(phantom_data, 100)

# Critical control variables
threshold = 4.7
mode_flag = len(transformed_data) % 2

# Key intermediate computation (distraction)
aggregated = sum(transformed_data) / len(transformed_data)
fluctuation_score = sum(
    abs(a - b) for a, b in zip(transformed_data, transformed_data[1:])
)

# Core analysis using correct logic chain
temp_diagnostic = analyze_pattern(transformed_data, threshold)

# Final branching logic based on fluctuation (distraction check)
if fluctuation_score > 5.0:
    final_diagnostic = temp_diagnostic + 1
else:
    final_diagnostic = temp_diagnostic - 1

# Additional decoy manipulation (never affects final result)
buffer = list(itertools.accumulate([int(x) for x in transformed_data]))
shifted = [b << 1 for b in buffer if b % 3 == 0]
encoded = ''.join(chr(97 + (b % 26)) for b in shifted[:3]) if shifted else 'xyz'

# Output the required result
print(f"Result: {final_diagnostic}")