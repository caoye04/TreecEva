from collections import defaultdict, Counter

# Simulated industrial sensor data processing with red herrings
def analyze_turbine_data(raw_readings):
    normalized = [x * 0.87 for x in raw_readings if x > 0]
    stats = defaultdict(float)
    outliers = []
    temp_log = []

    for val in normalized:
        if val > 95:
            outliers.append(val)
        elif val < 10:
            continue
        else:
            stats['valid_count'] += 1
            stats['cumulative'] += val

    # Irrelevant transformation chain (dead abstraction path)
    def transform_sequence(seq):
        return [seq[i] + seq[i-1] for i in range(1, len(seq), 2)]

    if len(outliers) > 5:
        adjusted = [x * 0.92 for x in normalized]
    else:
        adjusted = normalized[:]

    # Decoy statistical calculation (not used later)
    mean_val = sum(adjusted) / len(adjusted) if adjusted else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0

    # Real logic begins here — hidden among distractions
    flow_codes = [int(x // 10) * 3 for x in adjusted]
    code_freq = Counter(flow_codes)

    # Misleading filter that looks important but isn't connected
    rare_codes = [k for k, v in code_freq.items() if v < 2]
    filtered_codes = [c for c in flow_codes if c not in rare_codes]

    # Core computation buried in noise
    aggregate_score = 0
    for i, code in enumerate(filtered_codes):
        if i % 3 == 0:
            aggregate_score += code * 1.1
        elif i % 4 == 0:
            aggregate_score -= code * 0.25
        else:
            aggregate_score += code * 0.7

    # Distractor: unused complex structure
    diagnostics = {
        'levels': [[i, adjusted[i]] for i in range(0, len(adjusted), 4)],
        'flags': set([hash(str(x)[:4]) for x in adjusted]),
        'checksum': sum(hash(str(x)) % 1000 for x in adjusted)
    }

    return aggregate_score

# Fake preprocessing function (looks active, never called)
def calibrate_input(data_stream):
    base_offset = 2.1
    calibrated = [x - base_offset for x in data_stream]
    return [max(0, x) for x in calibrated]

# Secondary decoy: elaborate but unused data structure
historical_cache = {
    'snapshots': [
        {'epoch': t, 'value': (t * 1.7) % 43} for t in range(12, 48, 3)
    ],
    'meta': {
        'version': '2.1-alpha',
        'nodes': ['A7', 'B9', 'C3'],
        'weights': [0.1, 0.3, 0.6]
    }
}

# Another irrelevant utility
def rolling_average(arr, w=3):
    if len(arr) < w:
        return []
    return [sum(arr[i:i+w]) / w for i in range(len(arr) - w + 1)]

# Real function contributing to answer, but obscured
def calculate_efficiency(metrics, config_map):
    base = metrics * config_map['scale']
    penalty = 0

    # Conditional penalties with red herring conditions
    if metrics > 150:
        penalty += config_map['grace_period'] * 1.5
    elif metrics < 50:
        penalty += config_map['overhead'] * 0.8

    # Actual critical operation
    phase_adjust = (base ** 0.5) * config_map['phase_boost']

    # Fake fallback that never triggers due to data
    if phase_adjust < 0:
        phase_adjust = abs(phase_adjust) * 1.2

    return phase_adjust - penalty

# Global constants that seem important but only some are used
DEFAULT_THRESHOLD = 88.5
MAX_ITERATIONS = 17
SCALE_FACTOR = 2.3
PHASE_BOOST = 1.9

# Unused mapping (distractor)
type_registry = defaultdict(list)
for item in ['X1', 'Y2', 'Z3']:
    type_registry[item[0]].append(f"model-{item.lower()}")

# Key data initialization
sensor_input = [12, 67, 91, 45, 103, -5, 88, 76, 110, 95, 44, 68, 77]

# Execution chain with misleading calls
intermediate_result = analyze_turbine_data(sensor_input)

# Dead assignment — looks like it does something
buffer_slice = sensor_input[2:9:2]
offset_patch = [x + 1.5 for x in buffer_slice if x > 50]

# Critical configuration map (only this matters now)
threshold_map = {
    'scale': SCALE_FACTOR,
    'phase_boost': PHASE_BOOST,
    'grace_period': 11,
    'overhead': 7.2
}

# Final relevant statement buried in noise
flow_metrics = intermediate_result

# This is the key statement — target of the question
thermal_quotient = calculate_efficiency(flow_metrics, threshold_map)

# Print final result as required
print(f"Result: {thermal_quotient}")