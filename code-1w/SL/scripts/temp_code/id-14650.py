from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [14, 17, 23, 17, 14, 23, 19, 23, 25, 14, 19, 21, 21, 25, 17]

def apply_noise_filter(data):
    filtered = []
    for i in range(len(data)):
        if i == 0 or i == len(data) - 1:
            filtered.append(data[i])
        else:
            smoothed = (data[i-1] + data[i] + data[i+1]) // 3
            filtered.append(smoothed)
    return filtered

def count_transitions(data):
    # Irrelevant helper - simulates signal jitter counting (not used in final result)
    transitions = 0
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            transitions += 1
    return transitions

def compute_entropy(data):
    # Distractor function: computes entropy but not used in final path
    freq = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def generate_pairs(data):
    # Dead code path: generates pairs but never used
    pairs = []
    for i in range(len(data) - 1):
        pairs.append((data[i], data[i+1]))
    return pairs

def detect_outliers(data, limit=20):
    # Misleading intermediate: identifies high values but only some are relevant
    outliers = []
    for x in data:
        if x > limit:
            outliers.append(x)
    return outliers

def transform_signal(data, factor=2, offset=3):
    # Core transformation: shift and scale relevant values
    return [((x + offset) ** 2) % 37 for x in data]

def analyze_pattern(seq, cutoff):
    # Critical analysis logic
    stats = defaultdict(int)
    for val in seq:
        if val > cutoff:
            stats['high'] += 1
        elif val == cutoff:
            stats['exact'] += 1
        else:
            stats['low'] += 1
    
    # Secondary filter: only values that are prime affect diagnostic
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    prime_influence = 0
    for val in seq:
        if val > cutoff and is_prime(val):
            prime_influence += 1
    
    # Tertiary dependency: cumulative sum mod affects outcome
    cumsum = 0
    cumulative_mods = []
    for val in seq:
        cumsum += val
        cumulative_mods.append(cumsum % 11)
    
    adjustment = sum(cumulative_mods) % 7
    
    # Final diagnostic combines multiple factors
    base_score = stats['high'] * 13
    bonus = prime_influence * 5
    penalty = adjustment * 2
    final_score = base_score + bonus - penalty
    
    # Dead assignment - distractor
    temp_result = {'score': final_score, 'adjustment': adjustment}
    
    return final_score

# Main execution flow
raw_data = fetch_raw_readings()
filtered_data = apply_noise_filter(raw_data)

# Irrelevant computations - red herrings
jitter_count = count_transitions(filtered_data)
entropy_value = compute_entropy(filtered_data)
data_pairs = generate_pairs(filtered_data)

# Transform data using non-linear mapping
transformed_data = transform_signal(filtered_data, factor=2, offset=3)

# Outlier detection (partially misleading)
detected_anomalies = detect_outliers(transformed_data, limit=20)

# Key threshold derived from transformed structure
dynamic_threshold = len([x for x in transformed_data if x > 10]) * 2

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, dynamic_threshold)

# Print final result as required
print(f"Result: {final_diagnostic}")