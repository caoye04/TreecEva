import math

def preprocess_signal(raw_samples):
    filtered = []
    noise_floor = 0.05
    for s in raw_samples:
        if abs(s) > noise_floor:
            filtered.append(s ** 2)
    return filtered


def generate_baseline(n):
    # Irrelevant function: generates unused baseline data
    return [math.sin(x * 0.1) for x in range(n)]


def extract_features(data_stream):
    features = {}
    magnitude = sum(abs(x) for x in data_stream)
    peaks = [i for i, x in enumerate(data_stream) if x > 0.5 and (i == 0 or data_stream[i-1] < x)]
    smoothed = [data_stream[i] * 0.9 + 0.1 for i in range(0, len(data_stream), 2) if i < len(data_stream)]
    
    # Distractor computation
    avg = magnitude / len(data_stream) if data_stream else 0
    temp_cache = {i: math.log(1 + v) for i, v in enumerate(data_stream)}
    
    features['magnitude'] = magnitude
    features['peak_count'] = len(peaks)
    features['smooth_influence'] = sum(smoothed) if smoothed else 0
    return features


def transform_sequence(seq, factor=1.5):
    # Applies transformation but also adds red herring variables
    doubled = [x * 2 for x in seq]
    shifted = [x + 0.1 for x in doubled]
    powered = [x ** factor for x in seq]
    
    # Real transformation used later
    return [math.sqrt(abs(x)) for x in powered]


def analyze_patterns(dataset, config):
    result = 0
    decoy_sum = 0
    for i, record in enumerate(dataset):
        if i % 3 == 0:
            result += config.get('base', 10) * len(record)
        elif i % 3 == 1:
            temp_val = sum(math.ceil(x) for x in record if x > 0.4)
            result -= temp_val
        else:
            zipped = list(zip(record[::2], record[1::2]))
            bonus = sum(a * b for a, b in zipped if a > b)
            result += int(bonus * 1.5)
        
        # Dead code path — never executed due to logic above
        if len(record) > 100:
            fallback = 0
            for item in record:
                fallback ^= hash(str(item))
            decoy_sum += fallback
    
    # Another distractor: recursive but unused
    def deep_integrate(arr):
        if len(arr) <= 1:
            return arr[0] if arr else 0
        return arr[0] + 0.5 * deep_integrate(arr[1:])
    
    return result

# Main execution with multiple distractions
if __name__ == '__main__':
    raw_input_data = [
        0.12, -0.33, 0.67, 0.81, -0.02, 0.45, 0.88, -0.76,
        0.15, 0.22, -0.11, 0.91, 0.63, 0.07, -0.55, 0.72
    ]
    
    # Unused variable - red herring
    calibration_matrix = [[i*j for j in range(3)] for i in range(4)]
    
    cleaned = preprocess_signal(raw_input_data)
    
    # Extract features (partially used)
    signal_features = extract_features(cleaned)
    
    # Transform data using meaningful but obscured logic
    transformed_data = []
    chunk_size = 4
    for i in range(0, len(cleaned), chunk_size):
        chunk = cleaned[i:i+chunk_size]
        if len(chunk) == chunk_size:
            transformed_data.append(transform_sequence(chunk, 1.8))
        else:
            # Padding that isn't actually used
            padded = chunk + [0.1] * (chunk_size - len(chunk))
            transformed_data.append(transform_sequence(padded, 1.8))
    
    # Build configuration with irrelevant entries
    thresholds = {
        'base': 7,
        'gain': 2.1,
        'saturation': 0.95,
        'window_size': 1024,
        'debug_mode': False,
        'decay_factor': 0.88
    }
    
    # UNUSED recursive diagnostic tree — dead code
    def build_diagnostic_tree(data):
        if not data:
            return None
        mid = len(data) // 2
        return {
            'value': data[mid],
            'left': build_diagnostic_tree(data[:mid]),
            'right': build_diagnostic_tree(data[mid+1:])
        }
    
    # Key statement
    final_diagnostic = analyze_patterns(transformed_data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")