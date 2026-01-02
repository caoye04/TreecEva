from collections import defaultdict, Counter
import math

# Simulated sensor array data for a distributed environmental monitoring system
def generate_sensor_grid():
    grid = {}
    for i in range(5):
        for j in range(5):
            key = (i, j)
            # Real signal embedded in noise
            base = (i + 1) * (j + 1)
            noise = (i * j + abs(i - j)) % 3
            grid[key] = base + noise
    return grid

# Irrelevant auxiliary function – dead code path (distractor)
def compute_flow_dynamics(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                total += matrix[i][j] * (i - j) ** 2
    return total

# Secondary processing: extract feature patterns
def extract_features(raw_data):
    features = defaultdict(int)
    magnitude = 0
    for (x, y), val in raw_data.items():
        if x % 2 == 0 and y % 2 == 0:
            features['quad_even'] += val
        elif x % 3 == 0:
            features['triples'] += val
        magnitude += val ** 0.5
    features['magnitude'] = int(magnitude)
    return features

# Signal normalization using sliding window reference (unused distractor)
def normalize_signal(stream, window_size=3):
    normalized = []
    for i in range(len(stream)):
        window = stream[max(0, i - window_size):i + 1]
        avg = sum(window) / len(window)
        normalized.append(stream[i] / (avg + 1e-8))
    return normalized

# Core analysis logic with multiple steps and red herrings
def analyze_metrics(signature, baseline):
    # Step 1: Compute phase coherence
    coherence = 0
    for i, val in enumerate(signature):
        if i % 2 == 0:
            coherence += val * (i + 1)
        else:
            coherence -= val * (i % 4)
    
    # Step 2: Frequency shift correction (irrelevant to final result)
    shifted = []
    for x in signature:
        shifted.append((x * 17) % 19)
    
    # Step 3: Baseline delta mapping
    deltas = []
    for a, b in zip(signature, baseline):
        deltas.append(abs(a - b))
    
    # Step 4: Entropy approximation
    count_map = Counter(deltas)
    entropy = 0
    total = sum(count_map.values())
    for count in count_map.values():
        p = count / total
        entropy -= p * math.log(p) if p > 0 else 0
    
    # Step 5: Weighted anomaly index
    anomaly_index = 0
    for i, d in enumerate(deltas):
        weight = (i + 1) ** 0.5
        anomaly_index += d * weight * (0.9 ** i)
    
    # Step 6: Masking operation with bit manipulation (distractor)
    masked_value = 0
    temp = int(anomaly_index)
    for _ in range(8):
        temp = (temp ^ (temp << 1)) & 0xFFFF
        masked_value ^= temp
    
    # Step 7: Final diagnostic score computation (ACTUAL ANSWER PATH)
    # Only this calculation feeds into the returned value
    adjustment_factor = len(signature) / (entropy + 1)
    final_score = int(anomaly_index / adjustment_factor) * 3
    
    # Multiple decoy variables below (misleading intermediate results)
    spurious_metric_1 = (coherence * entropy) // (len(deltas) + 1)
    spurious_metric_2 = sum(shifted[:5]) - masked_value
    phantom_sum = sum([v for v in count_map.values() if v % 2 == 1])
    dummy_flag = spurious_metric_1 > spurious_metric_2 and phantom_sum < 100
    
    # Critical red herring: unused but plausible-looking return candidate
    fallback_diagnostic = (spurious_metric_1 + spurious_metric_2) // 2
    
    # ACTUAL return value
    return final_score

# Main execution block
if __name__ == '__main__':
    # Generate real input data
    sensor_data = generate_sensor_grid()
    
    # Extract meaningful signature from grid (only specific cells used)
    ordered_vals = []
    for i in range(5):
        for j in range(5):
            if (i + j) % 3 == 0:  # non-uniform sampling pattern
                ordered_vals.append(sensor_data[(i, j)])
    
    health_signature = [v % 13 for v in ordered_vals]  # Normalized signal
    
    # Baseline readings (fixed reference pattern)
    baseline_readings = [5, 3, 8, 2, 7, 4, 6, 9, 1, 5, 3, 8, 2]  # Length matches filtered signature
    
    # Dead code branch — never executed (control flow distraction)
    if len(health_signature) < 5:
        backup_system = [[i*j for j in range(4)] for i in range(4)]
        alt_result = compute_flow_dynamics(backup_system)
    
    # Core analysis call — produces final result
    final_diagnostic = analyze_metrics(health_signature, baseline_readings)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")