from collections import defaultdict

# Simulate sensor feedback and calibration weights
def collect_diagnostics(raw_readings):
    diagnostics = defaultdict(int)
    temp_factor = 0
    for idx, val in enumerate(raw_readings):
        if val % 3 == 0:
            diagnostics['stable'] += 1
            temp_factor += val * 0.1
        elif val % 5 == 0:
            diagnostics['warning'] += 1
            temp_factor -= val * 0.05
        else:
            diagnostics['critical'] += 1
    # Irrelevant transformation
    adjusted_temp = sum([v**2 for v in raw_readings if v > 0]) / (len(raw_readings) or 1)
    return dict(diagnostics), temp_factor

def compute_baseline(n):
    return [i * 1.5 for i in range(n)]

def generate_weight_profile(base):
    # Uses lambda and zip
    shift_func = lambda x: x * 0.8 + 2
    paired = zip(base, [shift_func(x) for x in base])
    profile = {}
    for i, (a, b) in enumerate(paired):
        profile[i] = a + b if i % 2 == 0 else a * b
    return profile

def analyze_feedback(logs):
    feedback_map = defaultdict(float)
    for entry in logs:
        key = entry % 4
        feedback_map[key] += 0.1 * entry
        if key == 2:
            feedback_map[key] *= 0.9
    # Dead code branch - never executed due to data constraints
    if len(feedback_map) > 1000:
        feedback_map['overflow'] = -999
    return dict(feedback_map)

def aggregate_performance(feedback, weights):
    final_score = 0
    for k in range(5):
        weight = weights.get(k, 1.0)
        reading = feedback.get(k, 0.0)
        contribution = weight * reading
        if k % 2 == 0:
            final_score += contribution * 1.1
        else:
            final_score -= contribution * 0.9
    # Additional irrelevant adjustment
    penalty = sum([v for v in feedback.values() if v < 5]) * 0.01
    final_score -= penalty  # Minor effect but not central
    return int(final_score)

# Main execution flow
if __name__ == "__main__":
    raw_data = [12, 15, 18, 20, 25, 30]
    base_size = len(raw_data)

    # Step 1: Collect system diagnostics
    status, thermal_index = collect_diagnostics(raw_data)

    # Step 2: Compute baseline metrics
    baseline = compute_baseline(base_size)

    # Step 3: Generate adaptive weight profile
    base_weights = generate_weight_profile(baseline)

    # Step 4: Analyze historical feedback logs
    logs = [16, 8, 24, 4, 28, 32]
    feedback_map = analyze_feedback(logs)

    # Step 5: Aggregate final performance score
    final_score = aggregate_performance(feedback_map, base_weights)

    print(f"Result: {final_score}")