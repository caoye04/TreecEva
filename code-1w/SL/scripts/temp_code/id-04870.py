def compute_integrity_score(data_stream, config):
    # Irrelevant configuration parsing
    threshold = config.get('threshold', 42)
    debug_mode = config.get('debug', False)
    timeout = config.get('timeout', 300)
    retries = config.get('retries', 3)
    temp_buffer = [0] * 16
    
    # Distractor: unused cryptographic constants
    CRYPTO_P = 65519
    CRYPTO_Q = 65521
    salt = config.get('salt', 1234)

    # Initialization of relevant variables
    state_vector = [i ^ config['seed'] for i in range(8)]
    checksum = 1
    sequence_log = []
    anomaly_count = 0

    # Simulated data processing with red herrings
    for index, raw_value in enumerate(data_stream):
        # Bit manipulation decoy
        masked = raw_value & 0xFF
        extended = (masked << 1) | (masked >> 7)
        inverted = ~extended & 0xFFFF

        # Distractor: power analysis side-channel simulation (dead computation)
        power_trace = 0
        for bit in range(16):
            if (inverted >> bit) & 1:
                power_trace += bit ** 2
        if power_trace > 1000:  # Never triggers due to values
            temp_buffer[0] = 999

        # Real logic buried among distractions
        if index % 2 == 0:
            scaled = raw_value * 2
        else:
            scaled = raw_value // 2 + 1

        # Critical path: conditional update based on state
        feedback = state_vector[index % len(state_vector)]
        adjusted = (scaled ^ feedback) % 1000

        # Decoy statistical tracking
        mean_proxy = sum(state_vector) / len(state_vector)
        variance_proxy = sum((x - mean_proxy) ** 2 for x in state_vector) / len(state_vector)
        if variance_proxy < 50:
            anomaly_count += 1  # Misleading metric

        # Update state vector using enumerate and zip (required features)
        temp_state = state_vector.copy()
        for i, val in enumerate(zip(state_vector, reversed(temp_state))):
            a, b = val
            temp_state[i] = (a ^ b + index) % 256
        state_vector = temp_state

        # Core integrity calculation (target logic)
        value = adjusted % 89
        checksum = (checksum + value) % 97

        # Logging distractor
        sequence_log.append({
            'idx': index,
            'raw': raw_value,
            'adj': adjusted,
            'chk': checksum,
            'power': power_trace  # Unused field
        })

        # Fake fault injection check
        if index == config['fault_at']:
            checksum = (checksum * 2) % 97  # Never executes: fault_at not in config

    # Final irrelevant transformation
    final_shift = config['seed'] ^ 0xABCD
    normalized_checksum = (checksum + final_shift) % 97
    result_payload = {'status': 'OK', 'crc': normalized_checksum}

    # Output required variable
    print(f"Result: {checksum}")

# Inputs
config_params = {
    'seed': 7,
    'threshold': 42,
    'debug': False,
    'timeout': 300,
    'retries': 3,
    # 'fault_at' intentionally omitted
}

data_feed = [123, 45, 88, 23, 7, 91, 150, 64]

compute_integrity_score(data_feed, config_params)