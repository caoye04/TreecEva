def analyze_threat_level(ips, thresholds):
    threat_score = 0
    for ip, data in ips.items():
        if data['failed_attempts'] > thresholds['brute_force']:
            threat_score += 3
        if data['port_scan'] and not data['whitelisted']:
            threat_score += 2
    return threat_score

# Simulated network scan data (distractor)
network_logs = {
    '192.168.1.10': {'failed_attempts': 7, 'port_scan': True, 'whitelisted': False},
    '192.168.1.15': {'failed_attempts': 2, 'port_scan': False, 'whitelisted': True},
    '10.0.0.5': {'failed_attempts': 12, 'port_scan': True, 'whitelisted': False}
}

def calculate_redundancy_checksum(elements):
    checksum = 0
    for i, e in enumerate(elements):
        checksum ^= (e + i) * 3
    return checksum

redundant_data = [13, 7, 22, 4, 9]
redundancy_hash = calculate_redundancy_checksum(redundant_data)

# Core key generation logic (relevant path)
def extract_entropy(source_stream, mask):
    entropy = 0
    for val in source_stream:
        if val & mask:
            entropy += (val ^ mask) % 7
    return entropy

sensor_readings = [85, 112, 193, 44, 76]
magic_mask = 0b1101
entropy_value = extract_entropy(sensor_readings, magic_mask)

# Misleading cryptographic stubs (dead code / red herrings)
class CipherStub:
    def __init__(self, strength):
        self.strength = strength
        self.rounds = 0

    def encrypt(self, data):
        # Not used in actual computation
        return sum(data) % 1000

weak_cipher = CipherStub(128)
legacy_hash = weak_cipher.encrypt([21, 34, 55])

# Real weighting function
def compute_auth_weight(factors, base_multiplier=1.7):
    total = 0.0
    weight_map = {}
    for k, v in factors.items():
        if 'critical' in k:
            weight_map[k] = v * base_multiplier * 0.8
        elif 'minor' in k:
            weight_map[k] = v * 0.3
        else:
            weight_map[k] = v * 0.5
    for w in weight_map.values():
        total += w
    return round(total, 4)

auth_factors = {
    'critical_error_count': 6,
    'minor_alerts': 4,
    'system_uptime': 92,
    'pending_updates': 3
}

auth_weight = compute_auth_weight(auth_factors)

# Entropy pool construction (relevant)
entropy_pool = (entropy_value * 17) + (len(network_logs) * 5)

# Auxiliary decoy transformation (irrelevant)
def transform_credentials(credentials):
    transformed = []
    for cred in credentials:
        transformed.append(''.join(reversed(cred)) + '_old')
    return transformed

dummy_creds = ['admin', 'guest', 'backup']
expired_tokens = transform_credentials(dummy_creds)

# Key combination logic
auth_weights = [auth_weight, entropy_pool, redundancy_hash, threat_score]

# Finalization function (key point)
def finalize_key(weights, salt):
    key = int(weights[0] * 100)  # Convert float weight to integer base
    key ^= weights[1]            # XOR with entropy pool
    key += salt % 19             # Add modular salt
    key &= 0xFFFFF               # Limit to 20 bits
    return key

# Dead code: Obsolete key migration logic
old_keys = [0xabcde, 0xf00ba, 0xbeef1]
for i in range(len(old_keys)):
    old_keys[i] = (old_keys[i] << 1) | ((old_keys[i] >> 19) & 1)

# Critical execution point
target_threshold = 8
threat_score = analyze_threat_level(network_logs, {'brute_force': 5})
security_key = finalize_key(auth_weights, entropy_pool)

print(f"Result: {security_key}")