import itertools

# System diagnostics simulation with red herrings and complex data flow
def analyze_sensor_array(raw_readings, threshold=0.75):
    normalized = [x / max(raw_readings) for x in raw_readings]
    anomalies = [i for i, v in enumerate(normalized) if v > threshold]
    return anomalies

# Irrelevant auxiliary function (dead path)
def legacy_checksum(data):
    acc = 0
    for x in data:
        acc = (acc + x) * 1103515245 % (2**31)
    return acc % 1000

# Complex state tracker with decoy logic
class DiagnosticsEngine:
    def __init__(self, version):
        self.version = version
        self.log_buffer = []
        self.activation_key = 42

    def validate_signature(self, sig):
        # Unused method - red herring
        return sum(sig) % self.activation_key == 0

    def generate_probe_sequence(self, n):
        seq = [1, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])  # Fibonacci probe
        return seq[:n]

# Misleading data transformation chain
def compute_thermal_gradient(readings):
    gradient = []
    for i in range(1, len(readings)):
        delta = readings[i] - readings[i-1]
        corrected = delta * 1.8 + 32  # Fake unit conversion
        gradient.append(abs(corrected))
    return gradient

# Core processing with distractors
system_status = {
    'firmware': 'v3.7.1',
    'uptime_days': 47,
    'calibration_needed': True,
    'redundancy_level': 3
}

sensor_data = [884, 492, 1023, 776, 201, 512, 999]
fault_flags = [False, True, False, True, False, False, True]

# Dead code block - misleading control flow
if system_status['redundancy_level'] > 5:
    backup_nodes = 6
    fallback_protocol = "QUORUM"
else:
    debug_snapshot = None  # Unused
    audit_trail = []      # Never appended to

# Generate irrelevant sequences
engine = DiagnosticsEngine(version="3.7")
probe_sequence = engine.generate_probe_sequence(len(sensor_data))
filtered_probes = [p for p in probe_sequence if p % 2 == 1]

# Fake signal processing
signal_envelope = [x * 0.001 for x in sensor_data]
envelope_sum = sum(signal_envelope)
baseline_correction = envelope_sum / len(signal_envelope)

# Real but obscured computation begins here
def extract_significant_bits(values):
    bit_plane = 0
    for val in values:
        bit_plane ^= int(val) & 255  # Use only lower byte
    return bit_plane

# Simulated calibration sequence with real impact
calibration_sequence = []
for i, val in enumerate(sensor_data):
    temp = val ^ (i * 17)
    temp = (temp + 32768) % 65536
    calibration_sequence.append(temp)

def merge_diagnostics(code_a, code_b):
    return (code_a + code_b) * 3

def evaluate_health_score(metrics):
    # Unused scoring function - distractor
    weights = [0.1, 0.3, 0.25, 0.35]
    return sum(m * w for m, w in zip(metrics, weights))

def process_metrics(seq, flags):
    # Key logic hidden among noise
    base_value = extract_significant_bits(seq)
    
    # Real dependency on fault_flags
    flag_code = 0
    for i, flag in enumerate(flags):
        if flag:
            flag_code += (i + 1) * 5
    
    # Actual core calculation
    intermediate = base_value ^ flag_code
    intermediate = (intermediate * 19) % 98765
    
    # Add effect of calibration sequence length
    adjustment = len(seq) ** 3
    intermediate = (intermediate + adjustment) % 100000
    
    # Final transformation using itertools (required feature)
    paired = list(itertools.zip_longest(seq[::2], seq[1::2], fillvalue=1))
    multiplier = len(paired)  # 4 pairs from 7 elements
    
    final_result = (intermediate * multiplier) % 100000  # Keep in range
    
    # Decoy dictionary operations (required feature)
    stats_summary = {
        'count': len(seq),
        'first': seq[0],
        'last': seq[-1]
    }
    stats_summary['range'] = stats_summary['last'] - stats_summary['first']
    stats_summary['version'] = system_status['firmware']
    
    return final_result

# Critical execution point
final_diagnostic = process_metrics(calibration_sequence, fault_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")