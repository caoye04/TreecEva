import math

def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    transformed = list(map(lambda x: math.sin(x) * math.cos(x), filtered))
    normalized = [val / max(transformed) if max(transformed) != 0 else 0 for val in transformed]
    return sum(normalized[:3])


def evaluate_stability(readings):
    diff_seq = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    squared_diffs = [d**2 for d in diff_seq]
    variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
    stability = math.exp(-variance)
    return stability


def compute_entropy(values):
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)


def simulate_calibration(sequence):
    shifted = sequence[::2] + [sequence[i] ** 0.5 for i in range(len(sequence)) if i % 3 == 0]
    processed = [x for x in shifted if x < 10]
    return processed[::-1]

# Irrelevant helper (dead path)
def unused_helper(x):
    return (x << 2) ^ 0xFF

# Misleading function with decoy logic
def assess_coherence(arr):
    if len(arr) < 5:
        return 0
    coherence_score = 0
    for i in range(len(arr)-1):
        if arr[i] * arr[i+1] < 0:
            coherence_score -= 1
        else:
            coherence_score += 1
    return coherence_score  # Never used

# Core logic with distractors
def process_performance(metrics, calibration_data):
    base_metric = metrics.get('amplitude', 0) * 1.5
    
    # Distraction: complex bit manipulation with no real impact
    magic_offset = (0xABCD ^ (len(calibration_data) & 0xFFFF)) >> 4
    dummy_flag = (magic_offset & 1) == 0
    
    # Real computation begins
    signal_data = metrics['readings']
    raw_stability = evaluate_stability(signal_data)
    
    # Another distraction: unused intermediate
    temp_analysis = [math.tanh(x) for x in signal_data if x != 0]
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    # Actual relevant transformation
    calibrated_values = simulate_calibration(calibration_data)
    entropy_value = compute_entropy(calibrated_values)
    
    # Red herring: conditional that always evaluates false due to domain constraints
    if len(calibrated_values) > 100:
        base_metric *= 0.1
    
    # Key processing step
    signal_strength = analyze_signal(signal_data, threshold=0.75)
    
    # Final composition using only select components
    adjustment_factor = 1 + raw_stability + entropy_value
    preliminary_score = base_metric * adjustment_factor * abs(signal_strength)
    
    # Distractor: complex-looking but unused calculation
    shadow_score = 0
    for i, val in enumerate(calibrated_values):
        shadow_score += val * (0.9 ** i)
    shadow_score = round(shadow_score, 3)
    
    # Critical assignment
    final_score = int(preliminary_score + 0.5)  # Round to nearest integer
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data with meaningful structure
    metrics = {
        'amplitude': 12,
        'readings': [0.8, 1.2, 0.9, 1.1, 1.0, 0.85],
        'timestamp': 1678886400,
        'mode': 'high_res'
    }
    
    calibration_data = [2, 4, 6, 8, 3, 9, 1, 5]
    
    # Dead variable (misleading)
    system_hash = (calibration_data[0] << 8) | calibration_data[-1]
    
    # Trigger key computation
    final_score = process_performance(metrics, calibration_data)
    
    # Output result as required
    print(f"Result: {final_score}")