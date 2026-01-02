from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic logic
def preprocess_stream(raw_data):
    processed = []
    for val in raw_data:
        if val < 0:
            val = abs(val) ^ 3  # Bitwise distraction
        if val % 2 == 0:
            val = val >> 1  # Right shift decoy
        processed.append(val * 1.5)
    return processed

# Irrelevant transformation chain (dead path)
def transform_legacy(data):
    accumulator = 0
    for item in data:
        accumulator += item ** 0.5
    return [accumulator / len(data)] * len(data)

# Core pattern analyzer (relevant function)
def extract_patterns(seq):
    freq = Counter(seq)
    pattern = []
    for k, v in freq.items():
        if v >= 2 and k % 3 != 0:  # Filtering condition
            pattern.append(k)
    return sorted(pattern)

# Red herring: Network simulation (unused)
def simulate_handshake(token):
    state = token & 0xFF
    for _ in range(5):
        state = (state ^ 0xB) % 17
    return state  # Never actually used

# Threshold-based classification (partially relevant)
def classify_amplitude(values):
    counts = defaultdict(int)
    for v in values:
        if v < 10:
            counts['low'] += 1
        elif v < 20:
            counts['medium'] += 1
        else:
            counts['high'] += 1
    return dict(counts)

# Decoy checksum (misleading intermediate result)
def compute_checksum(arr):
    chk = 0
    for i, n in enumerate(arr):
        chk ^= (n + i) * 3
    return chk % 1000  # Looks important, not used in final result

# Real signal analysis logic (critical path)
def evaluate_coherence(buffer, config):
    total = 0
    for i, x in enumerate(buffer):
        if i in config and config[i] > 0:
            total += x * config[i]
        elif i % 4 == 0:
            total += x // 2
    return total - len(buffer)

# Final diagnostic engine (target execution point)
def analyze_signal(signal, thresholds):
    temp_state = 0
    for idx, val in enumerate(signal):
        if val > thresholds.get(idx, 15):
            temp_state += val & 7  # Use bitwise AND
        else:
            temp_state -= val % 5
    
    # Secondary adjustment using zip
    adjustments = [1, -1, 2, -2, 3]
    for a, b in zip(signal, adjustments * (len(signal)//5 + 1)):
        temp_state += (a % 4) * b
        break  # Artificial constraint to limit effect

    return temp_state + 500

# === MAIN EXECUTION WITH DISTRACTORS ===
if __name__ == '__main__':
    # Input data (sensor readings)
    raw_sensor_data = [4, -2, 8, 5, 9, 4, 8, 12, 7, 5, 3]
    
    # Dead variables (distractors)
    session_token = 0x1A3F
    handshake_code = simulate_handshake(session_token)
    legacy_transform = transform_legacy(raw_sensor_data)
    
    # Preprocess step (relevant but indirect)
    cleaned = preprocess_stream(raw_sensor_data)
    
    # Extract key patterns (relevant)
    pattern_buffer = extract_patterns([int(x) for x in cleaned if x < 20])
    
    # Build threshold map (relevant)
    category_counts = classify_amplitude(cleaned)
    threshold_map = defaultdict(int)
    for i, count in enumerate(category_counts.values()):
        threshold_map[i] = count * 3 + 10
    
    # Misleading checksum (red herring)
    dummy_checksum = compute_checksum(pattern_buffer)
    
    # Coherence evaluation (partial relevance)
    coherence_score = evaluate_coherence(cleaned, {0: 2, 2: 1, 4: 3})
    
    # Critical assignment (target)
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")