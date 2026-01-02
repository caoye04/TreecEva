import math

# Simulated system telemetry and diagnostic processing
# Heavily instrumented with red herrings and irrelevant computations

def collect_timings(base_freq: float) -> list:
    raw_intervals = [base_freq * (1.1 ** i) for i in range(15)]
    filtered = [t for t in raw_intervals if t > 2.0]
    padded = [0.0] * 3 + filtered + [999.9]  # Irrelevant padding
    return padded  # Only first 12 elements matter later

def evaluate_health(sensor_array: list) -> dict:
    stats = {
        'peak': max(sensor_array),
        'baseline': sum(sensor_array) / len(sensor_array),
        'noise_floor': 0.0,
        'harmonic_stress': 0,
        'diagnostic_flag': False
    }
    stress_level = 0
    for val in sensor_array:
        if val > 5.0:
            stress_level += int(math.log(val, 2))
    stats['harmonic_stress'] = stress_level
    stats['diagnostic_flag'] = stress_level > 10
    return stats

def transform_coordinates(x: tuple, y: tuple) -> dict:
    # Completely irrelevant geometric transformation
    x_rev = x[::-1]
    y_rev = y[::-1]
    vector_map = {}
    for i in range(len(x_rev)):
        vector_map[f'vec_{i}'] = (x_rev[i] * 0.5, y_rev[i] * 1.5)
    return vector_map  # Dead code path

def calculate_entropy(stream: list) -> float:
    # Misleading information-theoretic computation
    freq_map = {}
    for item in stream:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(stream)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log(p) if p > 0 else 0
    return round(entropy, 6)

def normalize_readings(data: list) -> list:
    # Unused normalization function (decoy)
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val)**2 for x in data) / len(data))**0.5
    return [(x - mean_val) / stdev for x in data]

def generate_sequence(n: int) -> list:
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def aggregate_metrics(log: list, state: dict) -> int:
    # Core logic hidden among distractions
    segment = log[3:15]  # Critical slice
    offset = len(segment) // 2
    mid_val = segment[offset]
    
    # Real computation begins here
    temp_key = int(mid_val * 7)  # 7 is magic factor
    lookup_table = {i: (i * i) % 13 for i in range(20)}
    mapped_score = lookup_table.get(temp_key % 20, 0)
    
    # Conditional branching based on state flags
    modifier = 1
    if state['active_nodes'] > 5 and state['sync_mode']:
        modifier = -1
    elif state['latency'] < 100:
        modifier = 2
    
    # Final calculation
    result = (mapped_score * 100) + (state['active_nodes'] * 10) + modifier
    return result

# --- Main Execution with Heavy Interference ---

# Irrelevant coordinate setup
coords_x = (10, 20, 30, 40)
coords_y = (5, 15, 25, 35)
geo_data = transform_coordinates(coords_x, coords_y)  # Unused

# Generate timing data (relevant)
timing_log = collect_timings(1.5)

# Simulate system health check (partially relevant)
sensor_input = [1.2, 3.4, 5.6, 7.8, 9.1, 4.3, 2.2]
health_report = evaluate_health(sensor_input)

# Misleading entropy calculation on timing log
entropy_score = calculate_entropy([int(x) for x in timing_log if x < 10])

# Useless sequence generation
fibonacci_snippet = generate_sequence(10)  # Dead end

# System state definition — critical for final result
system_state = {
    'active_nodes': 8,
    'sync_mode': False,
    'latency': 87,
    'overclock': True,
    'power_status': 'optimal',
    'last_reset': '2023-12-01'
}

# Normalization (unused path)
normalized_timings = normalize_readings(timing_log)

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_state)

print(f"Result: {final_diagnostic}")