import itertools

def collect_sensor_data():
    # Simulate raw sensor readings (distractor: some are irrelevant)
    raw_readings = [127, 255, 0, 64, 192, 32, 96, 160]
    mask = 0b11000000
    filtered = [r & mask for r in raw_readings if r > 30]
    return filtered

def transform_signal(data):
    # Apply transformation with decoy logic
    shifted = [(x >> 2) ^ 15 for x in data]
    checksum = sum(shifted) % 256
    normalized = [x / 16.0 for x in shifted]
    # Dead path: checksum used only here
    if checksum > 100:
        normalized.append(0.0)  # never reached due to fixed input
    return normalized

def evaluate_stability(metrics):
    # Real logic hidden among distractions
    baseline = 3.5
    fluctuations = [abs(m - baseline) for m in metrics]
    high_deviation = [f for f in fluctuations if f > 1.0]
    score = len(high_deviation) * 0.5
    penalty = 0
    for i, f in enumerate(fluctuations):
        if i % 3 == 0 and f < 0.5:
            penalty += 0.1  # misleading adjustment
    return score - penalty

def generate_report(snippets):
    # Irrelevant text processing (string methods as required)
    titles = ['STATUS_A', 'DEBUG_X', 'LOG_9', 'EVENT_M']
    labeled = [f'{t}: {s:.2f}' for t, s in zip(titles, snippets)]
    joined = '; '.join(labeled).upper().replace('_', '-')
    parts = joined.split('; ')
    codes = [p.split(': ')[0] for p in parts]
    # This function returns nothing useful
    return len(codes)  # red herring return

def analyze_readings(data, limit):
    processed = []
    for val in data:
        temp = val
        if temp > limit:
            temp = temp // 2
            if temp % 2 == 0:
                temp = temp + 7
            else:
                temp = temp * 3 + 1  # hailstone-like step (real logic)
        processed.append(temp)
    
    # Core computation
    total = sum(processed)
    count = len([p for p in processed if p > 50])
    entropy_proxy = 0
    for p in processed:
        if p > 0:
            entropy_proxy += p * (p.bit_length() if p > 1 else 1)
    
    # Final diagnostic combines multiple factors
    aggregate = total + count * 10 - (entropy_proxy // 100)
    return aggregate

# Main execution with distractors
raw_data = collect_sensor_data()
processed_signal = transform_signal(raw_data)
eval_score = evaluate_stability(processed_signal)

# Unused debugging branch (dead code path)
if len(raw_data) > 10:
    debug_log = '\n'.join([bin(x) for x in raw_data])
    with open('/dev/null', 'w') as f:
        f.write(debug_log)

# Generate spurious report (irrelevant)
dummy_report_size = generate_report(processed_signal)

threshold = 45
final_diagnostic = analyze_readings(processed_signal, threshold)

# Critical print statement
print(f"Result: {final_diagnostic}")