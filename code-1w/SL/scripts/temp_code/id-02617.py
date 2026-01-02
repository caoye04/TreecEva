def preprocess_signal(raw_samples):
    # Irrelevant transformation (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.3]
    reshaped = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
    transposed = list(zip(*[sub for sub in reshaped if len(sub) == 3]))
    return transposed

# Misleading auxiliary function (dead-end logic)
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Core processing chain
def transform_sequence(seq):
    shifted = [(x * 2 + 1) % 256 for x in seq]
    sliced_part = shifted[5:15]  # Use of slicing
    inverted = [255 - x for x in sliced_part]
    grouped = [inverted[i:i+2] for i in range(0, len(inverted), 2)]
    flattened = [item for group in grouped for item in group]
    return flattened

# Data generation with decoy values
def generate_baseline(count):
    base = []
    val = 7
    for i in range(count):
        val = (val * 97 + 13) % 1000
        base.append(val)
    return base[:50]

# Key analysis function
def analyze_pattern(data):
    total = 0
    for i, chunk in enumerate(data):
        if len(chunk) >= 2:
            product = chunk[0] * chunk[1]
            total += (product ^ i) % 100
    return total - len(data)

# Main execution flow
if __name__ == '__main__':
    # Generate real input data
    sensor_readings = [12, 45, 67, 89, 101, 112, 130, 144, 150, 163, 
                       177, 188, 190, 201, 215, 222, 230, 244, 250, 255]

    # Distractor block: Unused but plausible computation
    stats_summary = {
        'mean': sum(sensor_readings) / len(sensor_readings),
        'peak': max(sensor_readings),
        'noise_floor': min(sensor_readings),
        'variance': sum((x - sum(sensor_readings)/len(sensor_readings))**2 for x in sensor_readings) / len(sensor_readings)
    }

    # Real processing begins here
    processed = transform_sequence(sensor_readings)

    # More distractions: unused transformed variants
    alternate_path = [x for x in processed if x % 3 == 0]
    masked_data = [x ^ 255 for x in processed]
    reversed_slice = processed[::-1]  # Slicing distraction

    # Structuring data for final analysis
    structured_chunks = [processed[i:i+3] for i in range(0, len(processed), 3)]
    cleaned_chunks = [chunk for chunk in structured_chunks if sum(chunk) > 100]

    # Final key computation
    final_diagnostic = analyze_pattern(cleaned_chunks)

    # Print result as required
    print(f"Target result: {final_diagnostic}")