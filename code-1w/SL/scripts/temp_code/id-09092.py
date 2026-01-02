def preprocess_sensor_readings(raw):    
    # Irrelevant transformation (distractor)
    temp = [x * 1.8 + 32 for x in raw]  # Convert to Fahrenheit (unused)
    cleaned = [x for x in raw if 0 <= x <= 100]
    normalized = [round(x / max(cleaned), 2) for x in cleaned]
    return normalized

# Misleading auxiliary function (dead path)
def analyze_soil_ph(ph_levels):
    avg = sum(ph_levels) / len(ph_levels)
    if avg < 6.0:
        return "acidic"
    elif avg > 7.0:
        return "alkaline"
    else:
        return "neutral"

# Unused but plausible data
test_ph = [5.2, 5.8, 6.1, 6.3]
soil_status = analyze_soil_ph(test_ph)

# Core logic buried in noise
raw_moisture = [45, 0, 67, 89, -5, 92, 105, 77, 34]

# Decoy computation with string methods (irrelevant)
diagnostic_log = "Sensor: MOIST-4A Status: OK Timestamp: 2023-08-15"
if diagnostic_log.startswith("Sensor") and "OK" in diagnostic_log:
    log_valid = True
    sensor_id = diagnostic_log.split(" ")[1].strip(":")  # MOIST-4A

# Real preprocessing
filtered_data = preprocess_sensor_readings(raw_moisture)

# Simulate multiple data passes (only one matters)
aggregated_metrics = []
for i, val in enumerate(filtered_data):
    if i % 2 == 0:
        # Apply real transformation only on even indices
        adjusted = val * (1 + 0.1 * i)  # Increasing efficiency factor
    else:
        adjusted = val * 0.9  # Distractor branch
    aggregated_metrics.append(round(adjusted, 2))

# Secondary irrelevant list operation
event_flags = [''.join(sorted(flag.lower())) for flag in ["Read", "Done", "Sync"]]

# Key conditional expression using combinatorics
pair_count = len(aggregated_metrics) * (len(aggregated_metrics) - 1) // 2 if len(aggregated_metrics) > 1 else 0

# Bit manipulation red herring
bitmask = 0b101010
shifted_mask = bitmask << 2
overlap_check = shifted_mask & 0b111100  # Unused result

# Main calculation hidden among distractions
def calculate_harvest_efficiency(metrics):
    base_efficiency = sum(metrics)
    
    # Integer division and rounding combo
    penalty_factor = len(metrics) // 3  # Every 3 sensors add a penalty
    adjusted_efficiency = base_efficiency - (penalty_factor * 2.5)
    
    # Conditional expression based on pair count (plausible link)
    multiplier = 1.1 if pair_count > 10 else 0.95
    
    # Final yield calculation (this is the answer)
    final_value = round(adjusted_efficiency * multiplier, 4)
    
    # Dead code path (never reached)
    if final_value < 0:
        return 0.0
    
    return final_value

# Unused recursive decoy
def binary_partition(n):
    if n <= 1:
        return 1
    return binary_partition(n - 2) + binary_partition(n // 2)

partition_test = binary_partition(8)  # Computationally heavy but irrelevant

# Critical execution point
processed_data = aggregated_metrics
final_yield = calculate_harvest_efficiency(processed_data)

print(f"Result: {final_yield}")