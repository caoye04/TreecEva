import itertools

# Simulated sensor data processing pipeline for environmental monitoring station
def analyze_readings(readings):
    filtered = [x for x in readings if 10 <= x <= 100]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    anomalies = list(filter(lambda x: x > 85, smoothed))
    return len(anomalies) > 0, sum(smoothed) / len(smoothed) if smoothed else 0

# Irrelevant helper - dead code path (never called)
def legacy_calibrate(data):
    return [d * 0.95 for d in data if d > 5]

# Data validation with red herring logic
def validate_sequence(seq):
    if not seq:
        return False
    checksum = sum(seq[i] * (i + 1) for i in range(len(seq)))
    expected = len(seq) * (len(seq) + 1) // 2
    # Distractor: this looks important but isn't used in main logic
    deviation = abs(checksum - expected * 7) if expected else 0
    return checksum % 9 == 0

# Core transformation with slicing and combinatorics
def generate_patterns(values):
    rotated = values[2:] + values[:2]  # slice rotation
    pairs = list(itertools.combinations(rotated, 2))
    products = [a * b for a, b in pairs if a != b]
    # Decoy aggregation
    dummy_agg = sum(p ** 0.5 for p in products[:10]) if len(products) > 5 else 0
    return sorted(set(products))

# Secondary metric processor (partially relevant)
def compute_density(area, count):
    if area <= 0:
        return 0
    base = count / area
    adjusted = base * 1.75 if base > 3 else base * 0.85
    # Unused distracting variant
    normalized = (adjusted - 1) / (adjusted + 1) if adjusted >= 1 else 0
    return adjusted

# Misleading state tracker (looks central but is peripheral)
class StateTracker:
    def __init__(self):
        self.history = []
        self.threshold = 42
    
    def update(self, val):
        status = 'alert' if val > self.threshold else 'normal'
        self.history.append({'value': val, 'status': status})
        return len([h for h in self.history if h['status'] == 'alert'])

# Main evaluation logic with key dependencies
def evaluate_performance(metrics, weights):
    # Step 1: Process primary indicators
    reading_valid, avg_smooth = analyze_readings(metrics['sensor_data'])
    pattern_list = generate_patterns(metrics['sequence'])
    
    # Step 2: Compute weighted components
    w1, w2, w3, w4 = weights
    c1 = avg_smooth * w1
    
    # Step 3: Conditional contribution from patterns
    if len(pattern_list) > 8:
        c2 = pattern_list[5] * w2
    else:
        c2 = sum(pattern_list) * 0.3 * w2
    
    # Step 4: Density factor
    density = compute_density(metrics['area'], metrics['count'])
    c3 = density * w3
    
    # Step 5: Boolean logic gate with short-circuit
    flag = reading_valid and (metrics['count'] > 5) or (avg_smooth > 40)
    c4 = w4 * 15 if flag else w4 * 3
    
    # Step 6: Early return decoy (never triggers due to data)
    if c1 > 1000:
        return -999  # unreachable with current inputs
    
    # Step 7: Final composition
    raw_score = c1 + c2 + c3 + c4
    
    # Step 8: Adjustment based on validation (calls function with side effect but result ignored)
    validate_sequence(metrics['sequence'])  # distractor call
    
    # Step 9: Apply non-linear transform
    final_score = int(raw_score ** 0.5 * 3.2) if raw_score > 0 else 0
    
    # Step 10: Clamp to realistic bounds (answer determined here)
    final_score = max(10, min(final_score, 50000))
    
    return final_score

# Initialization with realistic domain values
sensor_data = [12, 15, 88, 92, 45, 67, 83, 29, 11]
sequence = [3, 7, 1, 9, 4, 8]
area = 12.5
count = 7

metrics = {
    'sensor_data': sensor_data,
    'sequence': sequence,
    'area': area,
    'count': count
}

weights = (1.8, 0.7, 2.1, 1.3)

# Tracking system (distractor object)
tracker = StateTracker()
for val in sensor_data[::3]:
    tracker.update(val)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")