from collections import defaultdict, Counter

# Sensor simulation and diagnostic analysis system
def generate_sensor_data(seed=42):
    # Irrelevant data generation (red herring)
    base_values = [seed + i * 17 for i in range(20)]
    noise = [(i ** 2) % 13 for i in range(20)]
    return [base_values[i] + noise[i] for i in range(20)]

def filter_outliers(data, limit=500):
    # Misleading filtering function – not actually used in final computation
    return [x for x in data if x < limit]

def transform readings(readings):
    # Complex transformation with decoy logic
    shifted = [(r // 3) + (r % 11) for r in readings]
    scaled = [s * 2 if s % 2 == 0 else s * 3 for s in shifted]
    normalized = [n / max(scaled) * 100 for n in scaled]
    categorized = []
    for val in normalized:
        if val < 30:
            categorized.append('LOW')
        elif val < 70:
            categorized.append('MEDIUM')
        else:
            categorized.append('HIGH')
    return categorized

def compute_checksum(sequence):
    # Unused but plausible-sounding utility (dead code path)
    checksum = 0
    for i, item in enumerate(sequence):
        checksum += (i + 1) * hash(str(item)) % 19
    return checksum % 1000

def build_threshold_map(labels):
    # Relevant: builds mapping used later
    freq = Counter(labels)
    map_weights = defaultdict(float)
    total = sum(freq.values())
    for label, count in freq.items():
        map_weights[label] = round((count / total) * 100, 3)
    # Add dummy keys to obscure real usage
    map_weights['UNKNOWN'] = 0.0
    map_weights['ERROR'] = -1.0
    return map_weights

def decode_signature(sig_list):
    # Distractor function that looks important but is never called
    result = 0
    for i, val in enumerate(sig_list):
        result ^= (val << (i % 5))
    return result & 0xFFFF

def recursive_condense(values, depth=0):
    # Decoy recursion – appears computationally heavy but unused
    if depth >= 3 or len(values) == 1:
        return values[0] if values else 0
    new_vals = [(values[i] + values[i+1]) // 2 for i in range(0, len(values)-1, 2)]
    return recursive_condense(new_vals, depth + 1)

def preprocess_readings(raw):
    # Relevant preprocessing step
    adjusted = [r - 10 for r in raw]
    squared_if_odd = [x**2 if x % 2 == 1 else x for x in adjusted]
    return [x for x in squared_if_odd if x > 0]  # Remove negatives

def analyze_readings(clean_data, thresholds):
    # Core logic with subtle dependency on prior steps
    stats = defaultdict(int)
    for val in clean_data:
        if val > 500:
            stats['extreme'] += 1
        elif val > 250:
            stats['high'] += 1
        elif val > 100:
            stats['moderate'] += 1
        else:
            stats['normal'] += 1
    
    # Critical calculation path
    category_score = 0
    category_score += stats['extreme'] * 8
    category_score += stats['high'] * 4
    category_score += stats['moderate'] * 2
    category_score += stats['normal'] * 1
    
    # Weighting using threshold map (only 'HIGH' and 'MEDIUM' matter)
    modifier = 1.0
    if 'HIGH' in thresholds and thresholds['HIGH'] > 20.0:
        modifier *= 1.5
    if 'MEDIUM' in thresholds and thresholds['MEDIUM'] > 30.0:
        modifier *= 0.8
    
    intermediate = category_score * modifier
    
    # Final transformation using bit manipulation red herring
    temp = int(intermediate)
    temp = (temp ^ 0xAAAA) & 0xFFFF  # Bitwise decoy
    temp = (temp ^ 0x5555) & 0xFFFF  # Reverse the decoy
    
    # Actual final adjustment
    final_value = temp - 50  # Key offset
    
    # Dead code branch – never reached due to structure
    if False:
        backup = recursive_condense(clean_data)
        final_value = backup * 2
    
    return final_value

# --- Main Execution Flow ---
raw_sensor_data = generate_sensor_data(seed=42)

# Unused filtered version (distractor)
filtered_data = filter_outliers(raw_sensor_data, limit=400)

# Preprocess the original data
processed_data = preprocess_readings(raw_sensor_data)

# Transform into categories for threshold analysis
labeled_readings = transform_readings(raw_sensor_data)

# Build dynamic threshold map based on distribution
threshold_map = build_threshold_map(labeled_readings)

# Analyze the processed data with context-aware thresholds
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")