def analyze_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    return freq

# Irrelevant function - distractor
def compute_entropy(data):
    from math import log2
    total = sum(data.values())
    entropy = 0
    for count in data.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Another decoy: character grouping by parity of ASCII (irrelevant)
def group_chars_by_ascii_parity(s):
    even_group = []
    odd_group = []
    for c in s:
        if ord(c) % 2 == 0:
            even_group.append(c)
        else:
            odd_group.append(c)
    return {'even': even_group, 'odd': odd_group}

# Misleading transformation chain
def transform_sequence(seq):
    temp = [x * 2 for x in seq]
    temp = [x + 1 for x in temp]
    temp = [x for x in temp if x % 3 != 0]
    return temp

# Unused recursive red herring
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Dummy data processing pipeline
def preprocess_records(records):
    cleaned = []
    for record in records:
        if 'flag' in record and record['flag'] == True:
            cleaned.append({k: v * 2 for k, v in record.items() if isinstance(v, int)})
    return cleaned

# Real computation begins here — subtle signal in noise
base_weights = [0.1, 0.3, 0.4, 0.2]

# Simulate sensor metrics (some are relevant, others not)
sensor_data = [
    {'temp': 25, 'pressure': 1013, 'humidity': 45, 'o2': 20.9},
    {'temp': 26, 'pressure': 1012, 'humidity': 47, 'o2': 20.8},
    {'temp': 24, 'pressure': 1015, 'humidity': 44, 'o2': 21.0}
]

# Extract time-series-like values using enumerate (required feature)
humidity_readings = []
for i, entry in enumerate(sensor_data):
    humidity_readings.append((i, entry['humidity']))

# Use zip to pair base weights with o2 levels (misleading use)
o2_levels = [entry['o2'] for entry in sensor_data]
weight_o2_pairs = list(zip(base_weights[:len(o2_levels)], o2_levels))

# Actual relevant logic buried under distractions
def normalize(lst):
    s = sum(lst)
    return [x / s for x in lst] if s != 0 else lst

metrics = [78, 85, 90, 76]  # performance KPIs: response_time, accuracy, throughput, latency_penalty
weights = normalize([3, 4, 5, 2])  # dynamically adjusted importance

# Core calculation disguised among red herrings
def evaluate_performance(mets, wts):
    raw_scores = []
    for i, (m, w) in enumerate(zip(mets, wts)):
        contribution = m * w
        raw_scores.append(contribution)
    
    # Apply non-linear adjustment on third metric only
    if len(raw_scores) > 2:
        raw_scores[2] = raw_scores[2] * 1.1  # bonus for throughput
    
    # Final aggregation
    total = sum(raw_scores)
    
    # Decoy conditional below — never triggers due to data
    if any(x < 0 for x in mets):
        total *= 0.9  # penalty
    
    return int(round(total))

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")

# Additional noise: unused data structures
dummy_matrix = [[i*j for j in range(5)] for i in range(5)]
config_flags = {"debug": False, "trace": True, "verbose": False}

# More irrelevant computations
shifted = list(map(lambda x: x << 2, [1, 2, 3]))
checksum = sum(shifted) ^ 0xFF

# Final output
print(f"Target result: {final_score}")