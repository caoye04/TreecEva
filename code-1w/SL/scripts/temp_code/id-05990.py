import math

# Simulated sensor network diagnostic system
def collect_readings():
    raw_values = [127, 255, 64, 89, 191, 33]
    offset = 10
    adjusted = [v + offset for v in raw_values]
    return adjusted

# Irrelevant transformation - red herring
def transform_signal(data):
    transformed = []
    for x in data:
        if x > 100:
            transformed.append(x * 1.5)
        else:
            transformed.append(x * 0.8)
    scaling_factor = 1.2  # Unused later
    return [t * scaling_factor for t in transformed]

# Decoy function - never called
def compute_entropy(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    total = len(seq)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Real processing chain
processed_data = []
def preprocess_readings(raw):
    global processed_data
    temp_store = []
    for val in raw:
        if val % 2 == 0:
            temp_store.append(val // 2)
        else:
            temp_store.append(val * 2)
    processed_data = sorted(temp_store, reverse=True)
    # Dead code path
    if len(processed_data) > 100:
        processed_data = processed_data[:50]

# Threshold logic with set operations
def filter_anomalies(data, lower_bound=50, upper_bound=200):
    valid_range = set(range(lower_bound, upper_bound + 1))
    data_set = set(data)
    anomalies = data_set - valid_range
    return sorted(list(anomalies))

# Core analysis with conditional expressions and recursion
def recursive_diagnose(seq, index=0, acc=0):
    if index >= len(seq):
        return acc
    current = seq[index]
    # Conditional expression used
    contribution = acc * 0.9 if current < 100 else acc + 15
    new_acc = contribution + (current % 17)
    return recursive_diagnose(seq, index + 1, new_acc)

# Main analyzer combining multiple concepts
def analyze_readings(data, thresholds):
    # Use of set intersection as filter
    critical_levels = {x for x in data if x > 150}
    filtered_for_analysis = [x for x in data if x in thresholds]
    
    # Misleading intermediate
    temp_result = sum([x ** 0.5 for x in filtered_for_analysis]) * 1.5
    
    # Actual important computation
    base_score = recursive_diagnose(filtered_for_analysis)
    
    # Conditional adjustment
    adjustment = base_score / 2 if len(critical_levels) > 2 else base_score * 1.1
    
    # Final computation
    final_risk = int(adjustment + len(filter_anomalies(data)))
    
    # Dead assignment - distraction
    diagnostic_log = {'status': 'stable', 'score': temp_result, 'count': len(data)}
    
    return final_risk

# Orchestration with decoy variables
raw_sensor_data = collect_readings()

# Unused signal processing
enriched_signal = transform_signal(raw_sensor_data)

# Actual relevant processing
preprocess_readings(raw_sensor_data)

# Define thresholds using set operation
base_thresholds = set(range(40, 181, 5))
modifier = {x for x in base_thresholds if x % 3 != 0}
threshold_set = base_thresholds.union(modifier).intersection(set(range(35, 200)))

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_set)

# Print result as required
print(f"Result: {final_diagnostic}")