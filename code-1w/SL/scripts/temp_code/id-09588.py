def analyze_performance(values, threshold=0.5):
    count = 0
    total = 0.0
    temp_sum = 0  # distractor
    redundant_flag = False  # dead code

    for i, val in enumerate(values):
        if val > threshold:
            count += 1
            total += val
        else:
            temp_sum += val ** 2  # irrelevant computation

    avg = total / count if count > 0 else 0.0
    return avg, count


def validate_metrics(data):
    status_log = []
    for idx, item in enumerate(data):
        if item < 0:
            status_log.append((idx, 'invalid'))
        elif item >= 1:
            status_log.append((idx, 'critical'))
        else:
            status_log.append((idx, 'normal'))
    return status_log

# Simulated sensor readings
readings = [0.6, 0.4, 0.8, 0.2, 0.9]

# Secondary diagnostic data (not directly used)
diagnostics = [0.1, -0.3, 1.1, 0.5]

# Step 1: Analyze primary performance
mean_active, active_count = analyze_performance(readings)

# Misleading intermediate transformation
shadow_value = sum([x**2 for x in readings]) / len(readings)  # distraction: RMS-like calc

# Auxiliary validation (result not used in final score)
_ = validate_metrics(diagnostics)

# Construct feature metrics
metrics = {
    'mean': mean_active,
    'count': active_count,
    'length': len(readings),
    'ratio': active_count / len(readings)
}

# Convergence analysis with conditional expression
is_converged = True if metrics['ratio'] >= 0.6 else False
convergence = 1 if is_converged else -1

# Noise injection simulation (unused path)
noise_level = 0
for _ in range(10):
    noise_level += 0.01  # red herring loop

# Core rating logic
scaling_factor = 100 if convergence == 1 else 50

# Distractor: tuple unpacking with irrelevant data
details = [(1, 'A'), (2, 'B'), (3, 'C')]
indices, labels = zip(*details)  # semi-relevant, adds cognitive load

# Final calculation
base_score = metrics['mean'] * scaling_factor
penalty = 10 if metrics['count'] < 2 else 0
final_score = base_score - penalty

Result: {final_score}