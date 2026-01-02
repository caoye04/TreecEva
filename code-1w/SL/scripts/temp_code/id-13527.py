import itertools

# System health monitoring simulation with diagnostic metrics
def analyze_node_stability(temperatures, voltage_levels):
    stability_flags = []
    for temp, volt in zip(temperatures, voltage_levels):
        if temp > 75 and volt < 3.0:
            stability_flags.append(2)
        elif temp > 85:
            stability_flags.append(3)
        elif volt < 2.5:
            stability_flags.append(1)
        else:
            stability_flags.append(0)
    return stability_flags

# Irrelevant helper: simulates network latency (not used in final result)
def simulate_latency(ping_times):
    weighted_sum = 0
    for i, pt in enumerate(ping_times):
        weighted_sum += pt * (0.9 ** i)
    return round(weighted_sum / len(ping_times), 3)

# Core metric transformation
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * __import__('math').log(prob) if prob > 0 else 0
    return round(entropy, 6)

# Data cleansing (contains red herring)
def filter_anomalies(raw_data, limit=50):
    cleaned = [x for x in raw_data if 10 <= x <= limit]
    excess = [x for x in raw_data if x > limit]  # unused path
    if len(excess) > 3:
        pass  # dead logic branch
    return cleaned

# Main aggregation logic (key function)
def aggregate_metrics(scores, criteria):
    base_score = sum(s * c for s, c in zip(scores, criteria))
    adjustment = len([s for s in scores if s >= 4]) * 0.5
    
    # Distractor block: complex but irrelevant bitwise analysis
    bit_analysis = 0
    for s in scores:
        bit_analysis ^= (s << 2) & 0b1100 | (s >> 1)
    dummy_mask = bit_analysis & 0xFF
    
    # Real computation continues
    refined = [max(s - 1, 0) for s in scores if s % 2 == 1]
    refinement_bonus = compute_entropy(refined) if refined else 0.0
    
    # Another decoy: unused recursive depth counter
    def count_depth(arr, depth=0):
        return depth if not arr else count_depth(arr[:-1], depth + 1)
    
    unused_depth = count_depth(criteria)  # computed but not used
    
    # Final formula
    result = base_score + adjustment + refinement_bonus
    return round(result, 6)

# Simulated sensor input data
node_temps = [78, 82, 65, 90, 73]
voltages = [2.8, 3.1, 3.3, 2.9, 2.4]
ping_latencies = [12.5, 14.2, 13.1, 16.8, 11.9, 15.3]

# Generate intermediate diagnostics (some used, some not)
stability_codes = analyze_node_stability(node_temps, voltages)
normalized_loads = [round((t - 20) / 60, 2) for t in node_temps]

# Irrelevant data transformation chain
shifted_bits = list(itertools.accumulate([1, 0, 1, 1, 0], lambda x, y: (x ^ y) << 1))
rotated = [(b >> 1) | ((b & 1) << 2) for b in shifted_bits][-3:]

# Key inputs for final calculation
reliability_scores = [3, 4, 2, 5, 1]  # mapped from stability_codes indirectly
thresholds = [0.8, 1.2, 0.5, 1.0, 0.3]

# Dead code path: cryptographic hash simulation (no effect)
current_hash = 0xABCDE
for val in reliability_scores:
    current_hash = (current_hash ^ val) * 0x9E3779B1 % (2**32)

# Critical execution point
final_diagnostic = aggregate_metrics(reliability_scores, thresholds)

# Output the target result
print(f"Target result: {final_diagnostic}")