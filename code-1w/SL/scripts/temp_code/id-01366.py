import math

# Simulated sensor fusion system for environmental monitoring
def collect_readings():
    raw_signals = [127, 255, 192, 64, 224, 32, 168, 96]
    noise_floor = 42
    adjusted = [val ^ noise_floor for val in raw_signals]
    return adjusted

# Irrelevant auxiliary function (dead code path)
def deprecated_normalization(data):
    max_val = max(data)
    return [x / max_val * 100 for x in data]

# Signal classification (distractor logic)
def classify_signal_strength(val):
    if val > 200:
        return 'strong'
    elif val > 100:
        return 'moderate'
    else:
        return 'weak'

# Main processing pipeline
def preprocess_signal(signal_list):
    filtered = []
    for x in signal_list:
        if x & 1:  # Keep only even values
            x += 1
        shifted = x >> 1
        if shifted % 3 == 0:
            shifted = shifted ^ 17
        filtered.append(shifted)
    return filtered

# Red herring transformation (unused in final chain)
def legacy_compression(data):
    compressed = 0
    for i, val in enumerate(data):
        compressed += val * (2 ** (i % 5))
    return compressed % 10000

# Core analysis engine
def generate_threshold_map(config_level=3):
    base_map = {}
    for i in range(10):
        key = (i * 7) % 13
        value = int(math.sin(i * 0.5) * 100) + config_level * 10
        base_map[key] = abs(value)
    return base_map

# Critical data transformation (mixed arithmetic and logic)
def transform_sequence(seq, factor):
    result = []
    running = factor
    for idx, val in enumerate(seq):
        temp = val
        if idx % 2 == 0:
            temp = (temp * 2) + running
        else:
            temp = (temp - running) // 2
        running = (running + temp) % 25
        result.append(temp)
    return result

# Primary diagnostic analyzer
def analyze_readings(data, thresholds):
    score = 0
    penalty = 0
    
    for i, reading in enumerate(data):
        key = i % 13
        ref = thresholds.get(key, 15)
        
        # Conditional expression with side-effect-free branching
        adjustment = ref * 1.5 if reading > 100 else ref * 0.75
        
        if reading > ref:
            score += int(adjustment)
        elif reading < ref:
            penalty += int(ref - reading)
        else:
            score += 5
    
    # Final computation using complex interdependent logic
    stability_index = len([x for x in data if x % 4 == 0])
    score = score - penalty
    score += stability_index * 3
    
    # Decoy calculation (looks important but unused)
    outlier_ratio = sum(1 for x in data if x > 200) / len(data) if data else 0
    normalized_score = math.tanh(score / 100.0)
    
    return int(score)

# Orchestration with misleading intermediate steps
if __name__ == "__main__":
    readings = collect_readings()
    
    # Distractor: unused classification
    classifications = [classify_signal_strength(x) for x in readings]
    
    processed = preprocess_signal(readings)
    
    # Another red herring: legacy compression not used in final result
    legacy_code = legacy_compression(processed)
    
    transformed = transform_sequence(processed, 7)
    
    # Threshold generation appears complex but deterministic
    threshold_map = generate_threshold_map(config_level=3)
    
    # Final diagnostic uses only this variable
    final_diagnostic = analyze_readings(transformed, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")