def analyze_pattern(sequence):
    if len(sequence) < 5:
        return False
    sorted_seq = sorted(sequence)
    median = sorted_seq[len(sorted_seq) // 2]
    return median > 30 and sum(1 for x in sequence if x % 2 == 0) >= 3

# Irrelevant helper (dead path)
def compute_entropy(data):
    import math
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused transformation
def shift_cipher(text, shift=3):
    return ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.isalpha() and c.islower() else c for c in text)

# Decoy state variables
cached_result = None
diag_log = set()
temp_buffer = [0] * 100

# Core logic disguised among distractions
baseline_readings = [23, 45, 67, 89, 12, 34, 56, 78]

# Misleading pre-processing
adjusted = [x + 5 for x in baseline_readings if x < 70]
filtered = [x for x in adjusted if x % 3 != 0]

# Distractor: complex but unused structure
class SignalProcessor:
    def __init__(self, window_size):
        self.window = window_size
        self.cache = []

    def transform(self, val):
        return (val * 2) ^ self.window

# Real computation begins
signature_str = "A1B2C3D4E5"
digits = [int(c) for c in signature_str if c.isdigit()]
offsets = {i: d * 2 for i, d in enumerate(digits)}

# Actual signal extraction
health_signature = [baseline_readings[i % len(baseline_readings)] + offsets[i % len(digits)] for i in range(8)]

# Threshold map with red herring entries
threshold_map = {
    'low': 35,
    'critical': 90,
    'watch': 60,
    'ignore_me': 999,  # decoy
    'enable_flag': True,
    'mode': 'strict'
}

# Secondary distraction: string analysis with no impact
diag_code = "ERROR_45X"
diag_parts = diag_code.lower().replace('_', '').split('45')
flag_state = ''.join(diag_parts).upper().isalpha()

# Real processing function
def process_metrics(signal, config):
    level = config['low']
    critical_level = config['critical']
    watch_level = config['watch']

    above_low = sum(1 for x in signal if x > level)
    above_watch = sum(1 for x in signal if x > watch_level)
    above_critical = sum(1 for x in signal if x > critical_level)

    # Complex decision logic
    if above_critical > 2:
        score = -1000
    elif above_watch > 3 and not (above_low < 5 and len(signal) % 2 == 1):
        score = 420
    else:
        score = (above_low * 17) - (above_watch * 12)

    # Bit manipulation distraction (but actually used)
    meta_flag = len(signal) ^ 8
    if meta_flag & 8:
        score = score ^ 15

    # String-based toggle (irrelevant but looks important)
    mode_key = config.get('mode', '')
    if mode_key.startswith('s'):
        alt_score = len("process_metrics".upper().swapcase())
        score += 5 if alt_score % 2 else -3

    return score

# Key execution point
final_diagnostic = process_metrics(health_signature, threshold_map)
print(f"Target result: {final_diagnostic}")