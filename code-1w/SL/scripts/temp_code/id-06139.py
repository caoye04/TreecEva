import itertools

# Simulated sensor array data processing with diagnostic analysis
def collect_sensor_readings():
    base_readings = [3, 7, 1, 9, 2]
    readings = []
    for r in base_readings:
        # Real transformation
        transformed = (r ** 2) + 5
        readings.append(transformed)
    return readings

# Irrelevant helper - looks important but unused in final path
def deprecated_filter(data):
    return [x for x in data if x % 2 == 0]

# Decoy function - appears to be part of processing chain
def compute_legacy_score(values):
    score = 0
    for i in range(len(values)):
        score += values[i] * (i + 1)
    return score  # Never actually used

# Real transformation function
def apply_window_smoothing(data):
    smoothed = []
    window_size = 3
    for i in range(len(data) - window_size + 1):
        window_avg = sum(data[i:i+window_size]) / window_size
        smoothed.append(round(window_avg, 2))
    return smoothed

# Another red herring - processes data but result discarded
def generate_combinatorial_pairs(data):
    pairs = list(itertools.combinations(data, 2))
    magnitude = 0
    for a, b in pairs:
        magnitude += abs(a - b)
    temp_result = magnitude * 0.1
    return temp_result  # Computed but not used later

def flag_anomalies(data, limit):
    anomalies = []
    for val in data:
        if val > limit and val % 3 == 0:
            anomalies.append(val)
    return len(anomalies) > 0

# Core analysis function - actually contributes to final answer
def analyze_pattern(sequence, cutoff):
    count_valid = 0
    temp_buffer = []
    
    # Real logic starts here
    for item in sequence:
        if item > cutoff:
            temp_buffer.append(item * 0.5)
        else:
            temp_buffer.append(item * 1.1)
    
    # Secondary filtering
    filtered = [x for x in temp_buffer if x.is_integer()]
    
    # Accumulate based on condition
    for val in filtered:
        if val > 10:
            count_valid += int(val)
        else:
            count_valid += int(val * 2)
    
    # Final computation branch
    adjustment = 0
    for i in range(1, len(filtered) + 1):
        if i % 2 == 0:
            adjustment += i * 3
    
    return count_valid + adjustment

# Main execution flow
raw_data = collect_sensor_readings()  # [14, 54, 6, 86, 9]
processed_data = apply_window_smoothing(raw_data)  # Smoothing applied

# DEAD CODE PATH - looks active but result ignored
discarded_analysis = generate_combinatorial_pairs(raw_data)
score_proxy = compute_legacy_score(raw_data)  # Computed but unused

# Transform data for actual use
transformed_data = [int(x * 1.5) for x in raw_data]  # [21, 81, 9, 129, 13]

# Threshold determined from irrelevant anomaly check
exceeds_threshold = flag_anomalies(raw_data, 50)
threshold = 40 if exceeds_threshold else 30  # True -> threshold = 40

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")