import itertools

def analyze_signal(data):
    # Apply lambda to detect significant fluctuations
    detector = lambda x: abs(x[0] - x[1]) > 15
    pairs = zip(data, data[1:])
    spikes = list(filter(detector, pairs))
    
    # Count spike occurrences using itertools
    spike_count = sum(1 for _ in itertools.islice(spikes, None))
    
    # Simple bitwise weighting based on count
    weighted_score = spike_count ^ 7  # XOR with fixed weight
    base_level = 50
    energy_threshold = base_level + weighted_score
    return energy_threshold

# Simulated sensor data (voltage readings)
data_points = [102, 118, 101, 85, 90, 121, 105, 65, 88, 100]

# Preprocess: compress by averaging consecutive triplets
compressed_data = [
    sum(data_points[i:i+3]) // 3 
    for i in range(0, len(data_points), 3)
]

# Execute analysis
energy_threshold = analyze_signal(compressed_data)
print(f"Result: {energy_threshold}")