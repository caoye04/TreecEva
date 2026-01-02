from collections import defaultdict
import math

# Simulated sensor data processing system with diagnostic logic
def analyze_pattern(sequence):
    counter = defaultdict(int)
    for item in sequence:
        counter[item] += 1
    return sorted(counter.items())

def compute_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0 and total > 0:
            prob = v / total
            entropy -= prob * math.log(prob) if prob > 0 else 0
    return round(entropy, 6)

def detect_anomaly(readings, baseline):
    anomalies = []
    for i, r in enumerate(readings):
        if abs(r - baseline) > 2.5:
            anomalies.append(i)
    return anomalies if anomalies else [0]

def shift_cipher(text, shift):
    # Irrelevant cryptographic distraction
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def evaluate_stability(indices):
    # Misleading stability metric
    if len(indices) < 2:
        return False
    diffs = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    return all(d <= 3 for d in diffs)

def calculate_checksum(data_list):
    # Unused checksum function (dead code path)
    chk = 0
    for x in data_list:
        chk = (chk + x) * 11 % 7
    return chk

def filter_outliers(values, factor=1.5):
    # Distractor: Interquartile range filtering (not used in final result)
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]

def aggregate_metrics(timestamps, measurements):
    # Red herring aggregation
    metrics = defaultdict(list)
    for t, m in zip(timestamps, measurements):
        hour = t // 3600
        metrics[hour].append(m)
    avg_per_hour = {h: sum(vals)/len(vals) for h, vals in metrics.items()}
    return avg_per_hour

def process_readings(data, config):
    # Core relevant logic starts here
    base_ref = config['reference']
    tolerance = config['tolerance']
    
    # Step 1: Extract magnitude from complex-like readings (real part only)
    magnitudes = [abs(x) for x in data if isinstance(x, (int, float))]
    
    # Step 2: Apply threshold filtering (relevant)
    filtered = [m for m in magnitudes if m >= base_ref - tolerance]
    
    # Step 3: Compute statistical moment (skew-related, but simplified)
    n = len(filtered)
    if n == 0:
        skew_proxy = 0
    else:
        mean_val = sum(filtered) / n
        variance = sum((x - mean_val)**2 for x in filtered) / n
        if variance > 0:
            skew_proxy = sum((x - mean_val)**3 for x in filtered) / (n * variance**1.5)
        else:
            skew_proxy = 0
    
    # Step 4: Character analysis from metadata key (using string method)
    key_string = config['mode']
    char_groups = defaultdict(int)
    for ch in key_string:
        if ch in 'aeiou':
            char_groups['vowel'] += 1
        elif ch.isalpha():
            char_groups['consonant'] += 1
    
    # Step 5: Bitwise combination of control flags (relevant)
    mode_flag = len(key_string) ^ 7  # XOR operation
    vowel_count = char_groups['vowel']
    flag_state = (mode_flag | int(skew_proxy * 10)) & 15  # OR and AND masking
    
    # Step 6: Conditional adjustment based on length patterns
    length_code = len(filtered) & 3  # Modulo via bitwise
    adjustment = 0
    if length_code == 0:
        adjustment = 4
    elif length_code == 1:
        adjustment = -2
    elif length_code == 2:
        adjustment = 7
    else:
        adjustment = 1
    
    # Step 7: Combine into diagnostic code (this is the real answer)
    raw_diagnostic = int(abs(skew_proxy * 100)) + flag_state * 10 + adjustment
    
    # Step 8: Final transformation using character count (relevant)
    final_diagnostic = raw_diagnostic ^ (vowel_count * 11)  # Key XOR step
    
    # Irrelevant post-processing (distractor)
    encoded_diag = shift_cipher(f"diag{final_diagnostic}", 5)
    entropy_check = compute_entropy([final_diagnostic % 100, (final_diagnostic//100) % 100, final_diagnostic//1000])
    
    return final_diagnostic  # Only this matters

# Main execution block
if __name__ == "__main__":
    # Input data
    sensor_data = [1.2, -3.4, 5.6, 2.1, 0.8, -6.7, 4.3, 5.5, 2.9, 3.0, 1.1, 2.2]
    
    # Configuration with meaningful parameters
    thresholds = {
        'reference': 2.5,
        'tolerance': 1.0,
        'mode': 'adaptive_filter'
    }
    
    # Irrelevant preprocessing
    timestamp_log = list(range(1000, 2200, 100))
    extended_diagnostics = analyze_pattern(['A','B','A','C','B','A'])
    
    # Critical execution point
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")