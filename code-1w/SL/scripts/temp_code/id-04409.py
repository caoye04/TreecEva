def analyze_temperatures(temp_readings):
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_deviation = [round(abs(t - avg_temp), 2) for t in temp_readings]
    high_deviation_count = len([d for d in temp_deviation if d > 5.0])
    return avg_temp, high_deviation_count


def extract_signals(sensor_data):
    signals = []
    for i, reading in enumerate(sensor_data):
        if i % 3 == 0 and reading > 0:
            signals.append(reading * 1.5)
    normalized = [s / max(signals) for s in signals] if signals else [0]
    return normalized


def calculate_final_score(data_chunk):
    base_values = [x for x in data_chunk if x > 0]
    squared_chain = [val**2 for val in base_values]
    shifted_values = [sq - 10 for sq in squared_chain]
    
    # Irrelevant transformation (distraction)
    temp_analysis = []
    for idx, v in enumerate(shifted_values):
        if v > 0:
            temp_analysis.append(v * 0.9 + idx)
    
    # Dummy accumulation with partial use
    accumulator = 0
    for j, val in enumerate(shifted_values):
        if j % 2 == 0:
            accumulator += val
    
    # Actual score computation path
    filtered = [v for v in shifted_values if v > 0]
    if not filtered:
        return 0
    mean_positive = sum(filtered) / len(filtered)
    penalty_factor = len(shifted_values) - len(filtered)
    final_score = mean_positive - penalty_factor * 0.5
    return round(final_score, 4)

# Main execution block
raw_input_data = [3, -1, 4, 1, -5, 9, 2, 6, -3, 5]

# Distraction: unused derived list
expanded_data = [x * 2 for x in raw_input_data if x > 0]
expanded_data.append(sum(expanded_data[:3]))

# Another distraction: auxiliary processing with no impact
status_flags = []
for index, value in enumerate(raw_input_data):
    if value < 0:
        status_flags.append((index, 'NEG'))
    elif value == 0:
        status_flags.append((index, 'ZERO'))

# Real data flow begins here
subset_selection = [x for x in raw_input_data if x != -1]
cleaned_data = [abs(x) for x in subset_selection]
distorted_copy = [c * 1.1 for c in cleaned_data]
distorted_copy = [round(d, 1) for d in distorted_copy]

processed_data = []
for val in cleaned_data:
    processed_data.append(val + 2)

# Key computational step
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")