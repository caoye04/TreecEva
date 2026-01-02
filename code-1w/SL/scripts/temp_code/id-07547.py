from collections import defaultdict, Counter
import math

# Irrelevant telemetry data (distractor)
telemetry_logs = [
    {'node': 'A1', 'temp': 45, 'status': 'OK'},
    {'node': 'B2', 'temp': 52, 'status': 'WARN'},
    {'node': 'C3', 'temp': 61, 'status': 'ERROR'}
]

# Misleading preprocessing functions (dead path)
def preprocess_telemetry(logs):
    return [log['temp'] for log in logs if log['status'] == 'CRITICAL']

def calculate_entropy(data):
    """Irrelevant entropy calculation (red herring)"""
    freqs = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in freqs.values())

# Core system simulation with hidden logic chain
system_nodes = ['X9', 'Y7', 'Z5']
base_frequency = 13.7
phase_shift = 0.25

# Simulate quantum signature generation (mixed arithmetic and logic)
raw_signatures = []
for idx, node in enumerate(system_nodes):
    # Complex but partially irrelevant computation
    raw_val = (base_frequency + idx) ** phase_shift
    normalized = round(raw_val * 1000) % 256
    raw_signatures.append(normalized)

# Decoy transformation (looks important but unused later)
shifted_signature = [val ^ 0xAA for val in raw_signatures]
deep_copy = shifted_signature[:]

# Real processing begins: filtering and reduction
active_signature = [val for val in raw_signatures if val > 100]  # Only Z5 qualifies

# Bit manipulation red herring
def obfuscate_byte(b):
    b = ((b << 3) & 0xFF) | (b >> 5)
    b ^= 0x1F
    return b

# Unused obfuscation calls (misleading)
_ = [obfuscate_byte(x) for x in deep_copy]

# Key state aggregation via lambda and defaultdict (actual relevant code)
state_registry = defaultdict(lambda: 0)
for i, val in enumerate(active_signature):
    state_registry[f'state_{i}'] = val * 2 - (val // 10)

# Simulated diagnostic engine with recursive validation (core logic)
def validate_subsystem(level, threshold):
    if level <= 1:
        return level
    return level + validate_subsystem(level - 2, threshold)

# Spurious call with no effect (distractor)
_ = validate_subsystem(10, 5)

# Actual critical function with embedded logic chain
def analyze_system_state(signature_part):
    # Input is [204] from active_signature transformed
    base = signature_part[0]
    
    # Multi-step deterministic transformation
    stage1 = base ^ 0xFF  # Invert all bits
    stage2 = (stage1 >> 4) | (stage1 << 4)  # Rotate nibbles
    stage3 = stage2 & 0x7F  # Mask to 7 bits
    stage4 = stage3 ^ (stage3 >> 3)  # XOR shift pattern
    
    # Conditional amplification (depends on bit parity)
    bit_parity = bin(stage4).count('1') % 2
    amplified = stage4 * 17 if bit_parity else stage4 * 15
n    
    # Final adjustment using mathematical identity
    adjusted = int(amplified + math.cos(math.pi * bit_parity))
    
    # Critical reduction through list comprehension filter
    history_buffer = [adjusted - i*3 for i in range(5)]
    filtered = [x for x in history_buffer if x % 2 == 1]  # Keep odds
    final_score = sum(filtered) // len(filtered) if filtered else 0
    
    return final_score

# Execution point of interest
quantum_signature = active_signature  # This equals [204]
final_diagnostic = analyze_system_state(quantum_signature)
print(f"Target result: {final_diagnostic}")