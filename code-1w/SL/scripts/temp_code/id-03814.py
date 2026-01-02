def analyze_component_health(reading, threshold=75, mode='aggressive'):
    if mode == 'aggressive':
        return reading > threshold and (reading % 10) != 0
    elif mode == 'conservative':
        return reading >= threshold
    return False


def generate_diagnostics(code_map):
    diagnostics = {}
    for key, val in code_map.items():
        if isinstance(val, str):
            diagnostics[key] = len(val) % 7
        else:
            diagnostics[key] = val % 7
    return diagnostics

def transform_sequence(seq):
    # Irrelevant transformation path
    return [x ** 2 % 13 for x in seq if x % 3 != 0]

def compute_stability_index(configs):
    # Dead function - never used
    total = 0
    for c in configs:
        if 'priority' in c:
            total += c['priority'] * 2
    return total % 1000

def filter_noisy_data(data_stream):
    # Decoy filtering logic
    clean_data = []
    noise_count = 0
    for entry in data_stream:
        if 'ERROR' in entry.get('level', ''):
            noise_count += 1
            continue
        if entry.get('timestamp', 0) < 1000:
            continue
        clean_data.append(entry)
    return clean_data

def extract_critical_codes(log_chunk):
    codes = []
    for item in log_chunk:
        if item['type'] == 'CRITICAL' and item['active']:
            raw_code = item['code']
            processed = ''.join([c for c in raw_code if c.isalnum()])
            if processed.islower():
                codes.append(len(processed))
            elif processed.isupper():
                codes.append(-len(processed))
            else:
                codes.append(0)
    return codes

def evaluate_threshold_breach(values, limit=50):
    count = 0
    for v in values:
        if v > limit:
            count += 1
            if count > 3:
                return True
    return False

def process_metrics(entries, flags):
    # Core relevant logic begins
    temp_registry = []
    flag_sum = sum(f for f in flags if f > 0)  # Only positive flags matter

    for entry in entries:
        if not entry['valid']:
            continue
        raw_value = entry['value']
        adjusted = raw_value
        
        if raw_value > 100:
            adjusted = raw_value // 2
        if 'subtype' in entry and entry['subtype'] == 'calibrated':
            adjusted -= 10

        health_status = analyze_component_health(adjusted)
        if health_status:
            temp_registry.append(adjusted)

    # Extract auxiliary diagnostic info (irrelevant to final result)
    aux_logs = [{'code': f'ERR{i}', 'active': True, 'type': 'CRITICAL'} for i in range(len(temp_registry))]
    critical_lengths = extract_critical_codes(aux_logs)

    # Real computation path
    base_score = sum(temp_registry) % 97
    modifier = len([x for x in temp_registry if x % 2 == 0])  # count evens

    intermediate = base_score * 3 + modifier * 7

    # Apply secondary adjustment based on flag pattern
    flag_pattern_match = any(f % 11 == 0 for f in flags)
    if flag_pattern_match:
        intermediate -= 25
    else:
        intermediate += 15

    # Final transformation using string method red herring
    flag_str = ''.join([chr(97 + abs(f) % 26) for f in flags[:5]])  # 'a'-'z' mapping
    shift_offset = sum(ord(c) for c in flag_str.upper() if c in 'AEIOU')  # vowel ASCII sum

    # But actually, only length of transformed string matters (distraction)
    dummy_shift = len(flag_str.replace('x', '').replace('q', ''))  # irrelevant

    # Actual answer derivation
    core_value = intermediate + (shift_offset % 10)  # only modulo 10 of vowel sum affects result

    # Final irrelevant block: complex but unused structure
    metadata_bundle = {
        'version': '2.1.0',
        'checksum': transform_sequence([base_score, modifier, shift_offset]),
        'diagnostics': generate_diagnostics({'A': 'debug', 'B': 42, 'C': 'trace'})
    }

    final_diagnostic = core_value  # This is the actual target variable
    return final_diagnostic

# Main execution context
log_entries = [
    {'value': 120, 'valid': True, 'subtype': 'calibrated'},
    {'value': 85, 'valid': True},
    {'value': 92, 'valid': True, 'subtype': 'calibrated'},
    {'value': 130, 'valid': True},
    {'value': 70, 'valid': False},  # invalid, skipped
    {'value': 110, 'valid': True}
]

system_flags = [5, 11, 13, 22, 33, 44, 55]  # multiple divisible by 11

final_diagnostic = process_metrics(log_entries, system_flags)
print(f"Result: {final_diagnostic}")