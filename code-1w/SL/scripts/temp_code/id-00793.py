def monitor_system_load(base_frequency, multiplier, samples):
    readings = []
    temp_offset = 0.0
    for i in range(samples):
        if i % 2 == 0:
            temp_offset += (i + base_frequency) * 0.1
        elif i % 3 == 0:
            temp_offset -= (i // multiplier) * 0.05
        voltage_spike = (i * base_frequency) % 7 == 0
        power_draw = (i + multiplier) ** 0.5
        readings.append({
            'tick': i,
            'power': round(power_draw, 3),
            'voltage_spike': voltage_spike,
            'temp_comp': temp_offset
        })
    return readings


def calculate_entropy(data_series):
    from math import log2
    counts = {}
    for val in data_series:
        counts[val] = counts.get(val, 0) + 1
    total = len(data_series)
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return round(entropy, 4)


def validate_checksum(record):
    checksum = 0
    for key, value in record.items():
        if isinstance(value, int):
            checksum += value * 2
        elif isinstance(value, float):
            checksum += int(value)
    return checksum % 17


def analyze_efficiency(log_data, limit):
    # Irrelevant pre-processing block (distractor)
    filtered_ticks = [entry['tick'] for entry in log_data if entry['voltage_spike']]
    spike_rate = len(filtered_ticks) / len(log_data) if log_data else 0
    
    # Decoy computation with unused result
    baseline_shift = sum([int(entry['power']) for entry in log_data]) * 0.1
    adjustment_factor = 1.0
    if spike_rate > 0.3:
        adjustment_factor *= 0.9
    elif spike_rate == 0:
        adjustment_factor *= 1.1

    # Core logic: accumulate compensated temperature
    compensated_temps = []
    for entry in log_data:
        comp_temp = entry['power'] - entry['temp_comp']
        if comp_temp > limit:
            compensated_temps.append(comp_temp)
    
    # Red herring: complex but unused transformation
    transformed = [round((t ** 2 + 5) / 2.7, 3) for t in compensated_temps if t < 15]
    size_factor = len(transformed) // 2 if transformed else 0
    
    # Actual efficiency calculation
    raw_sum = sum(compensated_temps)
    penalty = 0
    for i in range(1, len(compensated_temps)):
        if compensated_temps[i] > compensated_temps[i-1]:
            penalty += 1
    efficiency = raw_sum - (penalty * adjustment_factor) + size_factor
    
    # Dead code path (never reached due to logic above)
    if baseline_shift < 0:
        efficiency *= 1.05  # Unused branch

    return int(round(efficiency))

# Simulate system monitoring
performance_log = monitor_system_load(base_frequency=13, multiplier=4, samples=47)

# Extract a subset of data for entropy analysis (irrelevant to final result)
data_stream = [int(entry['power'] * 10) % 5 for entry in performance_log]
entropy_value = calculate_entropy(data_stream)  # Unused metric

# Validate each record's checksum (partially executed but not used)
checksum_total = 0
for record in performance_log[:10]:
    checksum_total += validate_checksum(record)

# Apply threshold filter based on dynamic condition
dynamic_threshold = (len(performance_log) // 5) * 0.45

# Key statement
threshold = dynamic_threshold + 2.3

# This is the critical variable
efficiency_score = analyze_efficiency(performance_log, threshold)

# Output target result
print(f"Target result: {efficiency_score}")