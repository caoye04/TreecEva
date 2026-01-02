import math

def preprocess_metrics(raw):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in raw if x > 0]

def compute_entropy(values):
    # Distractor: computes entropy but not used in final result
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def shift_cipher(text, key):
    # Completely irrelevant string manipulation red herring
    return ''.join(chr((ord(c) - 97 + key) % 26 + 97) if c.isalpha() else c for c in text)

def validate_sequence(seq):
    # Unused validation logic (misleading)
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def filter_outliers(data, threshold=1.5):
    # Seemingly relevant but unused filtering
    q1, q3 = np.percentile(data, [25, 75])  # Note: deliberate error - np not imported
    iqr = q3 - q1
    return [x for x in data if q1 - threshold * iqr <= x <= q3 + threshold * iqr]

def transform_features(x, y, z):
    # Intermediate transformation with decoy outputs
    temp_a = (x ^ y) & 0xFF
    temp_b = (z >> 2) + (x << 1)
    checksum = temp_a ^ temp_b ^ 0xAB
    magnitude = math.sqrt(x**2 + y**2 + z**2)
    return {'mag': magnitude, 'chk': checksum}  # Not used later

def evaluate_performance(metrics, base):
    # Core logic buried among distractions
    adjusted = [m * (1.1 if m > base else 0.9) for m in metrics]
    deviation = sum(abs(a - base) for a in adjusted)
    penalty = 0
    for val in adjusted:
        if val < base * 0.85:
            penalty += 15
        elif val > base * 1.15:
            penalty -= 10  # Bonus for exceeding high threshold
    aggregate = sum(adjusted) - penalty
    trend_factor = 0
    for i in range(1, len(adjusted)):
        if adjusted[i] >= adjusted[i-1]:
            trend_factor += 1
        else:
            trend_factor -= 2
    final_score = int(aggregate / (abs(trend_factor) + 1))
    return final_score

# Simulated dataset with meaningful and irrelevant variables
raw_input = [42, 78, 56, 91, 67, 83, 72]
baseline_reference = 65

# Unused intermediate variables (distractors)
entropy_value = compute_entropy(raw_input)
shifted_text = shift_cipher("metrics", 7)
sorted_check = validate_sequence(raw_input)

# Data transformation chain
processed_batch = []
for idx, val in enumerate(raw_input):
    processed_batch.append(val + (idx % 3))

# Key computation hidden among noise
feature_set = transform_features(12, 19, 25)  # Result ignored

metric_data = [x + 2 for x in processed_batch]  # Actual input to evaluation

# Critical statement
final_score = evaluate_performance(metric_data, baseline_reference)

# Output required format
print(f"Result: {final_score}")