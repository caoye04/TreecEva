import math

# Simulated sensor fusion system for environmental monitoring

def collect_data(baseline, offset=0.15):
    readings = []
    for i in range(3, 7):
        val = (baseline ** i) % (10 + i * 2)
        readings.append(round(val + offset, 3))
    return readings

# Irrelevant utility - distractor function
def validate_checksum(data_str):
    if not data_str:
        return False
    total = sum(ord(c) for c in data_str)
    return total % 7 == 0

# Signal preprocessing with red herring operations
def preprocess_signal(raw_seq, mode='strict'):
    temp_buffer = [x * 1.05 for x in raw_seq]
    filtered = []
    threshold = sum(temp_buffer) / len(temp_buffer)
    
    # Dead code path - never executed due to mode
    if mode == 'relaxed':
        for v in temp_buffer:
            if v > threshold * 0.8:
                filtered.append(v)
    else:
        for v in temp_buffer:
            if v > threshold and v < 90:  # selective filtering
                filtered.append(v)
    
    # Unused transformation - creates misleading intermediate values
    normalized = [round((x - min(filtered)) / (max(filtered) - min(filtered)) * 100, 2) for x in filtered] if filtered else [0]
    
    # Actual relevant output
    return [math.log(x) if x > 0 else 0 for x in filtered]

# Core analysis logic
def compute_entropy(values):
    if not values:
        return 0.0
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

# Redundant string-based diagnostic - distraction
status_map = {
    'OK': 'Operational',
    'WARN': 'Degraded',
    'ERR': 'Failed'
}

def generate_status_report(code, details=''):
    label = status_map.get(code, 'Unknown')
    report_id = f"REP-{hash(details) % 10000}"
    return f"[{report_id}] System {label}: {details}" if details else "No data"

# Main processing chain
raw_input = collect_data(baseline=4.2, offset=0.15)

# Distractor: unused alternate collection path
alt_data = collect_data(baseline=2.1, offset=0.3)
dummy_check = validate_checksum("sensor_42")

processed_signals = preprocess_signal(raw_input, mode='strict')

# Fake branching - unreachable under current logic
if len(processed_signals) > 10:
    processed_signals = processed_signals[:5]

# Auxiliary computation - looks important but unused in final result
signal_power = sum(x**2 for x in processed_signals) / len(processed_signals) if processed_signals else 0
power_level = 'High' if signal_power > 10 else 'Low'

# Real analytical path begins here
entropy_metric = compute_entropy(processed_signals)

classification_bins = [0, 0.5, 1.0, 1.5, 2.0]
def get_bin_index(value):
    for i, edge in enumerate(classification_bins):
        if value <= edge:
            return i
    return len(classification_bins)

bin_category = get_bin_index(entropy_metric)

# Secondary irrelevant transformation using string methods
bin_label = f"BIN-{bin_category}".replace('B', 'b').upper()
flagged = bin_label.endswith('3') or len(bin_label) == 6

# Complex conditional expression combining boolean and arithmetic logic
adjustment_factor = 1.75 if flagged and entropy_metric < 1.2 else (0.85 if bin_category % 2 == 0 else 1.15)

# Final diagnostic computation - this is the actual answer point
final_diagnostic = round(entropy_metric * adjustment_factor * 100, 4)

# Misleading print statements - distract from target variable
# print(f"Raw input: {raw_input}")
# print(f"Processed: {processed_signals}")
# print(f"Entropy: {entropy_metric}, Bin: {bin_category}")
# print(generate_status_report('OK', f'Entropy={entropy_metric}'))

# Only this matters:
print(f"Target result: {final_diagnostic}")