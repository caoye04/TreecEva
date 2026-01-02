import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings(base_val, count):
    readings = []
    for i in range(count):
        val = (base_val * (i + 1)) % 97
        if i % 3 == 0:
            val = (val + 12) % 97
        readings.append(val)
    return readings

def encrypt_sequence(seq):
    # Irrelevant encryption function - dead path
    encrypted = []
    key = 0xABC
    for num in seq:
        encrypted.append(num ^ key)
    return encrypted

def filter_outliers(data, limit):
    # Misleading filtering that isn't actually used later
    return [x for x in data if abs(x - 48) < limit]

def transform_signal(raw):
    processed = []
    for x in raw:
        temp = (x ** 2) // 7
        temp = temp ^ 15
        if temp > 50:
            temp = temp // 3
        processed.append(temp)
    return processed

def shift_sequence(arr, offset):
    # Unused transformation - red herring
    return arr[offset:] + arr[:offset]

def calculate_entropy(values):
    # Decoy statistical function
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 6)

def extract_features(data_str):
    # String manipulation distraction
    parts = data_str.split('-')
    codes = []    
    for p in parts:
        clean = p.strip().upper()
        if clean.startswith('X'):
            continue
        numeric = ''.join(filter(str.isdigit, clean))
        if numeric:
            codes.append(int(numeric) % 50)
    return codes

def merge_and_scale(a1, a2):
    # Complex but unused merging logic
    result = []
    for i in range(max(len(a1), len(a2))):
        val1 = a1[i % len(a1)]
        val2 = a2[i % len(a2)]
        merged = (val1 + val2) // 2
        if merged % 2 == 0:
            merged = int(math.sqrt(merged)) if merged > 1 else 0
        result.append(merged)
    return result

def analyze_pattern(seq, cutoff):
    score = 0
    for i in range(1, len(seq)):
        diff = seq[i] - seq[i-1]
        if diff > 0 and seq[i] > cutoff:
            score += diff * 2
        elif diff < 0:
            score -= diff // 2
    parity_offset = 0
    for num in seq:
        parity_offset += (num & 1) ^ 1
    return score + parity_offset

# Main execution flow
base_input = 23
sample_count = 12

# Step 1: Collect sensor readings
collected = collect_readings(base_input, sample_count)

# Step 2: Extract features from auxiliary string (distractor)
auxiliary_data = "X9Z-14A-3B-45C-22D"
feature_codes = extract_features(auxiliary_data)

# Step 3: Transform the collected signal
t_transform = transform_signal(collected)

# Step 4: Calculate entropy (irrelevant metric)
entropy_metric = calculate_entropy(t_transform)

# Step 5: Encrypt sequence (dead path)
encrypted_data = encrypt_sequence(t_transform)

# Step 6: Filter outliers (result not used)
filtered_data = filter_outliers(t_transform, 30)

# Step 7: Shift sequence (unused)
shifted_data = shift_sequence(t_transform, 3)

# Step 8: Merge arrays (completely irrelevant)
dummy_seq = [1, 2, 3]
merged_result = merge_and_scale(t_transform, dummy_seq)

# Step 9: Determine dynamic threshold
threshold = len(t_transform) // 2
if threshold < 5:
    threshold = 5

# Step 10: Analyze final pattern using transformed data
final_diagnostic = analyze_pattern(t_transform, threshold)

# Output target result
print(f"Result: {final_diagnostic}")