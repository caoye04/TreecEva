from collections import defaultdict, Counter

# Simulated sensor array processing with diagnostic flags
def preprocess_readings(raw_data):
    processed = []
    for val in raw_data:
        if val < 0:
            processed.append(abs(val) % 7)
        elif val == 0:
            processed.append(3)
        else:
            processed.append((val * 2) % 9)
    return processed

def generate_bitmask(length, seed=5):
    # Irrelevant bitmask generator (not used in final logic)
    mask = 1
    sequence = []
    for i in range(length):
        mask = (mask * 17 + seed) % 67
        sequence.append(mask % 2)
    return sequence

def evaluate_thresholds(data, limit):
    counts = defaultdict(int)
    for x in data:
        counts[x] += 1
    above_limit = [k for k, v in counts.items() if v > limit]
    return sorted(above_limit)

def compute_entropy(values):
    # Dead-end function: calculated but never used
    freq = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just decoy
    return round(entropy, 6)

def extract_signatures(arr):
    sig = []
    for i in range(len(arr) - 1):
        sig.append((arr[i] + arr[i+1]) % 5)
    return sig[:4]

def build_graph_structure(nodes):
    graph = defaultdict(list)
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if (nodes[i] + nodes[j]) % 3 == 0:
                graph[nodes[i]].append(nodes[j])
    return graph

def filter_anomalies(dataset):
    temp_result = []
    for item in dataset:
        if item in [0, 2, 4]:
            temp_result.append(item * 3)
        else:
            temp_result.append(item)
    # This function appears important but is only partially influential
    return [x for x in temp_result if x % 2 == 1]

def integrate_signals(primary, secondary):
    merged = []
    for a, b in zip(primary, secondary):
        merged.append((a ^ b) + 1)  # XOR and increment
    return merged

def analyze_pattern(core_sequence, masks):
    # Core logic step 1: initialize diagnostics
    diagnostic_map = defaultdict(int)
    for i, val in enumerate(core_sequence):
        diagnostic_map[i] = val * (i + 1)
    
    # Core logic step 2: cumulative sum with offset
    base_score = sum(diagnostic_map.values())
    adjustment = 0
    for k, v in diagnostic_map.items():
        if v % 2 == 0:
            adjustment += k
    
    # Core logic step 3: apply transformation chain
    intermediate = (base_score + adjustment) // 2
    if intermediate % 3 == 0:
        intermediate = (intermediate * 5) // 4
    else:
        intermediate = (intermediate * 2) + 1
    
    # Core logic step 4: final mapping using modular reduction
    final_value = 0
    for idx in range(1, len(core_sequence) + 1):
        final_value += (intermediate // idx) % 7
    
    return final_value

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = [12, -3, 0, 8, 15, -7, 4, 21, 6]
    
    # Step 1: Preprocess sensor inputs
    cleaned = preprocess_readings(raw_sensor_data)
    
    # Distractor: unused entropy calculation
    _ = compute_entropy(cleaned)
    
    # Step 2: Extract key pattern features
    features = extract_signatures(cleaned)
    
    # Distractor: irrelevant graph structure
    _ = build_graph_structure(features)
    
    # Step 3: Filter and refine signal components
    refined_features = filter_anomalies(features)
    
    # Distractor: generate unused bitmask
    dummy_mask = generate_bitmask(10)
    
    # Step 4: Integrate dual signal paths (only one path used)
    logic_core = integrate_signals(refined_features, [1, 1, 1][:len(refined_features)])
    
    # Distractor: evaluate thresholds (result not used)
    _ = evaluate_thresholds(logic_core, 1)
    
    # Distractor: another unused bitmask
    bitmask_sequence = [0, 1, 0, 1, 1, 0]  # Hardcoded but looks dynamic
    
    # Key execution point
    final_diagnostic = analyze_pattern(logic_core, bitmask_sequence)
    
    print(f"Result: {final_diagnostic}")