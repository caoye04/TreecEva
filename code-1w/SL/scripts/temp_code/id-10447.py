def analyze_pattern(seq):
    return sum(x * (i + 1) for i, x in enumerate(seq))


def evaluate_stability(rates):
    return abs(sum(rates) - len(rates) * 50) < 10


def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)


def filter_anomalies(data, limit):
    return [x for x in data if x < limit]


def merge_signals(a, b):
    return [x ^ y for x, y in zip(a, b)]

# Irrelevant signal processing functions (distractors)
def encrypt_sequence(seq):
    return [x ^ 255 for x in seq]

def compress_data(seq):
    return [seq[i] for i in range(0, len(seq), 2)]

def generate_checksum(seq):
    return sum(seq) % 256

# Unused but plausible intermediate transformations
temp_offsets = [12, 7, 3, 19, 25]
signal_mask = [1, 0, 1, 0, 1, 0, 1]
baseline_correction = sum(temp_offsets) // len(temp_offsets)

# Real health monitoring data (simulated sensor inputs)
heart_rates = [68, 72, 70, 69, 75, 71, 67, 73]
respiration_rates = [16, 18, 17, 16, 19, 17, 15, 18]
blood_oxygen = [98, 97, 98, 99, 97, 98, 96, 98]

# Thresholds for diagnostic logic
thresholds = {
    'hr_low': 60,
    'hr_high': 100,
    'o2_critical': 95,
    'stability_margin': 10
}

# Auxiliary derived metrics (some irrelevant)
avg_heart_rate = sum(heart_rates) / len(heart_rates)
stable_rhythm = evaluate_stability(heart_rates)

# Simulated neural activity pattern (bitwise manipulation red herring)
neural_pattern = [1, 0, 1, 1, 0, 1, 0, 0]
shifted_pattern = [(x << 1) & 1 for x in neural_pattern]

# Decoy diagnostic using unused function
decoy_score = analyze_pattern(neural_pattern)

# Core data transformation chain
filtered_o2 = filter_anomalies(blood_oxygen, thresholds['o2_critical'])
combined_signal = merge_signals(heart_rates[:len(respiration_rates)], respiration_rates)

# Add dummy string processing to satisfy language feature requirement
status_log = "Patient stability assessment: COMPLETE"
log_flag = status_log.find("COMPLETE") >= 0
flag_weight = int(log_flag) * 10

# Real diagnostic metric computation
data_entropy = compute_entropy(combined_signal)

# Dictionary-based state tracking (meaningful usage)
diagnostic_state = {
    'entropy': data_entropy,
    'correction': baseline_correction,  # unused but plausible
    'length': len(combined_signal),
    'flag_adjust': flag_weight
}

# Primary processing function combining multiple concepts
def process_metrics(metrics, config):
    raw_values = metrics['values'] if 'values' in metrics else combined_signal
    
    # Apply threshold filtering
    valid_rates = [r for r in raw_values if config['hr_low'] <= r <= config['hr_high']]
    
    # Compute weighted index using enumeration
    index_sum = 0
    for i, val in enumerate(valid_rates):
        weight = 1.0 + (i * 0.1)
        index_sum += val * weight
    
    # Introduce bit manipulation distraction
    magic_key = 0
    for v in valid_rates:
        magic_key ^= (v & 15) << 1
    
    # Actual critical calculation
    n = len(valid_rates)
    if n == 0:
        return 0
    
    # Final formula incorporating entropy and adjusted average
    avg_valid = sum(valid_rates) / n
    adjustment = 1.0 + (diagnostic_state['entropy'] / 100)
    
    # Add decoy use of string method
    decoy_text = "Final report finalized."
    occurrences = decoy_text.count("final")  # irrelevant
    
    result = (avg_valid * adjustment) + diagnostic_state['flag_adjust']
    return int(round(result))

# Construct input dictionary (plausible structure)
health_data = {
    'sensor_id': 'HMD-9X',
    'timestamp': '2023-11-05T10:30:00Z',
    'values': heart_rates  # main input source
}

# Execute key statement
final_diagnostic = process_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")