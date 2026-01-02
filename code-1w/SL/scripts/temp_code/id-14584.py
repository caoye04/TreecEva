import math

# Simulated sensor array diagnostics with embedded logic chain

def preprocess_signal(raw_input, gain=1.0, offset=0.0):
    """Apply gain and offset correction to raw signal."""
    amplified = [x * gain for x in raw_input]
    corrected = [x + offset for x in amplified]
    return [round(x, 3) for x in corrected]


def detect_spikes(signal_data, threshold=0.75):
    """Identify spike events in normalized signal."""
    spikes = []
    for i in range(1, len(signal_data) - 1):
        if abs(signal_data[i]) > threshold:
            if abs(signal_data[i]) > abs(signal_data[i-1]) and abs(signal_data[i]) > abs(signal_data[i+1]):
                spikes.append(i)
    return spikes if spikes else [0]


def compute_coherence(signal_a, signal_b):
    """Compute cross-signal coherence metric (simplified)."""
    if len(signal_a) != len(signal_b):
        return 0.0
    product_sum = sum(a * b for a, b in zip(signal_a, signal_b))
    norm_a = math.sqrt(sum(a * a for a in signal_a))
    norm_b = math.sqrt(sum(b * b for b in signal_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return round(product_sum / (norm_a * norm_b), 6)

# Irrelevant utility - DISTRACTOR
convert_to_hex = lambda val: hex(int(val)) if isinstance(val, (int, float)) else '0x0'

# System status codes - PARTIALLY RELEVANT
SYSTEM_CODES = {
    'OK': 0,
    'WARN': 1,
    'FAULT': 2,
    'CRITICAL': 3
}

# Decoy function - DEAD CODE PATH
def legacy_calibrate(x):
    return [elem * 0.95 for elem in x if elem > 1]  # never called

# Signal sources (simulated)
primary_channel = [0.1, 0.82, 0.33, 0.91, 0.67, 0.22, 0.76, 0.51]
secondary_channel = [0.15, 0.79, 0.38, 0.88, 0.62, 0.29, 0.73, 0.54]

# Apply preprocessing - RELEVANT
processed_primary = preprocess_signal(primary_channel, gain=1.1, offset=-0.05)
processed_secondary = preprocess_signal(secondary_channel, gain=1.05, offset=-0.02)

# Spike detection - RELEVANT for flagging
primary_spikes = detect_spikes(processed_primary, threshold=0.7)
secondary_spikes = detect_spikes(processed_secondary, threshold=0.75)

# Compute coherence between channels - RELEVANT
coherence_score = compute_coherence(processed_primary, processed_secondary)

# Mock system health flags - MIX OF RELEVANT AND IRRELEVANT
system_status = 'OK'
system_age_years = 7
maintenance_due = False
last_calibration = '2023-06-15'

current_timestamp = '2024-04-05T10:30:00Z'
timezone_offset = '+02:00'

# Derive diagnostic flags - RELEVANT
spike_count_diff = abs(len(primary_spikes) - len(secondary_spikes))
system_warnings = 0
if spike_count_diff > 1:
    system_warnings += 1
if coherence_score < 0.85:
    system_warnings += 2

# Unused diagnostic - DISTRACTOR
signal_entropy = -sum(p * math.log(p) for p in processed_primary if p > 0)

# Flag vector construction - RELEVANT
system_flags = [
    int(system_status != 'OK'),
    system_warnings,
    1 if len(primary_spikes) > 2 else 0,
    1 if last_calibration.startswith('2022') else 0  # static eval: false
]

# Normalize signals using min-max - RELEVANT
min_val = min(min(processed_primary), min(processed_secondary))
max_val = max(max(processed_primary), max(processed_secondary))
range_val = max_val - min_val if max_val != min_val else 1

normalized_primary = [(x - min_val) / range_val for x in processed_primary]
normalized_secondary = [(x - min_val) / range_val for x in processed_secondary]

# Concatenate for joint analysis - RELEVANT
normalized_signals = [a + b for a, b in zip(normalized_primary, normalized_secondary)]

# Aggregate metrics function - KEY LOGIC HUB
# Contains conditional expression and string method red herring
aggregate_metrics = lambda sigs, flags: (
    sum(sigs) * (flags[1] + 1)
    + (50 if ''.join(['A', 'B', 'C']).lower().endswith('c') else -50)  # True -> +50
    - (100 if len([f for f in flags if f > 0]) >= 3 else 0)  # False -> no subtract
    + round(coherence_score * 100)
)

# Final computation - TARGET STATEMENT
final_diagnostic = aggregate_metrics(normalized_signals, system_flags)

# Irrelevant formatting - DISTRACTOR
report_header = f"Diagnostics Report {current_timestamp}".strip().upper()
report_id = report_header.split()[0].count('D')  # =1, unused

# Another decoy transformation - DISTRACTOR
transformed = list(map(lambda x: math.tanh(x), [coherence_score, spike_count_diff]))

# Output target result
print(f"Result: {final_diagnostic}")