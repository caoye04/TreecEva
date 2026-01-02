from collections import defaultdict, Counter
import math

# Simulated sensor data processing with noise filtering and pattern analysis
def preprocess_readings(raw_readings):
    filtered = []
    noise_floor = 0.05
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(round(val * 100) // 10)  # Normalize and discretize
    return filtered

# Irrelevant helper - simulates temperature conversion (not used in final result)
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Secondary transformation: group by magnitude bands
def categorize_magnitude(values):
    bands = defaultdict(int)
    for v in values:
        band = abs(v) // 5
        bands[band] += 1
    return bands

# Misleading aggregation path - looks important but unused
def compute_entropy(count_dict):
    total = sum(count_dict.values())
    entropy = 0
    for count in count_dict.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core pattern extraction based on frequency and transitions
def extract_transitions(data):
    if not data:
        return []
    transitions = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        transitions.append(diff % 7)  # Wrap differences into 0-6 range
    return transitions

# Decoy function: appears to do security hashing but irrelevant
def generate_checksum(seq):
    checksum = 0
    for i, x in enumerate(seq):
        checksum ^= (x * (i + 1)) % 23
    return checksum

# Main analysis: combines frequency, transition cycles, and symmetry
def analyze_patterns(data_seq, ref_map):
    freq = Counter(data_seq)
    total_unique = len(freq)
    
    # Compute weighted score based on reference importance
    base_score = 0
    for k, v in freq.items():
        if k in ref_map:
            base_score += v * ref_map[k]
    
    # Transition cycle analysis
    trans = extract_transitions(data_seq)
    cycle_signature = sum((t * (i+1)) % 5 for i, t in enumerate(trans[:10]))
    
    # Symmetry check
    reversed_data = list(reversed(data_seq))
    match_count = sum(1 for a, b in zip(data_seq, reversed_data) if a == b)
    symmetry_ratio = match_count / len(data_seq) if data_seq else 0
    
    # Dummy weight adjustment (red herring)
    adjustment_factor = 1.0
    if total_unique > 5:
        adjustment_factor *= 0.9
    if symmetry_ratio > 0.6:
        adjustment_factor *= 1.1
    
    # Final diagnostic formula - only some components are actually impactful
    local_diagnostic = int((base_score * 3) + cycle_signature - (10 * total_unique))
    
    # Dead code branch - never executed due to data constraints
    anomaly_flag = False
    if min(data_seq) < -50 or max(data_seq) > 50:
        anomaly_flag = True  # Unreachable with current data
    
    return local_diagnostic

# Unused statistical summary (distractor)
def summarize_distribution(vals):
    mean_val = sum(vals) / len(vals) if vals else 0
    variance = sum((x - mean_val)**2 for x in vals) / len(vals) if vals else 0
    return {'mean': round(mean_val, 3), 'variance': round(variance, 3)}

# --- Execution Pipeline ---

# Raw sensor input (simulated)
sensor_stream = [
    0.12, -0.03, 0.45, 0.23, -0.15, 0.67, 0.45, 0.23, 0.89, -0.02,
    0.12, 0.45, 0.67, 0.23, 0.45, 0.12, 0.89, 0.67, 0.45, 0.23
]

# Step 1: Preprocess raw readings
processed_signal = preprocess_readings(sensor_stream)

# Step 2: Apply magnitude categorization (distractor)
mag_groups = categorize_magnitude(processed_signal)

# Step 3: Generate unused entropy metric
entropy_metric = compute_entropy(mag_groups)  # Computed but not used

# Step 4: Transform data using secondary mapping
scaling_map = {x: (x % 4) + 1 for x in range(20)}
transformed_data = [scaling_map[x] if x in scaling_map else 1 for x in processed_signal]

# Step 5: Build reference importance map (used in analysis)
reference_map = defaultdict(int)
for i in range(1, 6):
    reference_map[i] = ((i ** 2) % 7) + 3

# Step 6: Introduce decoy checksum (irrelevant computation)
security_hash = generate_checksum(transformed_data)  # Dead end

# Step 7: Perform main analysis
final_diagnostic = analyze_patterns(transformed_data, reference_map)

# Output result
print(f"Result: {final_diagnostic}")