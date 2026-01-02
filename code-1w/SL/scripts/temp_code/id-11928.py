def analyze_system_performance(readings):
    total = 0
    peak_count = 0
    baseline = readings[0] if readings else 0
    temp_offset = 0

    for i, val in enumerate(readings):
        if val > baseline * 1.5:
            peak_count += 1
            temp_offset += (val - baseline) * 0.1

    adjusted_peaks = peak_count - int(temp_offset)
    return max(adjusted_peaks, 0)


def normalize_data(stream):
    if not stream:
        return [0]
    
    mean_val = sum(stream) / len(stream)
    deviation = sum((x - mean_val) ** 2 for x in stream)
    normalized = [(x - mean_val) / (deviation + 1e-8) for x in stream]
    
    # Distractor: unused transformation
    squared_norm = [n**2 for n in normalized]
    inverted = [-n for n in normalized]
    
    return normalized

readings_input = [12, 15, 14, 20, 25, 13, 18, 22]

# Irrelevant data processing branch
if len(readings_input) > 5:
    filtered_data = [x for x in readings_input if x > 14]
    processed_meta = sum(x * (i+1) for i, x in enumerate(filtered_data)) // len(filtered_data)

convergence = 0
stability = 0

for idx, (a, b) in enumerate(zip(readings_input, readings_input[1:])):
    diff = abs(b - a)
    if diff < 5:
        convergence += 1
    else:
        stability -= 1

    # Semi-relevant: affects control flow but not final answer directly
    if idx % 2 == 0 and diff > 3:
        convergence += 0.5  # fractional adjustment

# Unused helper computation - red herring
aggregate_trend = sum(1 for x, y in zip(readings_input, readings_input[1:]) if y > x)

# Simulate auxiliary state tracking
state_log = []
for step in range(3):
    state_log.append(f"Step {step}: active")

# Distractor variables
placeholder_sum = sum([convergence, stability, len(readings_input)])
dummy_weight = 0.95

# Core logic embedded within noise
normalized_readings = normalize_data(readings_input)
peak_analysis = analyze_system_performance(readings_input)

scaling_factor = 2.5 if peak_analysis > 2 else 1.8

intermediate_rating = (convergence * 10) + (abs(stability) * 3)

# Key function containing conditional expression
def calculate_rating(conv, stab):
    base = conv * 8.5
    penalty = 15 if stab < -3 else 5
    bonus = 20 if conv > 5 else 0
    
    # Conditional expression used idiomatically
    adjustment = 1.2 if any(r > 2.0 for r in normalized_readings[:4]) else 0.8
    
    # Distractor: complex-looking but unused calculation
    shadow_score = (base - penalty) * adjustment * 0.7 + bonus
    
    return int(base + bonus - penalty)  # Final deterministic integer

final_score = calculate_rating(convergence, stability)

print(f"Result: {final_score}")