import math

def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

def normalize_vector(v):
    norm = math.sqrt(sum(x ** 2 for x in v))
    return [x / norm for x in v] if norm > 0 else v

def compute_entropy(values):
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def evaluate_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs) if diffs else 0.0

def simulate_load(balance_factor, iterations=100):
    result = 0
    for i in range(iterations):
        result += (i % balance_factor) * 0.1
    return result

def main():
    # Simulated sensor metrics (irrelevant: some are decoys)
    temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8, 24.2, 23.6]
    pressure_data = [101.3, 102.1, 100.7, 103.4, 101.9]
    vibration_levels = [0.12, 0.34, 0.21, 0.45, 0.31, 0.28, 0.33]
    humidity_samples = [45, 47, 50, 44, 52, 48, 46]

    # Distractor: unused function call
    _ = simulate_load(7, 50)

    # Irrelevant transformation
    normalized_vib = normalize_vector(vibration_levels)
    entropy_vib = compute_entropy(vibration_levels)

    # Real metric extraction
    temp_trend = sum(temperature_readings) / len(temperature_readings)
    pressure_spike = max(pressure_data) - min(pressure_data)
    vib_rms = math.sqrt(sum(x**2 for x in vibration_levels) / len(vibration_levels))

    # Early stability check (red herring)
    stability_score = evaluate_stability(humidity_samples)

    # Key metrics used in final calculation
    signal_strength = analyze_signal(vibration_levels, threshold=0.25)
    baseline_offset = temp_trend - 20.0
    fluctuation_index = pressure_spike * 0.5

    # Distractor: complex but unused bitwise manipulation
    magic_flag = 0b1010
    magic_flag ^= 0b1100
    magic_flag >>= 1
    flag_meaning = "valid" if magic_flag == 1 else "invalid"

    # Weighted metrics (only three are actually used)
    metrics = {
        'signal': signal_strength,
        'offset': baseline_offset,
        'fluctuation': fluctuation_index,
        'entropy': entropy_vib,  # Unused
        'stability': stability_score  # Unused
    }

    weights = {
        'signal': 0.4,
        'offset': 0.3,
        'fluctuation': 0.3
        # 'entropy' and 'stability' weights omitted intentionally
    }

    def aggregate_performance(mets, wts):
        score = 0.0
        for key in wts:
            if key in mets:
                score += mets[key] * wts[key]
        return round(score, 6)

    final_score = aggregate_performance(metrics, weights)

    # Redundant print for distraction
    print(f"Debug: Stability={stability_score}, Entropy={entropy_vib}")
    print(f"Signal analysis: {signal_strength}")

    # Critical output
    print(f"Target result: {final_score}")

    # Dead code path
    if False:
        fallback = sum(humidity_samples) // len(humidity_samples)
        print(f"Fallback reference: {fallback}")

    return final_score

if __name__ == "__main__":
    main()