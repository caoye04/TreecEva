import math

# Simulated system telemetry data with mixed signal types
telemetry_stream = [72, 68, 75, 80, 69, 74, 71, 77]

# Irrelevant backup constants (distractor)
BACKUP_THRESHOLD = 42
MAX_RETRIES = 3

# System state flags representing hardware conditions
system_flags = {
    'overclocked': False,
    'fan_override': True,
    'secure_mode': False,
    'debug_trace': True
}

# Raw signal preprocessing (relevant)
signal_baseline = sum(telemetry_stream) / len(telemetry_stream)
noise_floor = math.sqrt(sum((x - signal_baseline) ** 2 for x in telemetry_stream))
filtered_signal = [x for x in telemetry_stream if abs(x - signal_baseline) <= noise_floor]

# Auxiliary diagnostic function (decoy - never called)
def legacy_diagnose(data):
    return sum(data) % 100

# Secondary metrics (partially relevant, partially distracting)
peak_magnitude = max(filtered_signal)
phase_shift = (peak_magnitude ^ 15) & 7  # Bitwise manipulation red herring

# Historical log entries with metadata (relevant container)
log_entries = [
    {'timestamp': 162000, 'value': 72, 'type': 'temp', 'valid': True},
    {'timestamp': 162001, 'value': 68, 'type': 'temp', 'valid': True},
    {'timestamp': 162002, 'value': 75, 'type': 'temp', 'valid': True},
    {'timestamp': 162003, 'value': 80, 'type': 'temp', 'valid': False},  # Invalid reading
    {'timestamp': 162004, 'value': 69, 'type': 'temp', 'valid': True}
]

# Unused helper (dead code path)
def normalize readings(readings):
    min_val = min(readings)
    return [(r - min_val) / (max(readings) - min_val) for r in readings]

# Core processing pipeline
status_weights = {
    'overclocked': 10,
    'fan_override': -3,
    'secure_mode': 5,
    'debug_trace': 2
}

# Compute activation score from flags (relevant)
activation_score = sum(status_weights[flag] for flag in system_flags if system_flags[flag])

# Extract valid values using list comprehension and dictionary op (relevant)
valid_values = [entry['value'] for entry in log_entries if entry['valid']]
value_count = len(valid_values)
raw_integral = sum(valid_values)

# Decoy calculation with bitwise operations (misleading intermediate)
correlation_key = (value_count << 2) ^ raw_integral
checksum_mask = correlation_key & 0xFF

# Secondary irrelevant transform (distractor)
frequency_domain = [math.sin(x * 0.1) for x in filtered_signal]
domain_entropy = sum(abs(f) for f in frequency_domain)

# Main metric processor (critical logic)
def process_metrics(logs, flags):
    # Step 1: Aggregate valid telemetry
    valid_data = [e['value'] for e in logs if e['valid']]
    
    # Step 2: Calculate base health index
    base_index = sum(valid_data) / len(valid_data)
    
    # Step 3: Apply flag-based modifiers
    modifier = 1.0
    if flags['overclocked']:
        modifier *= 1.2
    if not flags['secure_mode']:
        modifier *= 1.1
    if flags['debug_trace']:
        modifier *= 0.95  # Debug mode slightly reduces stability weight
    
    # Step 4: Adjusted health score
    adjusted_health = base_index * modifier
    
    # Step 5: Incorporate activation_score as integer bias
    biased_score = adjusted_health + (activation_score / 2)
    
    # Step 6: Final discretization
    return int(round(biased_score))

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)

# Print target result
print(f"Target result: {final_diagnostic}")