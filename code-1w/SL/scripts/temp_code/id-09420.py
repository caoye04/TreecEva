import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [i * 1.5 + 2.3 for i in range(15)]
    offset = sum([x % 2.7 for x in raw])  # Irrelevant offset calculation
    return raw

def filter_noise(data, level=0.5):
    filtered = [x for x in data if x > level]
    temp_sum = 0
    for val in filtered:
        temp_sum += val * 0.1  # Red herring accumulation
    normalized = [round(x, 1) for x in filtered]
    return normalized

def shift_phase(signal, phase=1):
    shifted = []
    for i in range(len(signal)):
        shifted.append(signal[i] + math.sin(i + phase))
    return shifted

def compress_data(seq):
    # Dead function – never used in execution path
    return [seq[i] for i in range(0, len(seq), 2)]

def augment_with_metadata(data):
    metadata_tags = ['A', 'B', 'C']
    enhanced = []
    for i, val in enumerate(data):
        tag = metadata_tags[i % 3]
        enhanced.append({'value': val, 'tag': tag, 'id': i})
    return enhanced

def extract_values(record_list):
    return [r['value'] for r in record_list]

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 6)

def generate_checksum(sequence):
    # Complex but irrelevant checksum
    chk = 0
    for i, v in enumerate(sequence):
        chk ^= int(v * 10) + i
    return chk * 2  # Distractor

def transform_sequence(raw):
    # Apply multiple transformations
    step1 = filter_noise(raw)
    step2 = shift_phase(step1)
    step3 = [x * 1.1 for x in step2]  # Amplify signal
    padding = [0.1] * 5
    extended = step3 + padding  # Add dummy data
    trimmed = extended[:len(step3)]  # Remove padding (confusing but neutral)
    return trimmed

def detect_anomalies(series, limit=5.0):
    anomalies = []
    for x in series:
        if abs(x - limit) < 0.8:
            anomalies.append(x)
    return anomalies if len(anomalies) > 2 else [0.0]  # Misleading fallback

def analyze_pattern(dataset, cutoff):
    # Core logic hidden among distractions
    base_sum = sum(dataset)
    count_above = len([x for x in dataset if x > cutoff])
    adjustment = math.sqrt(count_above) if count_above > 0 else 0
    score = base_sum * adjustment
    
    # Irrelevant branching
    if score < 100:
        flag = 'LOW'
    elif score < 200:
        flag = 'MEDIUM'
    else:
        flag = 'HIGH'
    
    # Decoy entropy use
    entropy_proxy = compute_entropy([abs(x) for x in dataset[:5]])
    final_score = int(score - (entropy_proxy * 10))  # Final deterministic result
    return final_score

# Main execution chain
sensor_data = collect_readings()
processed_data = transform_sequence(sensor_data)
structured_data = augment_with_metadata(processed_data)
pure_values = extract_values(structured_data)
anomaly_check = detect_anomalies(pure_values)
checksum = generate_checksum(pure_values)  # Unused but computed
threshold = 6.5
final_diagnostic = analyze_pattern(pure_values, threshold)
print(f"Target result: {final_diagnostic}")