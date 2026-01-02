from collections import defaultdict, Counter
import math

# Simulated sensor array diagnostics with red herrings
def analyze_sensor_noise(sensor_data, threshold=0.75):
    noise_pattern = []
    cumulative_drift = 0.0
    for i, reading in enumerate(sensor_data):
        if i % 4 == 0:
            adjusted = reading * 1.05
        elif i % 3 == 0:
            adjusted = reading * 0.92
        else:
            adjusted = reading
        noise_level = abs(adjusted - reading)
        if noise_level > threshold * 0.1:
            noise_pattern.append(i)
        cumulative_drift += abs(adjusted - reading)
    return len(noise_pattern) > 5, cumulative_drift

# Irrelevant image processing decoy
def process_pixel_grid(grid):
    height, width = len(grid), len(grid[0])
    edge_map = [[0]*width for _ in range(height)]
    for i in range(1, height-1):
        for j in range(1, width-1):
            gx = grid[i][j+1] - grid[i][j-1]
            gy = grid[i+1][j] - grid[i-1][j]
            edge_map[i][j] = math.sqrt(gx*gx + gy*gy)
    total_energy = sum(sum(row) for row in edge_map)
    return total_energy  # Dead end

# Core sequence validator with distractors
def validate_sequence_integrity(seq):
    seen = set()
    transitions = defaultdict(int)
    parity_count = {True: 0, False: 0}
    
    for i in range(len(seq) - 1):
        current, next_val = seq[i], seq[i+1]
        seen.add(current)
        transitions[(current % 3, next_val % 3)] += 1
        
        # Distractor computation
        if current > next_val:
            parity_count[True] += 1
        else:
            parity_count[False] += 1
            
        # Unused intermediate
        _ = math.atan2(current, next_val + 1e-8)
    
    # Critical path: transition signature
    signature = 0
    for (a, b), count in transitions.items():
        signature += (a * 3 + b) * count
    
    return signature, len(seen)

# Main diagnostic workflow
def generate_consistency_log(raw_readings):
    log = []
    temp_buffer = []
    
    for val in raw_readings:
        if val < 0:
            continue
        transformed = int((val ** 0.5) * 3.7) % 100
        temp_buffer.append(transformed)
        
        if len(temp_buffer) >= 3:
            avg = sum(temp_buffer[-3:]) / 3
            if avg > 40:
                log.append(transformed + 1)
            else:
                log.append(transformed - 1)
    
    # Dead code path - never accessed due to logic above
    if len(temp_buffer) == 0:
        fallback = [x*2 for x in raw_readings if x % 2 == 0]
        log.extend(fallback)
        
    return log

# Primary integrity computation
def compute_integrity_score(log):
    # Real computation
    freq = Counter(log)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    mode_value = min(modes) if modes else 0
    
    # Complex distractor chain
    squared_chain = [x*x for x in log if x % 2 == 1]
    filtered_chain = [s for s in squared_chain if s < 500]
    aggregate = sum(filtered_chain) // len(filtered_chain) if filtered_chain else 0
    
    # Secondary metric (unused)
    running_total = 0
    for i, x in enumerate(log):
        running_total += x * math.sin(i * 0.5)
    
    # Tertiary path with bit manipulation decoy
    bit_accum = 0
    for x in log[:10]:
        bit_accum ^= (x << 1) | (x >> 2)
    
    # ACTUAL answer derivation - subtle and non-obvious
    valid_entries = [x for x in log if x in freq and freq[x] >= 2]
    unique_valid = list(set(valid_entries))
    sorted_valid = sorted(unique_valid, reverse=True)
    
    if len(sorted_valid) >= 3:
        candidate = sorted_valid[2]  # Third largest repeated value
    else:
        candidate = mode_value
    
    # Final transformation
    final_score = (candidate * 17) % 97
    return final_score

# Orchestration function with misleading structure
def system_diagnostic_protocol(input_sequence):
    # Step 1: Noise analysis (partially relevant)
    has_issue, drift = analyze_sensor_noise(input_sequence)
    
    # Step 2: Generate log (critical)
    consistency_log = generate_consistency_log(input_sequence)
    
    # Step 3: Validate sequence (distractor)
    sig, unique_count = validate_sequence_integrity(input_sequence)
    
    # Step 4: Compute score (critical)
    final_diagnostic = compute_integrity_score(consistency_log)
    
    # Step 5: Process grid (completely irrelevant)
    dummy_grid = [[i+j for j in range(8)] for i in range(8)]
    _ = process_pixel_grid(dummy_grid)
    
    # Output target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point
if __name__ == "__main__":
    sensor_input = [16, 25, 9, 64, 49, 36, 81, 100, 25, 16, 4, 9, 64, 81, 49]
    result = system_diagnostic_protocol(sensor_input)