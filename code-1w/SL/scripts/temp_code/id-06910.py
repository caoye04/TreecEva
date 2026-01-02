import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [
    {'temp': 78, 'voltage': 3.3, 'status': 1},
    {'temp': 85, 'voltage': 3.1, 'status': 1},
    {'temp': 90, 'voltage': 2.9, 'status': 0},
    {'temp': 100, 'voltage': 3.0, 'status': 1},
    {'temp': 110, 'voltage': 3.2, 'status': 1}
]

# Irrelevant auxiliary mapping (distractor)
component_map = {i: f'COMP_{chr(65 + i)}' for i in range(10)}

# Decoy function that is never called
def decrypt_signal(data):
    return sum(ord(c) for c in ''.join(component_map.values())) % 1000

# Red herring: historical thresholds (not used in final logic)
historical_max_temp = 105
graceful_degrade_window = [0.85, 0.90, 0.95]  # unused list

# Core processing functions
def analyze_stability(temp_seq):
    if not temp_seq:
        return 0.0
    avg = sum(temp_seq) / len(temp_seq)
    variance = sum((t - avg) ** 2 for t in temp_seq) / len(temp_seq)
    return round(math.sqrt(variance), 4) if variance > 0 else 0.0

def validate_power_integrity(voltages):
    reference = 3.3
    deviations = [abs(ref - v) for ref, v in zip([reference]*len(voltages), voltages)]
    return all(d < 0.5 for d in deviations)

# Misleading intermediate diagnostic (unused)
class DiagnosticTrace:
    def __init__(self, code, level):
        self.code = code
        self.level = level

trace_log = [DiagnosticTrace(101, 'INFO'), DiagnosticTrace(205, 'WARN')]

# Signal processing chain
filtered_data = [entry for entry in telemetry_stream if entry['status'] == 1]
temperatures = [entry['temp'] for entry in filtered_data]
voltages = [entry['voltage'] for entry in filtered_data]

# Unused transformation (dead code path)
normalized_temps = [
    (t - min(temperatures)) / (max(temperatures) - min(temperatures))
    for t in temperatures
] if temperatures else []

# Control flow with early returns and red herrings
def evaluate_health(metrics):
    temp_span = max(metrics) - min(metrics) if metrics else 0
    
    if temp_span > 30:
        return "CRITICAL"
    if temp_span > 20:
        # This block is reachable but ultimately irrelevant to final answer
        baseline = 20
        adjustment = sum([baseline * 0.1 for _ in range(3)])  # misleading calc
        return "ELEVATED"
    return "STABLE"

# Complex state tracker (partial distractor)
system_state = {
    'mode': 'ACTIVE',
    'priority': 1,
    'flags': [True, False, True],
    'checksum': sum(len(str(x)) for x in [evaluate_health(temperatures), 12345])
}

# Unused recursive helper (decoy)
def calculate_depth(node_id, depth=0):
    if depth > 3:
        return depth
    return calculate_depth(node_id + 1, depth + 1)

# Main data structure transformation
log_data = []
for idx, reading in enumerate(filtered_data):
    log_entry = {
        'index': idx,
        'raw': reading,
        'rating': 'HIGH' if reading['temp'] > 95 else 'NORMAL',
        'flagged': idx % 2 == 0  # irrelevant pattern
    }
    log_data.append(log_entry)

# Another distraction: bit manipulation with no effect
config_word = 0b1101
mask = 0b1010
decoded_flag = (config_word & mask) ^ 0b0011  # result unused

# Core algorithm disguised among noise
def process_metrics(logs, state):
    if state['mode'] != 'ACTIVE':
        return -999

    temp_list = [entry['raw']['temp'] for entry in logs]
    
    # Real computation buried in distractions
    stability_score = analyze_stability(temp_list)
    valid_power = validate_power_integrity([entry['raw']['voltage'] for entry in logs])
    
    # Key branching logic
    health_label = evaluate_health(temp_list)
    
    # Dead conditional (misleads about label importance)
    if health_label == "CRITICAL":
        initial_weight = 100
    elif health_label == "ELEVATED":
        initial_weight = 75
    else:
        initial_weight = 50  # taken branch
    
    # Actual answer derivation
    base_value = sum(temp_list) // len(temp_list)  # integer division
    adjustment_factor = int(valid_power) * 10  # 10 if True, 0 if False -> True => 10
    secondary_shift = len([e for e in logs if e['rating'] == 'HIGH']) * 2  # two entries are HIGH
    
    # Final deterministic calculation
    result = base_value + adjustment_factor + secondary_shift
    
    # Early return trap (never reached due to prior conditions)
    if decoded_flag > 100:
        return 0
        
    return result

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")