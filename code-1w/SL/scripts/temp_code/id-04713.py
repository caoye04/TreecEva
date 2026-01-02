import itertools

# Simulated sensor data processing pipeline with red herrings
def collect_signals():
    raw_signals = [i ** 2 for i in range(15) if i % 3 != 0]
    noise_floor = sum([x & 7 for x in raw_signals])  # Irrelevant noise metric
    return raw_signals

# Out-of-scope diagnostic function (dead code path)
def run_diagnostics():
    status_codes = {i: (i * 17) % 11 for i in range(1, 10)}
    avg_code = sum(status_codes.values()) / len(status_codes)
    return avg_code  # Never used

# Real transformation: filter and scale
def normalize(signal_list):
    filtered = [x for x in signal_list if x > 20]
    scaling_factor = 0.85
    scaled = [int(x * scaling_factor) for x in filtered]  # Truncate to int
    return scaled

# Misleading intermediate transformation (partial use)
def augment_data(data):
    augmented = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            augmented.append(val + (val >> 2))  # Add 25% via bit shift
        else:
            augmented.append(val - (val // 10))  # Subtract 10%
    checksum = sum(augmented) % 97  # Distractor: looks important
    return augmented

# Core aggregation logic
def aggregate_series(processed):
    paired = list(itertools.zip_longest(processed[::2], processed[1::2], fillvalue=0))
    aggregated = []
    for a, b in paired:
        result = (a ^ b) + (a & b)  # XOR plus AND: unique combination
        aggregated.append(result)
    return aggregated

# Final computation with conditional expression
def finalize_processing(data_list):
    base_sum = sum(data_list)
    adjustment = 1.5 if len(data_list) > 5 else 0.75
    # Apply modular correction based on sum parity
    mod_shift = base_sum % 3 if base_sum % 2 == 0 else base_sum % 4
    final_score = base_sum * adjustment - mod_shift
    return round(final_score, 4)

# --- Execution Pipeline ---
sensor_readings = collect_signals()
normalized_readings = normalize(sensor_readings)
# Augment but only partially use output
temp_data = augment_data(normalized_readings)
decoy_stat = len(temp_data) * 2  # Unused distraction
primary_stratum = [x for x in temp_data if x % 4 == 2]  # Sub-selection
aggregated_data = aggregate_series(primary_stratum)
# Dead code invocation (no effect)
diagnostic_result = run_diagnostics()
# Critical statement
filtration_score = finalize_processing(aggregated_data)
print(f"Result: {filtration_score}")