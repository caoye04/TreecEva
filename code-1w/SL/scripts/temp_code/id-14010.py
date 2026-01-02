import math

def analyze_sequence(seq):
    if len(seq) < 3:
        return 0
    peaks = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            peaks += 1
    return peaks

def shift_cipher(text, key):
    # Irrelevant cryptographic distraction
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char.lower()) - 97 + key
            result += chr((shifted % 26) + 97)
        else:
            result += char
    return result

def evaluate_stability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance) < 5.0

def transform_data(arr):
    # Distractor transformation with slicing
    temp = arr[::2] + [x * 2 for x in arr]
    filtered = [x for x in temp if x % 3 == 0]
    return sorted(filtered, reverse=True)

def calculate_entropy(values):
    # Misleading information theory function (dead code path)
    probs = [v / sum(values) for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def process_metrics(log, limit):
    # Core logic embedded in noise
    critical_values = []
    backup_modes = 0
    total_latency = 0
    
    for entry in log:
        timestamp = entry['time']
        mode_flag = entry['mode']
        payload = entry['data']
        
        # Real signal: extract sequences where mode is active
        if mode_flag and len(payload) > 4:
            sequence_peak = analyze_sequence(payload)
            if sequence_peak > 1:
                # Meaningful data extraction
                subset = payload[1:-1]  # Slicing operation (required)
                avg_mid = sum(subset) / len(subset)
                if avg_mid > limit:
                    critical_values.append(avg_mid)
        
        # Distractor: simulate backup tracking (irrelevant)
        if not evaluate_stability(payload):
            backup_modes += 1
        
        # Red herring: accumulate latency (not used in final answer)
        total_latency += max(payload) - min(payload)
    
    # Actual computation path
    if critical_values:
        transformed = transform_data(critical_values)
        # Conditional expression (required python feature)
        efficiency_score = sum(transformed) * (1.5 if len(transformed) > 2 else 1.0)
        
        # Decoy assignment
        efficiency_score = efficiency_score / 2 if evaluate_stability(critical_values) else efficiency_score
    else:
        efficiency_score = 0
    
    # Final irrelevant cipher application
    _ = shift_cipher("metrics", int(efficiency_score % 26))
    
    final_output = efficiency_score
    return final_output

# Simulated sensor data log (realistic domain context: system telemetry)
data_log = [
    {'time': 1001, 'mode': True,  'data': [12, 15, 14, 18, 13, 19, 11]},
    {'time': 1002, 'mode': False, 'data': [8,  9,  7,  10, 8,  6,  9]},
    {'time': 1003, 'mode': True,  'data': [20, 25, 30, 28, 32, 27, 35]},
    {'time': 1004, 'mode': True,  'data': [5,  7,  6,  8,  7,  9,  6]},
    {'time': 1005, 'mode': True,  'data': [40, 42, 46, 44, 48, 43, 49]},
    {'time': 1006, 'mode': False, 'data': [14, 13, 15, 12, 16, 11, 14]}
]

threshold = 10

# Execute main logic
efficiency_score = 0
final_output = process_metrics(data_log, threshold)

print(f"Result: {final_output}")