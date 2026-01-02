import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_signals = [0.78, 0.65, 0.92, 0.41, 0.58]
    baseline = 0.5
    tolerance = 0.1
    filtered = [x for x in raw_signals if abs(x - baseline) > tolerance]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    return normalized

def compute_entropy(values):
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log(v)
    return round(entropy, 6)

def generate_checksum(data):
    # Irrelevant function: used as distractor
    checksum = 0
    for d in data:
        checksum ^= int(d * 100)
    return checksum + 5

def evaluate_stability(metrics):
    # Dead code path - never actually used in final computation
    if len(metrics) < 3:
        return False
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    return variance < 0.05

def derive_key(signal_set):
    # Decoy transformation with bit manipulation red herring
    temp_key = 0
    for s in signal_set:
        temp_key += int(s * 10) ^ 7
    temp_key = (temp_key << 2) | (temp_key >> 1)
    return temp_key % 100

def analyze_pattern(readings, config):
    # Core logic embedded within distractions
    readings_set = set(round(r, 3) for r in readings)
    threshold_set = set(config)
    
    # Conditional expression determining inclusion
    processed = [x for x in readings if (x > config[0]) else (x + 0.1 if x < config[2] else x)]
    
    # Set difference creates filtered diagnostic input
    significant = list(readings_set - (readings_set - threshold_set))
    
    # Real calculation path
    magnitude = sum(math.sin(math.pi * x) for x in significant)
    adjustment = math.log(config[1] + 1)
    score = magnitude * adjustment
    
    # Multiple assignments with unpacking red herring
    temp_a, temp_b = 12, 24
    temp_a, temp_b = temp_b, temp_a  # Swapped but unused
    
    # Final result derived here
    final_diagnostic = int(abs(score * 1000))
    return final_diagnostic

# Irrelevant auxiliary functions and variables
LOGGING_ENABLED = True
def log_event(msg):
    if LOGGING_ENABLED:
        pass  # No-op logging - dead code

aux_data = [1.2, 3.4, 5.6]
meta_checksum = 0
for val in aux_data:
    meta_checksum += int(val ** 2)

# Unused data structure - distraction
historical_context = {
    'version': '2.1',
    'mode': 'diagnostic',
    'active': False
}

# Main execution flow
if __name__ == "__main__":
    collected_data = collect_sensor_readings()
    
    # Distractor variables
    entropy_metric = compute_entropy(collected_data)
    stability_flag = evaluate_stability(collected_data)
    key_fragment = derive_key(collected_data)
    
    # Actual configuration thresholds used in analysis
    thresholds = [0.4, 0.6, 0.8]
    
    # Key statement
    final_diagnostic = analyze_pattern(collected_data, thresholds)
    
    # Additional irrelevant computation
    outlier_count = len([x for x in collected_data if x < 0.45 or x > 0.85])
    weighted_sum = sum(x * (i+1) for i, x in enumerate(collected_data))
    
    print(f"Result: {final_diagnostic}")