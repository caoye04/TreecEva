def analyze_readings(raw_data, threshold=0.85):
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = [x for x in normalized if x > threshold]
    return len(filtered) > 0

# Simulated sensor array outputs
temperature_stream = [23.4, 25.1, 26.8, 24.9, 27.3, 28.0, 26.5, 25.7]
humidity_stream = [45, 48, 52, 58, 61, 55, 50, 47]
pressure_stream = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant transformation chain (distractor)
def transform_sequence(seq):
    a = [x ** 0.5 for x in seq if x % 2 == 0]
    b = [y * 1.5 for y in a]
    c = sum(b) / len(b) if b else 0
    return [round(z - c, 2) for z in b]

baseline_adjustment = transform_sequence(pressure_stream)

# Signal convergence analysis
converged_signals = []
system_bias = 0.0

for i, (t, h, p) in enumerate(zip(temperature_stream, humidity_stream, pressure_stream)):
    temp_normalized = t / 30.0
    humid_ratio = h / 100.0
    press_deviation = abs(p - 1012) / 1012
    
    # Compute composite index
    index_score = (temp_normalized * 0.4) + (humid_ratio * 0.3) - (press_deviation * 0.3)
    
    # Dead code path (misleading)
    if index_score > 1.0:
        adjustment_factor = 0.9
        index_score *= adjustment_factor  # Never actually affects logic
    
    # Evaluate signal stability
    stable_temp = abs(t - temperature_stream[i-1]) < 2.0 if i > 0 else True
    humidity_trend = "rising" if (i > 0 and h > humidity_stream[i-1]) else "falling"
    
    # Decoy accumulation (irrelevant)
    cumulative_drift = 0.0
    for j in range(i+1):
        cumulative_drift += abs(pressure_stream[j] - 1012)
    
    if index_score > 0.75 and stable_temp:
        converged_signals.append(index_score)
        
        # Red herring: complex but unused calculation
        shadow_weight = (i + 1) * (index_score ** 2)
        temporal_decay = 1 / (1 + i*0.1)
        effective_weight = shadow_weight * temporal_decay
        
# Unused diagnostic functions (dead code)
def compute_entropy(data):
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log(count/total) for count in freq.values())
    return entropy

def validate_coherence(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

# Real computation buried among distractions
bias_accumulator = 0.0
for idx, val in enumerate(converged_signals):
    bias_accumulator += val * (0.9 ** idx)

system_bias = round(bias_accumulator / len(converged_signals), 6) if converged_signals else 0.0

# Secondary irrelevant structure
event_log = []
for i, reading in enumerate(temperature_stream):
    status_flag = 'HIGH' if reading > 26 else 'NORMAL'
    event_log.append(f"T{i}:{status_flag}")

# Key operation embedded in noise
intermediate_fusion = []
for s in converged_signals:
    transformed = s ** 2 + 0.1 * s
    intermediate_fusion.append(transformed)

fusion_total = sum(intermediate_fusion)
scaling_constant = 1.75

# Final metric aggregation (target)
def aggregate_metrics(signals, bias):
    base = sum(x**1.5 for x in signals)
    penalty = len(signals) * bias * 0.2
    return int((base - penalty) * 1000)  # Discretized diagnostic code

final_diagnostic = aggregate_metrics(converged_signals, system_bias)
print(f"Target result: {final_diagnostic}")