import math

# Simulated system telemetry processing with embedded diagnostics

def analyze_signal_strength(signal: list) -> float:
    # Irrelevant helper: calculates RMS but not used in final path
    squared = [x ** 2 for x in signal]
    mean_sq = sum(squared) / len(squared)
    return math.sqrt(mean_sq)


def generate_checksum(data: dict) -> int:
    # Distractor function: looks important but unused
    chk = 0
    for key, value in data.items():
        chk ^= hash(str(key)) ^ (value % 17)
    return chk % 1000


def decode_transmission(packet: str) -> list:
    # Dead code path: never invoked
    return [int(c, 16) for c in packet if c.isalnum()]


def evaluate_anomalies(readings: list) -> bool:
    # Misleading intermediate logic
    threshold = 42.5
    anomalies = 0
    for val in readings:
        if abs(val - threshold) > 10:
            anomalies += 1
    return anomalies > 5


def compute_entropy(values: list) -> float:
    # Red herring computation
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)


def extract_diagnostic_codes(events: dict) -> list:
    # Unused extraction logic — looks relevant
    codes = []
    for k, v in events.items():
        if isinstance(v, list) and len(v) > 0 and v[-1] == 'ERROR':
            codes.append(hash(k) % 100)
    return sorted(codes)


def filter_critical_logs(entries: list) -> list:
    # Partially relevant but only one value matters
    filtered = []
    for entry in entries:
        if entry['priority'] > 7 and 'temp' in entry['metrics']:
            filtered.append(entry)
    return filtered  # distractor return


def aggregate_health_score(records: list) -> int:
    # Decoy scoring function
    score = 0
    for r in records:
        score += r['health'] * 3
    return score % 85


def validate_system_state(config: dict, flags: dict) -> bool:
    # Complex conditional red herring
    if flags.get('safe_mode', False):
        return True
    if config['version'] < 2 and not flags.get('override', False):
        return False
    return config['nodes'] > 1


def process_metrics(log_entries: list, system_flags: dict) -> int:
    # Core logic buried in noise
    accumulator = 0
    temp_values = []

    # Relevant data extraction
    for log in log_entries:
        if 'metrics' in log and 'temp' in log['metrics']:
            temp_values.append(log['metrics']['temp'])

    # Key transformation: bitwise manipulation on sorted temps
    temp_values.sort()  # Suggested paradigm: sorting
    if len(temp_values) >= 3:
        a = int(temp_values[1])  # second lowest
        b = int(temp_values[-2])  # second highest
        xor_key = (a ^ b) & 0xFF  # Suggested paradigm: bitwise XOR

        # Critical calculation
        prime_seed = 17
        accumulator += (xor_key * prime_seed) // 3

    # Interference: multiple dictionary operations
    status_map = {
        'idle': 0, 'active': 1, 'alert': 2, 'critical': 3
    }
    for entry in log_entries:
        state = entry.get('status', 'idle')
        if state in status_map:
            accumulator += status_map[state]  # minor additive effect

    # Conditional offset based on flag
    if system_flags.get('boost_enabled'):
        boost_factor = system_flags.get('boost_level', 1)
        accumulator *= (boost_factor + 1)
    
    # Final adjustment using hash-derived constant (deterministic)
    salt = hash('diagnostic_finalize') % 50
    accumulator = (accumulator + salt) % 100000

    return accumulator

# Main execution with extensive irrelevant context
if __name__ == '__main__':
    # Simulated telemetry input
    log_entries = [
        {'timestamp': 1678886400, 'priority': 5, 'status': 'active', 'health': 80,
         'metrics': {'temp': 36.2, 'load': 0.45}, 'source': 'sensor_A'},
        {'timestamp': 1678886401, 'priority': 9, 'status': 'alert', 'health': 60,
         'metrics': {'temp': 48.7, 'load': 0.82}, 'source': 'sensor_B'},
        {'timestamp': 1678886402, 'priority': 8, 'status': 'active', 'health': 90,
         'metrics': {'temp': 41.3, 'load': 0.33}, 'source': 'sensor_C'},
        {'timestamp': 1678886403, 'priority': 10, 'status': 'critical', 'health': 40,
         'metrics': {'temp': 52.1, 'load': 0.95}, 'source': 'sensor_D'},
        {'timestamp': 1678886404, 'priority': 7, 'status': 'idle', 'health': 100,
         'metrics': {'temp': 33.9, 'load': 0.12}, 'source': 'sensor_E'}
    ]

    # Irrelevant data structures
    system_config = {
        'version': 3,
        'nodes': 4,
        'timeout': 30,
        'buffer_size': 1024
    }

    system_flags = {
        'safe_mode': False,
        'override': True,
        'boost_enabled': True,
        'boost_level': 2,
        'debug_trace': False,
        'log_compression': 'lz4'
    }

    # Dead computation branches
    signals = [1.2, 3.4, 2.1, 5.6, 4.3]
    _rms = analyze_signal_strength(signals)
    _entropy = compute_entropy([1, 1, 2, 3, 3, 3, 4])
    _valid = validate_system_state(system_config, system_flags)

    # Key execution point
    final_diagnostic = process_metrics(log_entries, system_flags)

    # Output requirement
    print(f"Target result: {final_diagnostic}")