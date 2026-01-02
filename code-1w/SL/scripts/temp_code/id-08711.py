import math

# Irrelevant helper function (dead code path)
def unused_calculate_entropy(values):
    return sum(-p * math.log2(p) for p in values if p > 0)

# Decoy transformation map (partially used as distraction)
transformation_map = {
    'A': lambda x: x + 10,
    'B': lambda x: x * 2,
    'C': lambda x: x - 5,
    'D': lambda x: x ** 0.5,
    'E': lambda x: x  # Identity (misleading redundancy)
}

# Real processing functions
def normalize(val, factor=1.0):
    return val / (factor + 1e-9)

def apply_shift(val, shift_config):
    if shift_config['active']:
        direction = 1 if shift_config['direction'] else -1
        magnitude = shift_config['mag']
        return val + direction * magnitude
    return val

def evaluate_threshold(val, thresholds):
    if val < thresholds['low']:
        return 'LOW'
    elif val > thresholds['high']:
        return 'HIGH'
    else:
        return 'MID'

# Complex data transformation pipeline
def process_component(x, meta):
    temp_a = x * meta.get('scale', 1)
    temp_b = temp_a + meta.get('offset', 0)
    if meta.get('invert', False):
        temp_b = -temp_b
    # Red herring: unused intermediate
    temp_c = temp_b ** 2 if temp_b > 0 else 0
    temp_d = math.log(abs(temp_b) + 1)
    return normalize(temp_d, factor=meta.get('norm_factor', 1))

# Misleading auxiliary processor (never called)
# This exists to distract from the real flow
def auxiliary_processor(items, mode='passive'):
    accumulator = 0
    for item in items:
        if mode == 'aggressive':
            accumulator += item ** 3
        else:
            accumulator -= item ** 0.1
    return accumulator / len(items) if items else 0

# Main pipeline with multiple concepts
def process_pipeline(raw_data, settings):
    # Initialization with irrelevant variables
    debug_trace = []
    stats_log = {'count': 0, 'sum': 0.0, 'flags': []}
    dummy_buffer = [0] * len(raw_data)  # Unused allocation

    result_chain = []

    # Core processing loop with nesting and logic
    for idx, entry in enumerate(raw_data):
        # Extract values with meaningful names
        measurement = entry['value']
        context = entry['ctx']

        # Apply conditional preprocessing
        if context['phase'] == 1:
            adjusted_val = measurement * 1.5
        elif context['phase'] == 2:
            adjusted_val = measurement * 0.8
        else:
            adjusted_val = measurement

        # Bit manipulation red herring (irrelevant to final result)
        binary_tag = context['tag']
        parity_check = bin(binary_tag).count('1') % 2
        if parity_check:
            adjusted_val += 0.1  # Minor perturbation (looks important)

        # Actual critical transformation
        processed = process_component(adjusted_val, settings['meta'])

        # Conditional filtering that actually matters
        threshold_state = evaluate_threshold(processed, settings['thresholds'])
        if threshold_state == 'MID':
            shift_val = apply_shift(processed, settings['shift'])
            result_chain.append(shift_val)
            stats_log['count'] += 1
            stats_log['sum'] += shift_val

        # Dead branch: never reached due to logic above
        if threshold_state == 'EXTREME':  # Impossible state
            fallback = math.atan(processed)
            result_chain.append(fallback)

        # Log for debugging (irrelevant)
        debug_trace.append({
            'idx': idx,
            'raw': measurement,
            'adj': adjusted_val,
            'proc': processed,
            'state': threshold_state
        })

    # Final aggregation with distractors
    if not result_chain:
        return -999.0

    raw_average = stats_log['sum'] / stats_log['count']
    variance_proxy = sum((x - raw_average) ** 2 for x in result_chain)
    stability_score = math.exp(-variance_proxy)  # Looks important, unused

    # Real final step: weighted combination with fixed coefficients
    weight_func = lambda w, x: w * x
    weighted_sum = sum(
        weight_func(0.3, result_chain[0]) + \
        weight_func(0.7, result_chain[-1])
    ) if len(result_chain) >= 2 else result_chain[0]

    # Final adjustment using dictionary lookup (key operation)
    final_adjustments = {'level1': 1.1, 'level2': 0.95, 'default': 1.05}
    level_key = settings.get('level', 'default')
    adjustment = final_adjustments.get(level_key, 1.05)

    final_output = weighted_sum * adjustment

    # Print required output
    print(f"Result: {final_output}")
    return final_output

# Input data setup
data = [
    {'value': 42, 'ctx': {'phase': 1, 'tag': 0b1010}},
    {'value': 38, 'ctx': {'phase': 2, 'tag': 0b1100}},
    {'value': 45, 'ctx': {'phase': 3, 'tag': 0b1111}},
    {'value': 33, 'ctx': {'phase': 1, 'tag': 0b0001}}
]

config = {
    'meta': {
        'scale': 1.2,
        'offset': -3,
        'invert': True,
        'norm_factor': 2.5
    },
    'thresholds': {
        'low': 0.15,
        'high': 0.85
    },
    'shift': {
        'active': True,
        'direction': 0,  # subtract
        'mag': 0.05
    },
    'level': 'level1'
}

# Execution point
final_output = process_pipeline(data, config)