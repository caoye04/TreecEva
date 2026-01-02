def analyze_growth_patterns(data, threshold=3):
    count = 0
    temp_vals = []
    for i, val in enumerate(data):
        if val > threshold:
            count += 1
            temp_vals.append(val * 2 + i)
    return count, temp_vals


def compute_buffer_sequence(n):
    # Irrelevant helper function that computes unused sequence
    seq = [1, 1]
    for i in range(2, n + 1):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def evaluate_resilience_index(values):
    index = 0
    for v in values:
        if v % 2 == 0:
            index += v // 4
        else:
            index -= v % 5
    return index


def harvest_results(cycles):
    base = 10
    adjustment_factor = 0
    history = []
    
    for cycle in range(1, cycles + 1):
        if cycle % 2 == 0:
            adjustment_factor += cycle * 0.5
        else:
            adjustment_factor -= cycle * 0.1
        
        # Simulate intermediate logging (not used later)
        log_entry = f"Cycle-{cycle}:adj={adjustment_factor:.1f}"
        history.append(len(log_entry))
    
    # Real computation path
    result = base * (cycles - 2) + adjustment_factor
    
    # Dead code branch (never executes due to fixed input)
    if cycles < 0:
        fallback = compute_buffer_sequence(10)
        result = sum(fallback) // 10
    
    return int(result)

# Main simulation setup
sensor_readings = [1, 4, 2, 6, 8, 3, 7]
detection_level = 5

# Step 1: Filter significant growth phases
active_count, amplified = analyze_growth_patterns(sensor_readings, threshold=2)

# Step 2: Compute resilience metric (semi-relevant)
resilience_score = evaluate_resilience_index(amplified)

# Step 3: Track phase transitions using zip
phases = ['init', 'growth', 'stable', 'decline']
phase_indices = list(range(len(phases)))
transitions = []
for idx, (name, num) in enumerate(zip(phases, phase_indices)):
    transitions.append(f"{name}-{num}")

# Misleading buffer calculation (stored but not critical)
buffer_zone = compute_buffer_sequence(active_count + 2)
shadow_metric = sum(buffer_zone) / len(buffer_zone)

# Core cycle count derived from analysis
total_cycles = active_count + (resilience_score % 4)

# Key execution point
final_yield = harvest_results(total_cycles)

print(f"Result: {final_yield}")