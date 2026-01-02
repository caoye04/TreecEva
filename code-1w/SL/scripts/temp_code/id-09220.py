import math

# Simulated sensor data processing with noise filtering and state analysis
def collect_sensor_data(raw_readings):
    filtered = []
    for val in raw_readings:
        if abs(val - 50) < 20:  # arbitrary noise filter
            filtered.append(val * 0.95)
        elif val > 70:
            filtered.append(60)
    return filtered[:15]  # cap at 15 entries

# Irrelevant helper: calculates statistical dispersion (not used in final result)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Misleading transformation chain
def apply_calibration(signal):
    calibrated = [math.sin(x / 10) * 100 for x in signal]
    normalized = [abs(c) % 75 for c in calibrated]
    return normalized[::2]  # slicing: every other element

# Dead function: looks important but unused in critical path
def detect_anomaly(pattern):
    score = 0
    for i in range(len(pattern)):
        if pattern[i] > 50 and i % 3 == 0:
            score += 3
        elif pattern[i] < 30:
            score -= 1
    return score > 5

# Core logic obscured by surrounding distractions
def evaluate_stability(sequence):
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Complex conditional branching
    pos_runs = neg_runs = 0
    current_run = 0
    for t in trend:
        if t == 1:
            if current_run < 0:
                neg_runs += 1
            current_run = max(0, current_run + 1)
        elif t == -1:
            if current_run > 0:
                pos_runs += 1
            current_run = min(0, current_run - 1)
    
    # Distractor: computes but doesn't affect final answer
    oscillations = pos_runs + neg_runs
    dampening_factor = 0.87
    for _ in range(oscillations // 3):
        dampening_factor *= 0.9
    
    return pos_runs - neg_runs

# Key function containing the actual computation path
def analyze_system(log_entries, limit):
    # log_entries goes through multiple transformations
    processed = []
    for entry in log_entries:
        if entry < limit:
            processed.append(entry ** 0.5 * 2)
        else:
            processed.append(entry / 4)
    
    # Slicing operation used meaningfully
    segment_a = processed[1:6]
    segment_b = processed[-5:]
    
    # Conditional logic based on length and sum
    if len(segment_a) == 5 and sum(segment_b) > 50:
        adjustment = sum(segment_a) / len(segment_a)
    else:
        adjustment = math.log(abs(sum(processed)) + 1)
    
    # Final decision with bit manipulation red herring
    temp_flag = 0
    for val in segment_b:
        temp_flag ^= int(val) & 7  # bitwise decoy
    
    # Actual equilibrium calculation
    base = sum(processed) / len(processed)
    modifier = math.cos(math.pi * adjustment / 30)
    equilibrium_value = int(base + modifier * 10)
    
    # Critical distraction: multiple similar variables
    equilibria_list = [equilibrium_value, equilibrium_value + 5, equilibrium_value - 3]
    equilibrium_index = 0
    
    return equilibria_list[equilibrium_index]

# Irrelevant data structure setup
system_states = {
    'initial': [45, 52, 48, 55, 51],
    'critical': [70, 72, 68],
    'recovery': [40, 38, 44]
}

# Unused algorithm: matrix-like traversal
def traverse_grid(data_2d):
    total = 0
    for row in range(len(data_2d)):
        for col in range(len(data_2d[row])):
            if row == col:
                total += data_2d[row][col] * 2
            elif row < col:
                total += data_2d[row][col]
    return total

# Main execution flow with decoy calls
if __name__ == '__main__':
    raw_input = [52, 48, 56, 75, 44, 60, 53, 49, 58, 71, 47, 50, 54, 68, 46, 59, 51]
    
    # Distractor: collection and unused variance check
    clean_data = collect_sensor_data(raw_input)
    variance = calculate_variance(clean_data)
    
    # Another red herring transformation
    calibrated_signal = apply_calibration(clean_data)
    
    # Looks important but not part of final calculation
    stability_metric = evaluate_stability(calibrated_signal)
    
    # Real data path begins here, but hidden among distractions
    raw_sequence = [52, 48, 56, 44, 60, 53, 49, 58, 47, 50, 54, 46, 59, 51, 61]
    threshold = 55
    
    # This is the key statement
    equilibrium = analyze_system(raw_sequence, threshold)
    
    # Print final result as required
    print(f"Target result: {equilibrium}")