import math

# Simulated sensor array diagnostics with signal processing and noise filtering
def collect_sensor_data():
    raw_values = [i * 1.5 + (i % 3) for i in range(18)]
    noise_floor = sum([math.sin(i / 2) for i in range(10)])
    calibrated = [v + noise_floor * 0.1 for v in raw_values]
    return calibrated

def filter_outliers(data, threshold=1.8):
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs((x - mean_val)) / stdev < threshold]
    return filtered

def generate_frequency_map(values):
    # Irrelevant frequency analysis (distractor)
    freq_map = {}
    for v in values:
        rounded = int(round(v % 5))
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    return freq_map

def shift_phase(signal_list, steps=2):
    # Unused phase shifting function (dead code path)
    shifted = signal_list[steps:] + signal_list[:steps]
    return shifted

def compress_signal(signal):
    # Decoy compression algorithm (irrelevant)
    return [round(s * 0.9) for s in signal]

def integrate_sections(data):
    sections = [data[i:i+4] for i in range(0, len(data), 4)]
    integrated = []
    for idx, section in enumerate(sections):
        if len(section) < 4:
            continue
        weighted = sum(section[j] * (j+1) for j in range(len(section)))
        normalized = weighted / 10.0
        integrated.append(normalized)
    return integrated

def validate_coherence(sequence):
    # Misleading validation logic
    total_change = sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))
    allowed_drift = len(sequence) * 0.5
    is_coherent = total_change <= allowed_drift
    return is_coherent  # never actually used

def analyze_readings(signals):
    # Core computation buried among distractors
    base_score = sum(math.cos(x / 10) for x in signals)
    adjustment = 0
    for i, val in enumerate(signals):
        if i % 3 == 0 and val > 5:
            adjustment += 1.5
        elif i % 4 == 0:
            adjustment -= 0.7
    final_score = base_score + adjustment
    return int(round(final_score * 2))

def main():
    # Primary execution flow
    raw_data = collect_sensor_data()
    processed_signals = filter_outliers(raw_data)
    
    # Distractor block: irrelevant transformations
    freq_analysis = generate_frequency_map(processed_signals)
    compressed = compress_signal(processed_signals)
    coherence = validate_coherence(compressed)
    integrated_segments = integrate_sections(processed_signals)
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_signals)
    
    # Dead code paths with misleading prints
    if len(integrated_segments) > 10:
        phase_shifted = shift_phase(integrated_segments)
        print(f"Phase adjusted: {phase_shifted[:3]}")
    
    # Output result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()