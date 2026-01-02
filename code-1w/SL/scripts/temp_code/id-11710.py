from collections import defaultdict, Counter

# Simulated sensor data analysis with red herrings
def analyze_readings(data_stream):
    raw_samples = [x for x in data_stream if x > 0]
    filtered = list(filter(lambda x: x % 2 == 1, raw_samples))

    # Irrelevant transformation (decoy)
    normalized = [round((x - min(raw_samples)) / (max(raw_samples) - min(raw_samples)), 3) for x in raw_samples]
    avg_normalized = sum(normalized) / len(normalized)

    # Actual signal extraction (reused later)
    signal_peaks = [x for x in filtered if x > (sum(filtered) / len(filtered))]

    # Distractor: unused complex structure
    stats_map = defaultdict(lambda: defaultdict(int))
    for val in raw_samples:
        stats_map['magnitude'][val // 10] += 1
        stats_map['parity']['odd' if val % 2 else 'even'] += 1

    # Fake diagnostic path (dead code)
    def compute_stability_index(seq):
        return sum(seq[i] - seq[i-1] for i in range(1, len(seq))) / len(seq)
    
    stability_score = None  # Never used

    # Real processing begins here
    peak_count_map = Counter(signal_peaks)
    unique_peaks = len(peak_count_map)
    total_peak_energy = sum(peak_count_map.values())

    # Secondary filter: only strong peaks
    strong_peaks = [k for k, v in peak_count_map.items() if v >= 2]
    coherence_score = len(strong_peaks) * unique_peaks

    # Dummy string analysis (red herring)
    status_flags = ['OK', 'ERROR', 'WARNING', 'OK', 'OK']
    flag_distribution = Counter(status_flags)
    dominant_flag = max(flag_distribution, key=flag_distribution.get)
    flag_entropy = -sum((count / len(status_flags)) * __import__('math').log(count / len(status_flags)) 
                        for count in flag_distribution.values())

    # Another decoy: text-based weight (irrelevant)
    metadata_tag = "SENS-V3-CALIBRATED"
    calibration_weight = sum(map(ord, metadata_tag)) % 17

    # Core logic buried among distractions
    base_threshold = 42
    aggregate_score = 0
    for peak in signal_peaks:
        if peak > base_threshold:
            aggregate_score += peak // 3
        else:
            aggregate_score -= peak % 4

    # Temperature correction from unrelated calculation
    temp_log = "TEMP: 23.5C HUMID: 64%"  
    temperature_str = temp_log.split()[1].replace('C', '')
    temperature_val = float(temperature_str)
    temperature_factor = int(temperature_val // 2)

    # Final computation buried at end
    final_diagnostic = aggregate_score + temperature_factor

    # Unrelated print (misleading)
    print(f'Debug: Coherence={coherence_score}, Calibration={calibration_weight}')

    return final_diagnostic

# Input data stream
sensor_input = [105, -5, 88, 105, 72, 111, -3, 111, 95, 105, 64, 111]

result = analyze_readings(sensor_input)
print(f'Target result: {result}')