import math

# Simulated sensor array data from environmental monitoring station
def fetch_sensor_data():
    raw_values = [127, 255, 0, 64, 192, 32, 96, 160]
    timestamps = [1623456000 + i*60 for i in range(8)]
    metadata = {'location': 'Zone-D', 'version': '3.1', 'calibrated': True}
    return list(zip(timestamps, raw_values))

# Signal conditioning with noise filtering (relevant and irrelevant transformations)
def preprocess_signal(data_pair):
    timestamp, reading = data_pair
    
    # Irrelevant transformation: timestamp scrambling (dead path)
    scrambled = ((timestamp >> 16) & 0xFF) ^ (timestamp & 0xFFFF)
    
    # Relevant: normalize reading to 0-1 scale
    normalized = reading / 255.0
    
    # Distractor: compute unused checksum
    chksum = (reading ^ 0xAA) + 0x55
    
    # Apply logarithmic sensitivity curve (relevant only if reading > 0)
    if reading > 0:
        log_adjusted = math.log(normalized * 10 + 1) / math.log(11)
    else:
        log_adjusted = 0.0
    
    # Return only the relevant processed signal
    return log_adjusted

# Legacy function - never called but adds confusion
def legacy_calibrate(x):
    return (x * 2.041) % 1.0

# Main processing pipeline
def process_all_sensors(sensor_data):
    # Extract readings and apply preprocessing
    filtered_data = []
    for item in sensor_data:
        proc_val = preprocess_signal(item)
        if proc_val > 0.3:  # Threshold filter
            filtered_data.append(proc_val)
    
    # Distractor: unused statistical artifacts
    mean_proxy = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance_proxy = sum((x - mean_proxy)**2 for x in filtered_data) / len(filtered_data) if filtered_data else 0
    
    # Critical transformation: amplify via sigmoid compression
    amplified = [1 / (1 + math.exp(-5 * (x - 0.5))) for x in filtered_data]
    
    # Decoy operation: string-based encoding (never used)
    encoded_str = ''.join([chr(int(65 + 25 * val)) for val in amplified[:3]]) if amplified else 'N/A'
    
    return amplified

# Diagnostic engine
def analyze_readings(signals):
    if not signals:
        return -1
    
    # Compute weighted impulse score
    weights = [math.sin(i * math.pi / len(signals)) for i in range(len(signals))]
    impulse_score = sum(s * w for s, w in zip(signals, weights))
    
    # Red herring: entropy calculation (not used in output)
    def shannon_entropy(lst):
        from collections import Counter
        counts = Counter(round(x, 1) for x in lst)
        total = sum(counts.values())
        return -sum((count/total) * math.log2(count/total) for count in counts.values())
    
    entropy_diagnostic = shannon_entropy(signals)  # Computed but unused
    
    # Secondary metric: zero-crossing approximation (distractor)
    zero_crossings = sum(1 for i in range(1, len(signals)) if signals[i]*signals[i-1] < 0)
    
    # Final diagnostic: cumulative activation above threshold
    threshold = 0.7
    active_periods = [1 for x in signals if x > threshold]
    
    # Key result computation
    base_count = len(active_periods)
    bonus = 0.5 if len(signals) > 4 else 0
    penalty = 0.25 * zero_crossings
    final_diagnostic = int(base_count * 100 + bonus * 100 - penalty * 100)
    
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    # Fetch raw sensor input
    raw_input = fetch_sensor_data()
    
    # Process signal chain
    processed_signals = process_all_sensors(raw_input)
    
    # Generate final system diagnosis
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")