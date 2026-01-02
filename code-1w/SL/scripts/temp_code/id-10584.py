def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def xor_cipher(data, key):
    # Irrelevant encryption-like function
    return [d ^ key for d in data]


def evaluate_health_metric(sensor_readings):
    baseline = sum(sensor_readings[:5]) / 5
    deviations = [abs(x - baseline) for x in sensor_readings]
    return sum(deviations)


def transform_sequence(seq, factor):
    # Apply non-linear transformation
    return [int(x * factor + (x % 2)) for x in seq]


def analyze_pattern(data, limit):
    count = 0
    running = 0
    for i, val in enumerate(data):
        if val > limit:
            count += 1
            running ^= val
        else:
            running += val % 7
    return count * running

# Main execution with distractions
raw_data = list(range(1, 18))
raw_data.reverse()

# Irrelevant signal processing chain
signal_noise = [x * 0.5 + 2 for x in raw_data]
processed_signal = preprocess_signal(signal_noise)
health_score = evaluate_health_metric(processed_signal)  # Red herring

# Core computation path disguised among others
fibo_seq = generate_sequence(10)
decoy_encrypted = xor_cipher(fibo_seq, 7)  # Dead path
scaling_factor = 3.7
transformed_data = transform_sequence(fibo_seq, scaling_factor)

# Multiple thresholds evaluated but only one used
thresholds = [10, 25, 44, 60]
interim_results = []
for t in thresholds:
    interim_results.append(analyze_pattern(transformed_data, t))

# Key statement
final_diagnostic = analyze_pattern(transformed_data, thresholds[2])

# Print final result as required
print(f"Result: {final_diagnostic}")