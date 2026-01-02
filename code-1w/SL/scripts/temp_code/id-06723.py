def filter_anomalies(data, limit):
    # Irrelevant transformation
    scaled = [x * 1.05 for x in data if x > 0]
    anomalies = []
    for val in scaled:
        if val > limit * 1.2:
            anomalies.append(int(val // 1))
    # Dead code path - never used
    temp_result = [x for x in anomalies if x % 2 == 0]
    return anomalies[:10]

# Decoy function that looks important but isn't used in final calculation
def compute_variance(samples):
    mean = sum(samples) / len(samples)
    return sum((x - mean) ** 2 for x in samples) / len(samples)

# Another red herring: complex bit manipulation with no real impact
def encode_flags(mode, level, active):
    flag = 0
    flag |= (mode & 0b111) << 5
    flag ^= (level & 0b1111) << 1
    if active:
        flag |= 1
    # Result is never used in main logic
    return flag ^ 0xABCD

# Diagnostic aggregator with side distractions
def generate_diagnostics(tags):
    tag_set = set(tag.upper() for tag in tags)
    prefix_count = {}
    for tag in tag_set:
        prefix = tag[:3]
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1
    # Creates illusion of complexity but unused
    sorted_pairs = sorted(prefix_count.items(), key=lambda x: x[1], reverse=True)
    return {k.lower(): v for k, v in sorted_pairs}

# Core logic buried among noise
def analyze_readings(vals, log_map):
    if not vals:
        return -999
    
    # Real computation begins here
    adjusted = [v - 5 for v in vals]
    positive_only = [v for v in adjusted if v > 0]
    
    # Distractor: creates a mapping that's not fully used
    magnitude_classes = {}
    for v in positive_only:
        class_key = v // 10
        magnitude_classes[class_key] = magnitude_classes.get(class_key, 0) + 1
    
    # Actual result derivation
    total = sum(positive_only)
    count = len(positive_only)
    
    # This slicing operation is critical and easy to miss
    window = positive_only[-3:]  # Last three values
    surge = sum(window) / 3 if window else 0
    
    # Final formula combining multiple concepts
    base_score = total * count
    boost = int(surge * 2.7)  # Hidden multiplier
    final_score = base_score + boost
    
    # Dead assignment - misleading
    final_score = final_score if final_score > 0 else abs(final_score)
    
    return final_score

# Irrelevant initialization block
modes = ['A', 'B', 'C']
data_keys = {f'key_{i}': i * 0.95 for i in range(5)}
status_flags = [True, False, True]

# Real data inputs
sensor_data = [8, 12, -3, 25, 40, 16, 7, 38, 42, 31, 9, 20, 28, 35]
threshold = 20

# Unused but plausible-looking diagnostic structure
diagnostics_log = {
    'version': '2.1.5',
    'tags': ['SYS', 'IO', 'MEM', 'CPU', 'NET'],
    'active': True,
    'checksum': 0xDEADBEEF
}

# Side computation that seems relevant but isn't
baseline = list(range(10))
baseline_squared = [x**2 for x in baseline if x % 3 == 0]

# Critical execution point buried in distraction
filtered_data = filter_anomalies(sensor_data, threshold)
encoded = encode_flags(5, 12, True)  # Result ignored
log_analysis = generate_diagnostics(diagnostics_log['tags'])  # Partially unused
final_diagnostic = analyze_readings(filtered_data, log_analysis)

# Output the required result
print(f"Result: {final_diagnostic}")