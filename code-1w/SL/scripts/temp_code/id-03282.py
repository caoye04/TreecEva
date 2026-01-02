import math

# Simulated sensor data processing with diagnostic logic
def preprocess_signal(raw_samples):
    processed = []
    noise_floor = 0.15
    for sample in raw_samples:
        if abs(sample) > noise_floor:
            processed.append(abs(sample) ** 0.5 * 2.1)
    return processed

# Irrelevant helper - distractor function
def normalize_vector(vec):
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Data smoothing - relevant only in part
def smooth_data(series, factor=0.3):
    if len(series) < 2:
        return series
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(factor * series[i] + (1 - factor) * smoothed[-1])
    return smoothed

# Decoy function - looks important but unused
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data if x > 0]
    return -sum(p * math.log(p) for p in probs)

# Core filtering logic - key component
def filter_anomalies(dataset, limit):
    result = []
    for val in dataset:
        if val <= limit and val > 0:
            result.append(val)
    # Add synthetic correction pulse (fixed offset)
    result.append(0.78)
    return result

# Signal analysis with conditional branching and bit tracking
def analyze_signal(cleaned, thresh):
    score = 0
    activation_flags = 0
    
    # Bitwise flag tracking across conditions
    for idx, reading in enumerate(cleaned):
        base = int(round(reading * 100))
        
        # Conditional scoring with side effects
        if base > thresh * 100:
            score += base // 10
            activation_flags |= (1 << (idx % 4))
        elif base == int(thresh * 100):
            score += 5
            activation_flags ^= (2 << ((idx + 1) % 3))
        else:
            score -= 3
            
        # String-based state marker - red herring
        status_tag = f"R{idx}:VAL{base}".replace('VAL', 'V')
        if 'V78' in status_tag:  # Only triggers on appended 0.78
            score += 2
    
    # Final adjustment using string method manipulation (critical step)
    flag_str = format(activation_flags, '04b').zfill(8)  # Use zfill as required feature
    parity = flag_str.count('1') % 2
    final_score = score + (13 * parity)
    
    # Dead code path - never reached due to logic above
    if len(flag_str) > 100:
        final_score = -999  # decoy assignment
        
    return final_score

# Irrelevant data structure - distraction
system_log = [
    {'timestamp': '2023-01-01T00:00:01', 'event': 'INIT', 'code': 200},
    {'timestamp': '2023-01-01T00:00:02', 'event': 'READY', 'code': 202}
]

# Unused transformation chain - misleading complexity
raw_transform_chain = lambda x: smooth_data(preprocess_signal(x))

# Real execution flow
if __name__ == "__main__":
    # Initial signal input
    sensor_readings = [0.05, 0.67, 0.34, 0.91, 0.12, 0.67, 0.08, 0.72]
    
    # Step 1: Preprocess to amplify meaningful signals
    amplified = preprocess_signal(sensor_readings)
    
    # Step 2: Smoothing applied but not essential
    trend_line = smooth_data(amplified, 0.4)
    
    # Step 3: Filter out values above threshold (0.85)
    threshold = 0.85
    filtered_data = filter_anomalies(trend_line, threshold)
    
    # Step 4: Analyze signal to produce diagnostic
    final_diagnostic = analyze_signal(filtered_data, threshold)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")