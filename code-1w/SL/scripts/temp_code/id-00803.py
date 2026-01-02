from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_samples):
    filtered = []
    noise_floor = 0.05
    for sample in raw_samples:
        if abs(sample) > noise_floor:
            filtered.append(round(sample * 100) / 100)
    return filtered

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 6)

def shift_window(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    return windows

def detect_spikes(series, threshold=2):
    spikes = []
    avg = sum(series) / len(series)
    std_dev = (sum((x - avg) ** 2 for x in series) / len(series)) ** 0.5
    for val in series:
        if abs(val - avg) > threshold * std_dev:
            spikes.append(val)
    return spikes  # Unused in final result - red herring

def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return checksum % 1000  # Distractor computation

def transform_sequence(data):
    result = []
    multiplier = 1.5
    offset = -0.5
    for x in data:
        transformed = x ** 2 * multiplier + offset
        if transformed > 100:
            transformed = 100
        elif transformed < -100:
            transformed = -100
        result.append(round(transformed, 4))
    return result

def analyze_pattern(dataset, params):
    temp_results = defaultdict(float)
    segment_a = dataset[:len(dataset)//2]
    segment_b = dataset[len(dataset)//2:]
    
    # Meaningful calculation branch
    if params['mode'] == 'deep':
        windowed = shift_window(segment_a, 3)
        scores = []
        for win in windowed:
            score = (win[0] * 0.2) + (win[1] * 0.5) + (win[2] * 0.3)
            scores.append(abs(score))
        temp_results['aggregate'] = sum(scores) * params['sensitivity']
        
        # Critical path: entropy used in final answer
        entropy_val = compute_entropy([int(x) for x in segment_b if -50 < x < 50])
        temp_results['entropy'] = entropy_val
        
        # Red herring: complex but unused logic
        fake_weights = [0.1, 0.3, 0.6]
        dummy_score = 0
        for i, w in enumerate(fake_weights):
            if i < len(segment_a):
                dummy_score += segment_a[i] * w * params.get('dummy_factor', 0)
        temp_results['dummy'] = dummy_score
        
        # Final computation
        base = temp_results['aggregate']
        adjustment = temp_results['entropy'] * 100
        final_value = int(base + adjustment)
        
        # Dead code path - never executed due to mode
        if params['mode'] == 'debug':
            return -999  # Unreachable
        
        return final_value

    return -1

# Main execution flow
if __name__ == '__main__':
    # Raw sensor input (simulated)
    raw_sensor_data = [
        0.12, -0.34, 0.56, 0.11, -0.29, 0.51, 0.62, -0.41,
        0.23, 0.71, 0.19, -0.28, 0.33, 0.44, 0.66, -0.52
    ]
    
    # Irrelevant preprocessing chain
    cleaned = preprocess_readings(raw_sensor_data)
    checksum_early = generate_checksum([int(x*10) for x in cleaned])  # Unused
    spike_list = detect_spikes(cleaned, threshold=1.8)  # Computed but not used
    
    # Transform data through multiple stages
    enhanced_data = [x * 2.1 for x in cleaned]
    processed_batch = transform_sequence(enhanced_data)
    
    # Add decoy structure
    decoy_map = defaultdict(int)
    for i, val in enumerate(processed_batch):
        decoy_map[f'item_{i % 5}'] += int(abs(val))
    # Decoy map never used again
    
    # Configuration with misleading keys
    config = {
        'mode': 'deep',
        'sensitivity': 2.3,
        'dummy_factor': 5.0,  # Looks important but only used in dead branch
        'debug_mode': False,
        'buffer_size': 1024
    }
    
    # Core transformation before analysis
    transformed_data = []
    for val in processed_batch:
        if val > 0:
            transformed_data.append(math.log(val + 10))
        else:
            transformed_data.append(math.sqrt(abs(val) + 9))
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")