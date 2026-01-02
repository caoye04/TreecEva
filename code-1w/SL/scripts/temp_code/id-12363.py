from itertools import compress, count

def analyze_signal(data, noise_floor):
    filtered = [x for x in data if x > noise_floor]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    
    # Irrelevant transformation
    inverted = [1 - val for val in normalized if val < 0.8]
    inversion_sum = sum(inverted)

    # Actual relevant feature extraction
    significant = list(compress(normalized, (val >= 0.65 for val in normalized)))
    return significant

def calculate_efficiency(signal_parts, limit):
    base = sum(signal_parts)
    adjustment = 0
    for i, val in enumerate(signal_parts):
        if i % 2 == 0:
            adjustment += val * 0.1
        else:
            adjustment -= val * 0.05
    
    # Dead computation - does not affect final logic
    temp_sequence = [i ** 2 for i in range(len(signal_parts)) if i < limit]
    temp_sum = sum(temp_sequence)

    efficiency = (base + adjustment) * 100
    return int(efficiency)

# Main execution
raw_signal = [120, 140, 95, 160, 175, 80, 200, 155]
baseline = 100
threshold = 5

# Signal preprocessing chain
cleansed = analyze_signal(raw_signal, baseline)

# Secondary irrelevant tracking
status_log = []
for idx, reading in enumerate(cleansed):
    status_log.append(f'Sample {idx}: {reading}')

# Key state variable updated here
efficiency_score = calculate_efficiency(cleansed, threshold)

# Additional red herring variables
total_power = sum(x**2 for x in raw_signal)
signal_peaks = [x for x in raw_signal if x > 150]
peak_count = len(signal_peaks)

# Final output
print(f'Result: {efficiency_score}')