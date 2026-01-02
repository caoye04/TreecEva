import math

# Simulated system telemetry data
telemetry_stream = [78, 85, 91, 64, 72, 88, 95, 54, 67, 80]

# Irrelevant signal processing functions
def apply_filter(signal):
    return [x * 0.9 for x in signal if x > 60]

def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

def calculate_entropy(values):
    hist = {}
    for v in values:
        hist[v] = hist.get(v, 0) + 1
    entropy = 0
    total = len(values)
    for count in hist.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused but plausible diagnostic routines
def legacy_diagnostic(seq):
    return sum([x ** 0.5 for x in seq]) % 100

def validate_checksum(record):
    return sum(record) % 256

# Core system health logic
log_entries = [(1, 'TEMP', 88), (2, 'VOLT', 12.4), (3, 'TEMP', 95), (4, 'FAN', 2400), (5, 'TEMP', 82)]
system_baseline = {'TEMP': 85, 'VOLT': 12.0, 'FAN': 2500}

# Distractor: complex-looking but unused data transformation
temp_history = [entry[2] for entry in log_entries if entry[1] == 'TEMP']
historical_deviation = sum([abs(t - system_baseline['TEMP']) for t in temp_history]) / len(temp_history) if temp_history else 0

# Misleading intermediate metric
apparent_stress_level = (historical_deviation * 1.5) + 10

# Real threshold logic buried in noise
system_threshold = 87

# Decoy state machine
state_weights = {
    'IDLE': 0.1,
    'ACTIVE': 0.6,
    'LOAD': 0.8,
    'CRITICAL': 1.2
}

# Irrelevant lambda used once and discarded
transform = lambda x: x + 5 if x < 80 else x - 3
processed_telemetry = list(map(transform, telemetry_stream))

def evaluate_stability(metrics):
    # Nested conditional with red herring
    if len(metrics) < 4:
        return 0.0
    
    temp_readings = [m[2] for m in metrics if m[1] == 'TEMP']
    volt_readings = [m[2] for m in metrics if m[1] == 'VOLT']
    
    # Real computation begins here
    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
    avg_volt = sum(volt_readings) / len(volt_readings) if volt_readings else 0
    
    # Multiple distractor calculations
    fluctuation_score = max(temp_readings) - min(temp_readings) if temp_readings else 0
    voltage_risk = 1 if any(v < 11.5 for v in volt_readings) else 0
    
    # Actual core logic masked by complexity
    base_risk = 50 if avg_temp > system_threshold else 20
    adjustment = 15 if fluctuation_score > 10 else 5
    
    # Conditional expression determining final outcome
    safety_margin = 1.0 if avg_volt >= 12.0 else 0.7
    
    # Final calculation embedded in function
    return int((base_risk + adjustment) * safety_margin)

# Another decoy function that looks important
analyze_pattern = lambda data: sum(1 for i in range(1, len(data)) if data[i] > data[i-1])

# Unused recursive structure to distract
def predict_failure(seq, depth=0):
    if depth >= 2 or not seq:
        return 0
    return seq[0] * 0.1 + predict_failure(seq[1:], depth + 1)

# Real processing function
config_flags = [True, False, True]
enabled_modules = sum(1 for f in config_flags if f)

# The actual answer-producing function
process_metrics = lambda logs, thresh: evaluate_stability(logs) + (10 if enabled_modules > 2 else 0)

# Key execution point
final_diagnostic = process_metrics(log_entries, system_threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")