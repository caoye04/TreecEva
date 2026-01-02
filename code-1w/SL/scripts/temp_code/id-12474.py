import math

# Simulated bio-signal processing pipeline with diagnostic analysis
def preprocess_signal(raw_points):
    filtered = [x for x in raw_points if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-9) for x in filtered]
    return normalized

# Irrelevant transformation: frequency domain mock-up
def compute_harmonics(samples):
    harmonics = []
    for i in range(len(samples)):
        harmonics.append(math.sin(samples[i] * math.pi) * math.cos(i * 0.5))
    # Dead code path — never used
    if len(harmonics) > 100:
        return [h * 2 for h in harmonics]
    return harmonics[:50]

# Distractor function: energy profile calculation (not used in final result)
def calculate_energy(signal_chunk):
    return sum([x ** 2 for x in signal_chunk]) * 0.5

# Core pattern transformer: applies non-linear shift based on index parity
def transform_sequence(data):
    shifted = []
    for idx, val in enumerate(data):
        if idx % 2 == 0:
            shifted.append(val + math.log(1 + idx))
        else:
            shifted.append(val - math.atan(idx))
    return shifted

# Diagnostic analyzer: computes weighted anomaly score
def analyze_pattern(seq):
    weights = [0.1 * (i + 1) for i in range(len(seq))]
    anomalies = 0.0
    for i, x in enumerate(seq):
        deviation = abs(x - 0.5)
        anomalies += deviation * weights[i]
    return int(anomalies * 1000)  # Final quantized diagnostic code

# Unused auxiliary functions — red herrings
def generate_baseline(n):
    return [math.exp(-i / n) for i in range(n)]

def validate_coherence(signal):
    return all(x >= 0 for x in signal)

# Main execution flow
if __name__ == "__main__":
    # Simulated neural interface data stream
    raw_neural_data = [0.05, -0.32, 0.71, 0.15, -0.83, 0.92, 0.01, 0.63, -0.44, 0.77, 
                       0.21, -0.19, 0.68, 0.88, -0.51, 0.33, 0.75, -0.22, 0.41, 0.69]

    # Step 1: Preprocess to remove noise floor
    processed_trace = preprocess_signal(raw_neural_data)

    # Step 2: Apply harmonic analysis (distractor — result unused)
    spectral_analysis = compute_harmonics(processed_trace)

    # Step 3: Transform sequence using index-based non-linearity
    transformed_data = transform_sequence(processed_trace)

    # Step 4: Analyze transformed data for diagnostic code
    final_diagnostic = analyze_pattern(transformed_data)

    # Print result as required
    print(f"Target result: {final_diagnostic}")