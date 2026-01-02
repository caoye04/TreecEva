import math

# Simulated sensor fusion module for aerospace telemetry
def analyze_vibration(pattern):
    if len(pattern) < 3:
        return 0
    return sum(p ** 2 for p in pattern[:3]) * 0.1

def evaluate_stress_factor(load, temperature):
    base = (load * 1.5 + temperature * 0.8) / 2.3
    adjustment = math.sin(math.radians(min(load, 90)))
    return base + adjustment

def compute_redundancy_score(nodes):
    # Irrelevant function - decoy
    return len(nodes) * 2 if all(n > 0 for n in nodes) else -1

def encrypt_handshake(token):
    # Dead code path - never used in logic
    return ''.join(chr((ord(c) + 3) % 127) for c in token)

def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings] if max_val > 0 else readings

def generate_synthetic_trace(length):
    # Distractor: generates unused data
    return [int(100 * math.cos(i * 0.5)) for i in range(length)]

def validate_checksum(data_str):
    # Misleading intermediate - looks important
    return sum(ord(c) for c in data_str) % 256 == 127

# Critical processing pipeline
def extract_phase_vector(signal):
    if not signal:
        return [0]
    mid = len(signal) // 2
    return signal[mid-1:mid+2]

def calculate_coherence_index(amplitudes, phases):
    weighted = [a * (p + 1) for a, p in zip(amplitudes[:len(phases)], phases)]
    return round(sum(weighted) / len(weighted), 4) if weighted else 0.0

def derive_safety_margin(threshold, current):
    return (threshold - current) / threshold if threshold != 0 else 0.0

def assess_integrity_level(signature):
    # Complex but irrelevant transformation
    transformed = [((s << 2) ^ 0x5A) & 0xFF for s in signature]
    filtered = [t for t in transformed if t % 3 == 0]
    return sum(filtered) / len(transformed) if transformed else 0

# Main diagnostic processor
def process_metrics(signature, load):
    # Extract key components
    vib_pattern = signature[::3][:5]
    stress_temp = signature[1::4][:2]
    
    # Real computation branch
    vibration_score = analyze_vibration(vib_pattern)
    temperature = stress_temp[1] * 2.1 if len(stress_temp) > 1 else 0
    stress_score = evaluate_stress_factor(load, temperature)
    
    # Red herring: complex bit manipulation with no impact
    decoy_bits = 0
    for x in signature:
        decoy_bits ^= (x << 3) | (x >> 2)
    decoy_flag = (decoy_bits & 0xF) > 7
    
    # Another distraction: string processing that goes nowhere
    status_tag = "SYS_OK" if load < 80 else "LOAD_HIGH"
    extended_diagnostic = status_tag.lower().replace('_', '-') + "_v2"
    validation_chain = "->".join([extended_diagnostic] * 2)
    
    # Core logic begins here
    phase_data = extract_phase_vector(signature)
    normalized_sig = normalize_readings(signature)
    
    # Key calculation
    coherence = calculate_coherence_index(normalized_sig, phase_data)
    safety_margin = derive_safety_margin(95.0, vibration_score + stress_score)
    
    # Tuple unpacking and conditional expression
    weights = (0.6, 0.4) if safety_margin > 0.1 else (0.3, 0.7)
    weighted_avg = lambda w1, w2: w1 * vibration_score + w2 * stress_score
    
    primary_metric = weighted_avg(*weights)
    
    # Final integration using lambda and conditional expression
    adjustment_factor = (lambda x: math.log(x + 1) if x > 0 else 0)(coherence)
    final_raw = primary_metric * (1 + adjustment_factor)
    
    # This is the actual answer computation - everything above provides context and noise
    final_diagnostic = int(round(final_raw * 100))
    
    # Unused sorting operation - distractor
    sorted_signature = sorted(signature, reverse=True)
    
    # Dead function call
    fake_hash = encrypt_handshake("HEALTH")
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data - fixed for determinism
health_signature = [23, 18, 45, 67, 33, 29, 52, 14, 38, 41]
system_load = 76

# Execution point of interest
final_diagnostic = process_metrics(health_signature, system_load)