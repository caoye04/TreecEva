from collections import defaultdict, Counter
import math

def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    smoothed = []
    for i in range(len(normalized)):
        window = normalized[max(0, i-2):min(i+3, len(normalized))]
        smoothed.append(sum(window) / len(window))
    return smoothed

def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def evaluate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    stability_score = math.exp(-variance)
    return stability_score

def main():
    # Irrelevant sensor data (distractor)
    legacy_sensor_log = [0.12, 0.33, 0.05, 0.88, 0.41, 0.76, 0.24, 0.59]
    calibration_offsets = {i: math.sin(i * 0.5) for i in range(10)}
    adjusted_offsets = [round(v, 2) for v in calibration_offsets.values()]

    # Core input data
    raw_readings = [4, 2, 9, 2, 7, 4, 2, 9, 1, 5]

    # Distractor: unused transformation path
    def obsolete_transform(x):
        return (x << 2) ^ 7
    mapped_values = [obsolete_transform(x) for x in raw_readings]  # Dead computation

    # Relevant preprocessing
    processed = preprocess_signal([x * 0.3 for x in raw_readings])

    # Introduce red herring with combinatorics
    combinations_count = 0
    for i in range(len(raw_readings)):
        for j in range(i+1, len(raw_readings)):
            if raw_readings[i] != raw_readings[j]:
                combinations_count += 1
    expected_combinations = math.comb(len(raw_readings), 2)  # Misleading exact value

    # Generate Fibonacci-based weights (partially relevant)
    weights = generate_sequence(10)
    weighted_sum = sum(processed[i % len(processed)] * weights[i] for i in range(8))

    # Bit manipulation decoy
    accumulator = 0
    for val in raw_readings:
        accumulator ^= val
        accumulator = (accumulator << 1) & 0xFF
    final_hash = accumulator  # Looks important but unused

    # Real processing begins
    freq_map = Counter(raw_readings)
    mode_value = freq_map.most_common(1)[0][1]
    threshold = math.sqrt(mode_value ** 2.5)

    temp_store = defaultdict(list)
    for idx, val in enumerate(processed):
        bucket = idx % 3
        temp_store[bucket].append(val)

    aggregated = []    
    for key in sorted(temp_store.keys()):
        segment = temp_store[key]
        if len(segment) > 1:
            segment_avg = sum(segment) / len(segment)
            segment_max = max(segment)
            # Only this transformed value matters
            transformed = (segment_avg * segment_max) + 0.5
            aggregated.append(transformed)

    # Critical transformation
    transformed_data = [round(x, 2) for x in aggregated]

    # Actual analysis function
    def analyze_pattern(data, limit):
        if not data:
            return 0
        peak = max(data)
        base = min(data)
        ratio = peak / base if base else float('inf')
        score = int((ratio * 100)) % 89

        # Real answer depends on this conditional chain
        if score > limit:
            result = (score * 3) - 17
        elif score == int(limit):
            result = score * 2
        else:
            result = (score + int(limit)) * 2

        # Final interference: complex-looking but irrelevant sorting
        sorted_data = sorted(data, reverse=True)
        entropy = 0
        for p in data:
            if p > 0:
                entropy -= p * math.log(p)
        # End of distractions

        return result  # This is what we actually need

    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()