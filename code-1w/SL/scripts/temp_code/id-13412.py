from collections import defaultdict, Counter
import math

# Irrelevant helper functions (distractors)
def calculate_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def generate_checksum(sequence):
    checksum = 0
    for i, char in enumerate(sequence):
        checksum += ord(char) * (i + 1)
    return checksum % 1000

def validate_entry(record):
    if not record.get('active'):
        return False
    if record.get('version', 0) < 2:
        return False
    return True

# Core logic with meaningful computation mixed with distractions
def transform_sequence(seq):
    # Some bitwise manipulation (partly relevant, partly red herring)
    transformed = []
    for item in seq:
        temp = (item ^ 255) & 127
        if temp % 2 == 0:
            temp = temp >> 1
        transformed.append(temp)
    return transformed

def analyze_frequency(pattern):
    freq = Counter(pattern)
    ranked = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [k for k, _ in ranked]

def compute_weighted_sum(values, multipliers):
    # Actual core component used later
    return sum(v * m for v, m in zip(values, multipliers))

def extract_features(dataset):
    features = defaultdict(float)
    temp_data = []
    
    for entry in dataset:
        x = entry['x']
        y = entry['y']
        z = entry['z']
        
        # Distractor computations
        magnitude = math.sqrt(x**2 + y**2 + z**2)
        direction = math.atan2(y, x)
        normalized_z = z / (magnitude if magnitude else 1)
        
        # Real feature extraction
        if x > 0 and y < 50:
            features['positive_x_low_y'] += 1
        if z % 7 == 0:
            features['divisible_by_7'] += z // 7
        
        temp_data.append(magnitude * direction)
    
    # This part is actually unused but looks important
    entropy = calculate_entropy([int(f) for f in features.values() if f > 0])
    features['entropy_proxy'] = round(entropy, 3)
    
    return dict(features)

def process_metrics(raw_data, importance_weights):
    # Step 1: Extract structural features (some irrelevant)
    extracted = extract_features(raw_data)
    
    # Step 2: Transform raw values through distraction pipeline
    raw_values = [d['metric'] for d in raw_data]
    transformed_values = transform_sequence(raw_values)
    ranked_indices = analyze_frequency(transformed_values)
    
    # Step 3: Compute actual weighted contribution (key step)
    base_contributions = [v * 0.7 + 3 for v in transformed_values]
    
    # Step 4: Apply correct weighting using lambda for functional style
    apply_bonus = lambda val: val * 1.25 if val > 60 else val * 0.9
    adjusted = [apply_bonus(val) for val in base_contributions]
    
    # Step 5: Use only first N aligned with weights (critical alignment)
    aligned = adjusted[:len(importance_weights)]
    
    # Step 6: Compute final score (this is the answer)
    final_score = compute_weighted_sum(aligned, importance_weights)
    
    # Red herring: checksum on stringified data
    debug_tag = ''.join(chr(v % 97 + 33) for v in raw_values[:5])
    validation_code = generate_checksum(debug_tag)
    
    # Dead branch - never executed due to constant condition
    if len(debug_tag) > 100:
        fallback = sum(transformed_values) / len(transformed_values)
        final_score = fallback * 0.85
    
    return final_score

# Simulated input data
input_data = [
    {'x': 12, 'y': 45, 'z': 14, 'metric': 88, 'active': True, 'version': 3},
    {'x': -5, 'y': 60, 'z': 21, 'metric': 72, 'active': True, 'version': 2},
    {'x': 8, 'y': 33, 'z': 28, 'metric': 95, 'active': True, 'version': 4},
    {'x': 15, 'y': 70, 'z': 35, 'metric': 64, 'active': False, 'version': 1},
    {'x': 3, 'y': 25, 'z': 42, 'metric': 81, 'active': True, 'version': 5}
]

weights_scheme = [0.4, 0.6, 0.5, 0.3]  # Only first four used

# Key execution point
final_score = process_metrics(input_data, weights_scheme)

print(f"Result: {final_score}")