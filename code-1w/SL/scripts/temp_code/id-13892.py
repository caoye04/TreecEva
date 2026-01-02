import math

def analyze_signal(data, threshold=0.5):
    """Irrelevant function: signal analysis with decoy logic."""
    magnitude = sum([abs(x) for x in data])
    normalized = magnitude / len(data) if data else 0
    return normalized > threshold

def validate_checksum(record):
    """Dead code path: never actually used in execution."""
    if not record:
        return False
    checksum = 0
    for c in record:
        checksum ^= ord(c)
    return checksum % 7 == 0

def transform_sequence(seq):
    """Distractor transformation with bit manipulation red herring."""
    result = []
    for i, val in enumerate(seq):
        transformed = (val << 2) ^ 17
        if transformed % 3 == 0:
            result.append(transformed // 3)
        else:
            result.append(transformed)
    return result

def main():
    # Irrelevant sensor simulation
    sensor_grid = [[i + j * 10 for i in range(5)] for j in range(4)]
    active_sensors = sum([len([x for x in row if x % 3 == 0]) for row in sensor_grid])

    # Decoy constants
    MAX_BUFFER_SIZE = 1024
    RETRY_LIMIT = 3
    TIMEOUT_DELAY = 0.25

    # Core data - appears passive but is referenced later
    log_entries = [
        {'timestamp': 1678886400, 'level': 'ERROR', 'payload': 204},
        {'timestamp': 1678886401, 'level': 'INFO', 'payload': 102},
        {'timestamp': 1678886402, 'level': 'WARN', 'payload': 305},
        {'timestamp': 1678886403, 'level': 'ERROR', 'payload': 204}
    ]

    # Misleading aggregation
    error_count = len([e for e in log_entries if e['level'] == 'ERROR'])
    info_count = len([e for e in log_entries if e['level'] == 'INFO'])
    warn_count = len([e for e in log_entries if e['level'] == 'WARN'])

    temp_buffer = [math.log(e['payload']) for e in log_entries]
    avg_log_payload = sum(temp_buffer) / len(temp_buffer)

    # System state with nested structure and irrelevant flags
    system_state = {
        'status': 'ACTIVE',
        'mode': 'diagnostic',
        'flags': {
            'debug_enabled': False,
            'legacy_mode': True,
            'audit_trail': False
        },
        'version': (2, 3, 1),
        'node_id': 0x1A4C
    }

    # Red herring: unused complex lambda
    weighted_sum = lambda vals, weights: sum(v * w for v, w in zip(vals, weights))
    weights = [0.1, 0.2, 0.3, 0.4]
    dummy_result = weighted_sum([10, 20, 30, 40], weights)  # Unused

    # Distractor: character counting in level strings
    total_chars = sum(len(entry['level']) for entry in log_entries)

    # Real logic chain begins here - obscured by prior noise
    critical_ids = [100, 204, 305]
    id_mapping = {100: 'INIT', 204: 'FAULT', 305: 'WARNING'}

    def resolve_code(payload):
        return id_mapping.get(payload, 'UNKNOWN')

    def count_critical_events(entries, codes):
        matched = [e for e in entries if e['payload'] in codes]
        return len(matched)

    event_count = count_critical_events(log_entries, critical_ids)

    # Conditional expression determining next phase
    phase = 'critical' if event_count > 2 else 'stable'

    # Bitwise operation decoy
    status_flag = 0
    if system_state['flags']['debug_enabled']:
        status_flag |= 1 << 3
    if system_state['flags']['legacy_mode']:
        status_flag |= 1 << 1

    # Actual key computation hidden among distractions
    payload_values = [e['payload'] for e in log_entries]
    unique_payloads = list(set(payload_values))
    sorted_payloads = sorted(unique_payloads)

    # Real transformation: sum of squares of unique payloads
    transformed_sum = sum(x ** 2 for x in sorted_payloads)

    # Secondary filter based on timestamp parity
    filtered_entries = [e for e in log_entries if e['timestamp'] % 2 == 0]
    adjustment_factor = len(filtered_entries)

    # Final diagnostic depends on transformed_sum and adjustment_factor
    base_score = transformed_sum * 7
    final_diagnostic = base_score - (adjustment_factor ** 3)

    # Print required at end
    print(f"Result: {final_diagnostic}")

    # Unused recursive function as dead path
    def traverse_tree(node):
        if not node:
            return 0
        return node['value'] + traverse_tree(node.get('left')) + traverse_tree(node.get('right'))

    return final_diagnostic

if __name__ == '__main__':
    main()