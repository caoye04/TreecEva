def analyze_frequency(signal_list, sample_rate):
    total_peaks = 0
    peak_magnitudes = []
    for i, val in enumerate(signal_list):
        if abs(val) > 5 and i % 2 == 0:
            total_peaks += 1
            peak_magnitudes.append(abs(val))
    
    # Distractor: irrelevant frequency scaling
    scaled_peaks = [mag * sample_rate / 100 for mag in peak_magnitudes]
    average_scaled = sum(scaled_peaks) / len(scaled_peaks) if scaled_peaks else 0

    # Real logic starts here
    adjusted_peaks = [int(mag // 2) for mag in peak_magnitudes]
    cumulative = 0
    for p in adjusted_peaks:
        cumulative = (cumulative + p) % 97
    return cumulative


def filter_artifacts(raw_data):
    cleaned = []
    artifact_flags = []
    for idx, entry in enumerate(raw_data):
        flag = False
        if isinstance(entry, dict) and 'noise_level' in entry:
            if entry['noise_level'] > 3:
                flag = True
        artifact_flags.append(flag)
        if not flag and 'value' in entry:
            cleaned.append(entry['value'])
    
    # Distractor: unused transformation
    inverted = [1.0 / x if x != 0 else 0 for x in cleaned]
    return cleaned, artifact_flags

# Main execution
sensor_data = [
    {'value': 12, 'noise_level': 1},
    {'value': -6, 'noise_level': 4},
    {'value': 8, 'noise_level': 0},
    {'value': 15, 'noise_level': 2},
    {'value': -20, 'noise_level': 5}
]

threshold = 9

filtered_data, _ = filter_artifacts(sensor_data)

intermediate_result = analyze_frequency(filtered_data, sample_rate=50)

# Secondary processing path with distractors
shadow_buffer = [x ^ 3 for x in filtered_data if x > 0]
duplicate_check = len(filtered_data) != len(set(filtered_data))

# Core final computation
shift_value = len(filtered_data) % 5
context_sum = sum([x for i, x in enumerate(filtered_data) if i % 2 == 1])

# Use of zip to align indices and values meaningfully
paired_offsets = list(zip(filtered_data, [context_sum] * len(filtered_data)))
modulated = 0
for base, ctx in paired_offsets:
    modulated = (modulated + (base * ctx)) % 101

# Final integration step
final_output = (intermediate_result + modulated) % 10000

print(f"Result: {final_output}")