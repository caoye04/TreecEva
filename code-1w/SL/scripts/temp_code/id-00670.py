def analyze_sequence(data):
    # Irrelevant transformation chain (distractor)
    temp_map = {i: val ** 2 for i, val in enumerate(data)}
    shifted = [v % 7 for v in temp_map.values()]
    checksum = sum(shifted) // 3

    # Red herring: complex but unused computation
    decoy_matrix = [[i * j for j in range(4)] for i in range(4)]
    trace = sum(decoy_matrix[i][i] for i in range(4))

    # Actual relevant logic hidden among noise
    valid_count = len([x for x in data if x > 0 and x % 2 == 1])
    return valid_count * 2 + checksum  # Used later


def extract_signals(raw_log):
    # Parsing string patterns (required string method)
    lines = raw_log.strip().split('\n')
    signal_codes = []
    for line in lines:
        parts = line.split(':')
        if len(parts) > 1 and 'SIG' in parts[0]:
            code = int(parts[1].strip()[0])
            signal_codes.append(code)
    
    # Dead path: never called function
    def decode_legacy_format(s):
        return s[::-1].upper()
    
    # Distractor: intermediate statistic not used in final result
    avg_code = sum(signal_codes) / len(signal_codes) if signal_codes else 0
    return signal_codes


def compute_integrity(nodes):
    # Dictionary operations (required feature)
    status_map = {node['id']: node['active'] for node in nodes}
    active_count = sum(status_map.values())
    
    # Bit manipulation red herring
    flag_register = 0
    for i, active in enumerate(status_map.values()):
        if active:
            flag_register |= (1 << i)
    
    # Unused recursive distraction
    def explore_subtree(idx):
        if idx >= len(nodes):
            return 0
        return 1 + explore_subtree(idx + 2)
    
    return active_count * 3


# Main execution with mixed paradigms
if __name__ == '__main__':
    # Input data setup
    sensor_data = [3, -1, 7, 8, 11, 14, 15, 21]
    log_text = '''
    INIT: System online
    SIG: 9A2 detected
    STATUS: nominal
    SIG: 3B1 reported
    DEBUG: cycle complete
    SIG: 7C4 observed
    '''
    
    network_nodes = [
        {'id': 'N1', 'active': True, 'type': 'router'},
        {'id': 'N2', 'active': False, 'type': 'sensor'},
        {'id': 'N3', 'active': True, 'type': 'gateway'},
        {'id': 'N4', 'active': True, 'type': 'endpoint'}
    ]

    # Irrelevant pre-processing steps
    normalized = [x / max(sensor_data) for x in sensor_data]
    categories = ['low' if x < 0.5 else 'high' for x in normalized]
    category_count = {cat: categories.count(cat) for cat in set(categories)}  # Unused dict

    # Key variables interwoven with distractors
    base_metric = analyze_sequence(sensor_data)
    
    # String-based extraction (uses string methods)
    signals = extract_signals(log_text)
    signal_sum = sum(signals)  # Looks important, but only partially used
    
    # Data structure processing
    health_score = compute_integrity(network_nodes)
    
    # Complex conditional with misleading branches
    adjustment_factor = 0
    if len(signals) > 2:
        adjustment_factor += 4
        temp = signal_sum // 2
        if temp % 2 == 0:
            adjustment_factor += 2  # Never reached
    else:
        adjustment_factor -= 1
    
    # Decoy list comprehensions
    phantom_values = [base_metric * i for i in range(5) if i % 2 == 0]
    shadow_copy = [x for x in phantom_values]  # Unused

    # Core logic disguised as one among many
    log_entries = len(log_text.split('\n'))
    system_state = {
        'nodes': len(network_nodes),
        'active_ratio': health_score / 3,
        'signals_received': len(signals),
        'base_diagnostic': base_metric
    }

    # Final computation buried in complexity
    def process_metrics(entries, state):
        # Integer division and rounding usage
        base = state['base_diagnostic']
        load = entries // 2
        stress_adj = round(load * 0.75)
        
        # Character counting distractor
        raw_chars = len(log_text.replace(' ', '').replace('\n', ''))
        char_weight = raw_chars // 10  # Looks meaningful
        
        # Actual formula: combines arithmetic, ignores most strings/dicts
        result = base + stress_adj + state['signals_received']
        return result
    
    final_diagnostic = process_metrics(log_entries, system_state)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")