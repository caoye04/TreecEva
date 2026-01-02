from collections import defaultdict, Counter
import math

# System configuration (partially irrelevant)
SYSTEM_MODE = 'DIAGNOSTIC'
DEBUG_FLAGS = {"verbose": False, "audit": True}
BASE_OFFSET = 17
CALIBRATION_FACTOR = 2.3

# Irrelevant sensor simulation data
temperature_log = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = {'room_a': 45, 'room_b': 52, 'room_c': 48}
pressure_samples = [(1013, 1), (1015, 2), (1012, 3)]

# Core diagnostic parameters
def initialize_buffer(size):
    return [0 for _ in range(size)]

def encrypt_value(x, key):
    shifted = (x ^ key) + 3
    return (shifted * 2) ^ 5

def decrypt_value(y, key):
    # Reverse: undo xor 5, divide by 2, then reverse inner xor and shift
    temp = (y ^ 5) // 2
    return (temp - 3) ^ key

# Misleading auxiliary function (never called)
def legacy_checksum(data):
    chk = 0
    for d in data:
        chk = (chk + d * 3) % 251
    return chk

def generate_sequence(seed, length):
    seq = []
    val = seed % 97
    for i in range(length):
        val = (val * 37 + 13) % 1000
        if i % 4 == 0:
            val = val ^ 15
        elif i % 5 == 0:
            val = (val + 10) % 1000
        seq.append(val)
    return seq

def filter_outliers(data):
    avg = sum(data) / len(data)
    filtered = [x for x in data if abs(x - avg) < 200]
    return filtered if len(filtered) > 0 else data

# Complex analysis with red herring operations
def analyze_pattern(sequence, key):
    buffer = initialize_buffer(len(sequence) + 5)
    history = defaultdict(int)
    stats = Counter()

    encrypted_values = []
    for idx, val in enumerate(sequence):
        enc = encrypt_value(val, key)
        encrypted_values.append(enc)
        history[idx] = enc % 19
        stats['processed'] += 1
        if enc % 3 == 0:
            stats['divisible_by_3'] += 1

    # Dead code path - condition never met due to encryption properties
    if any(x < 0 for x in encrypted_values):
        recovery_mode = True
        for i in range(len(encrypted_values)):
            encrypted_values[i] = abs(encrypted_values[i])
    else:
        recovery_mode = False

    # Actual relevant computation chain
    decrypted_sum = 0
    for enc_val in encrypted_values:
        dec_val = decrypt_value(enc_val, key)
        decrypted_sum += dec_val

    # Secondary transformation (distraction)
    transformed = []
    for v in encrypted_values:
        t = (v >> 2) & 0xFF
        s = int(math.sin(t * 0.01) * 100)
        transformed.append(s)
    
    # Red herring statistical calculation
    mean_transformed = sum(transformed) / len(transformed) if transformed else 0
    variance_proxy = sum(abs(t - mean_transformed) for t in transformed) // len(transformed)

    # Key logic buried among distractions
    raw_total = sum(sequence)
    adjusted_total = decrypted_sum  # Should equal raw_total due to invertibility
    
    # Conditional manipulation based on system mode (irrelevant branch)
    if SYSTEM_MODE == 'OPERATIONAL':
        final_score = (adjusted_total * CALIBRATION_FACTOR) // 1
    else:
        # This is the actual execution path
        adjustment = BASE_OFFSET * (len(sequence) // 10)
        interim = adjusted_total + adjustment
        if interim % 2 == 0:
            interim = interim // 2
        else:
            interim = (interim + 1) // 2
        final_diagnostic = abs(interim - 128)
    
    # Unused derived values (distractors)
    entropy_estimate = len(set(sequence)) / len(sequence) if sequence else 0
    peak_value = max(sequence) if sequence else 0
    checksum_diagnostic = sum(history.values()) * 3

    return final_diagnostic

# Simulated secure handshake data (red herring)
handshake_nonce = 741
auth_token = "SEC-8XJ2"
login_attempts = [{'user': 'admin', 'success': True}, {'user': 'guest', 'success': False}]

# Generate real input data
system_key = 13
raw_sequence = generate_sequence(seed=867, length=14)
cleaned_data = filter_outliers(raw_sequence)
encrypted_sequence = [encrypt_value(x, system_key) for x in cleaned_data]  # Not used; misleads

# Critical execution point
final_diagnostic = analyze_pattern(cleaned_data, system_key)
print(f"Target result: {final_diagnostic}")