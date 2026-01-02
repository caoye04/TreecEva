def analyze_pattern(sequence):
    """Irrelevant helper function for pattern analysis."""
    return [i for i, x in enumerate(sequence) if x % 3 == 0]

# Simulated sensor readings from environmental monitoring stations
temperature_readings = [23, 25, 19, 17, 26, 28, 24, 20]
humidity_levels = [45, 50, 60, 70, 55, 40, 35, 65]
pressure_values = [1013, 1015, 1012, 1010, 1016, 1018, 1014, 1009]

# Distractor: unused transformation
transformed = list(map(lambda x: (x - 32) * 5/9, [f*9/5+32 for f in temperature_readings]))

# Weight configuration for data fusion (some weights are misleading)
weight_config = {
    'temp': [0.3, 0.4, 0.3],
    'humidity': [0.2, 0.3, 0.5],
    'pressure': [0.1, 0.1, 0.8]  # Misleading emphasis on last element
}

# Irrelevant sequence processing
def generate_fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

fib_data = generate_fibonacci(8)
decoy_matrix = [[i*j for j in range(4)] for i in range(4)]

# Real computation begins: trend detection using moving average
def compute_trend(data, window=3):
    trends = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        trends.append(round(window_avg, 2))
    return trends

trend_temperature = compute_trend(temperature_readings)
trend_humidity = compute_trend(humidity_levels)
trend_pressure = compute_trend(pressure_values)

trend_data = list(zip(trend_temperature, trend_humidity, trend_pressure))

# Secondary distractor: character counting in dummy labels
sensor_labels = ['A1', 'B2', 'C3', 'D4', 'E5']
label_char_count = sum(len(label) for label in sensor_labels)

# Weight vector for final aggregation (only this weight set is used)
weights = [0.5, 0.3, 0.2]

# Complex data transformation with red herring operations
def preprocess_entry(entry):
    base_val = entry[0] * 1.1  # Temperature contribution
    adj_factor = (entry[1] / 100) * 0.9  # Humidity adjustment
    noise_offset = (entry[2] % 100) * 0.01  # Pressure-derived noise (distractor)
    return base_val + adj_factor - 0.5  # Final formula ignores noise

processed_entries = [preprocess_entry(item) for item in trend_data]

# Dead code path - never called
def legacy_compatibility_mode():
    return sum(fib_data) / len(fib_data)

# Another decoy function with bit manipulation (irrelevant)
def obfuscate_value(x):
    return (x << 2) ^ 0xA5 ^ (x >> 1)

obfuscated_sequence = [obfuscate_value(int(t)) for t in trend_temperature]

# Core aggregation logic - only this part matters
def aggregate_metrics(trends, w):
    totals = []n    for idx, entry in enumerate(trends):
        # Only temperature trend is actually used in final calculation
        relevant_input = entry[0]  # Only temperature component
        weighted_contribution = relevant_input * w[idx % len(w)]
        totals.append(weighted_contribution)
    
    # Final diagnostic score computed via selective summation
    raw_sum = sum(totals)
    adjustment = len(totals) * 0.25
    return int(raw_sum - adjustment)  # Deterministic integer result

# Key execution point
final_diagnostic = aggregate_metrics(trend_data, weights)

# Output result as required
print(f"Target result: {final_diagnostic}")