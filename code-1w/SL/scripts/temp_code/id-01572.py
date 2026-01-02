from itertools import cycle, islice

def analyze_trend(data, threshold):
    trend = []
    for i in range(1, len(data)):
        trend.append(data[i] - data[i-1])
    return [x for x in trend if abs(x) > threshold]

# Irrelevant helper function (decoy)
def compute_entropy(values):
    total = 0
    for v in values:
        if v != 0:
            total -= v * v  # Not actual entropy, just misleading
    return total

# Another decoy: Unused transformation
def transform_sequence(seq):
    return [x ** 2 + 2 * x + 1 for x in seq if x % 2 == 0]

# Simulated system metrics over time
metrics = [88, 92, 90, 95, 87, 93, 96, 89, 91, 94]
baseline = 90

# Distractor variables
offset = sum([i for i in range(5)])  # 10, irrelevant
checksum = 0
for val in metrics:
    checksum += val % 7

# Misleading intermediate calculation
effective_yield = 0
for i, m in enumerate(metrics):
    if m > baseline:
        effective_yield += (m - baseline) * (0.5 ** i)  # decays fast

# Dead code path (never executed)
if False:
    shadow_buffer = [0] * len(metrics)
    for idx in range(len(metrics)):
        shadow_buffer[idx] = metrics[idx] // 3

# Real logic buried in noise
def adjust_for_variance(seq, ref):
    adjusted = []
    variance_sum = 0
    for x in seq:
        variance_sum += (x - ref) ** 2
    std_dev = (variance_sum / len(seq)) ** 0.5 if len(seq) > 0 else 0
    for x in seq:
        adjusted.append((x - ref) / (std_dev + 1))  # Normalize by pseudo-stddev
    return adjusted

# Secondary distraction: circular padding
circular_pad = list(islice(cycle([1, -1]), len(metrics)))
padded_metrics = [m + c for m, c in zip(metrics, circular_pad)]

# Another red herring: frequency count of deltas
deltas = [abs(metrics[i+1] - metrics[i]) for i in range(len(metrics)-1)]
frequency_map = {}
for d in deltas:
    frequency_map[d] = frequency_map.get(d, 0) + 1

# Core processing function (key logic)
def process_performance(raw_data, target):
    # Step 1: Normalize data around baseline
    normalized = [x - target for x in raw_data]
    
    # Step 2: Count how many exceeded baseline
    exceed_count = sum(1 for x in raw_data if x > target)
    
    # Step 3: Apply non-linear gain on positive deviations
    gains = [max(0, x - target) ** 1.5 for x in raw_data]
    
    # Step 4: Apply decay-weighted sum
    weighted_sum = 0
    decay_factor = 0.85
    for i, g in enumerate(gains):
        weighted_sum += g * (decay_factor ** i)
    
    # Step 5: Adjust based on consistency bonus
    consistency_bonus = 1.0
    if all(x >= target - 5 for x in raw_data):  # All within 5 points of baseline
        consistency_bonus = 1.2
    
    # Step 6: Apply adjustment using variance correction
    adjusted_normalized = adjust_for_variance(raw_data, target)
    spread_penalty = sum(abs(x) for x in adjusted_normalized) / len(adjusted_normalized)
    
    # Step 7: Final score computation
    base_score = weighted_sum * consistency_bonus
    final_penalized = base_score - (spread_penalty * 10)
    
    # Return deterministic scalar
    return int(round(final_penalized))

# Key statement
final_score = process_performance(metrics, baseline)

# Output result as required
print(f"Result: {final_score}")