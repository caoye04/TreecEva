def preprocess_sensor(x):
    return (x >> 1) ^ 0xAA

def legacy_transform(x):
    return (x * 3) % 256  # Unused in final logic

def validate_integrity(checksum, data):
    computed = sum(data) & 0xFF
    return computed == checksum

def filter_anomalies(values):
    threshold = sum(values) / len(values)
    return {x for x in values if abs(x - threshold) < 30}

def integrate_system_log(log_entries):
    total = 0
    for entry in log_entries:
        total ^= entry % 17
    return total * 2  # Distractor function

def analyze_readings(signals):
    base_set = set()
    temp_offset = 0
    
    for val in signals:
        if val % 2 == 0:
            temp_offset += (val // 4)
        else:
            temp_offset -= (val % 7)
    
    adjusted = [v + temp_offset for v in signals]
    
    for a in adjusted:
        if a > 100:
            base_set.add(a % 50)
        elif a < 50:
            base_set.discard(a % 25)  # Possible removal
        else:
            base_set.add(a // 3)

    checksum = sum(base_set) & 0xFF
    extra_data = [18, 22, 26, 30, 34]
    if validate_integrity(checksum, extra_data):
        base_set.add(42)
    
    scaling_factor = 1.5
    aggregate = 0
    for item in base_set:
        if item % 4 == 0:
            aggregate += item * scaling_factor
        else:
            aggregate += item
            
    return int(aggregate)

# Simulated signal acquisition
raw_inputs = [120, 88, 45, 72, 103, 64]
processed_signals = []
decoys = []

for x in raw_inputs:
    processed = preprocess_sensor(x)
    processed_signals.append(processed)
    
    # Irrelevant legacy path
    old_style = legacy_transform(x)
    decoys.append(old_style)

# Unused data structures as red herrings
corrupted_buffer = [0xDE, 0xAD, 0xBE, 0xEF]
system_log = [101, 202, 113, 44, 155]
log_diagnostic = integrate_system_log(system_log)

# Real computation chain
interim_set = filter_anomalies(processed_signals)
processed_signals = list(interim_set)  # Update based on filtering

final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")