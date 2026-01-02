from collections import defaultdict, Counter
import math

# Simulated sensor health monitoring system for a distributed IoT network

def analyze_pattern(sequence):
    # Irrelevant helper: analyzes repeating subsequences (dead-end logic)
    freq = Counter()
    for i in range(len(sequence)):
        for j in range(i+2, len(sequence)+1):
            freq[tuple(sequence[i:j])] += 1
    return max(freq.values(), default=0)

def auxiliary_checksum(data):
    # Distractor function: computes XOR checksum (not used in final result)
    chk = 0
    for val in data:
        chk ^= int(val * 100) % 256
    return chk

def evaluate_stability(ring_buffer):
    # Misleading stability metric based on variance (unused)
    mean = sum(ring_buffer) / len(ring_buffer)
    var = sum((x - mean)**2 for x in ring_buffer) / len(ring_buffer)
    return var < 0.05

def detect_spikes(stream, threshold):
    # Red herring: detects large jumps (computed but not critical)
    spikes = 0
    for i in range(1, len(stream)):
        if abs(stream[i] - stream[i-1]) > threshold:
            spikes += 1
    return spikes > 3

def compute_entropy(values):
    # Decoy information-theoretic measure (no impact)
    counts = Counter(values)
    probs = [count / len(values) for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def core_integrity_score(seq):
    # Actually relevant but obfuscated: computes weighted sum modulo prime
    weight = 1
    total = 0
    prime = 97
    for val in seq:
        weight = (weight * 7) % prime
        total = (total + val * weight) % prime
    return total

def extract_critical_flags(sensor_ranks):
    # Processes ranking to extract binary flags (partially relevant)
    flags = 0
    for i, rank in enumerate(sensor_ranks):
        if rank < 3:
            flags |= (1 << i)
    return flags & 0xF  # Only lower 4 bits matter

def process_metrics(data, limits):
    # MAIN FUNCTION: heavily interspersed with distractors
    
    # Step 1: Filter valid sensors (temperature within operational bounds)
    valid_ids = []
    temp_readings = []
    for sid, readings in data.items():
        avg_temp = sum(readings['temp']) / len(readings['temp'])
        if limits['min_temp'] <= avg_temp <= limits['max_temp']:
            valid_ids.append(sid)
            temp_readings.append(avg_temp)
    
    # Step 2: Compute pressure trend (red herring computation)
    total_pressure = 0
    for readings in data.values():
        total_pressure += sum(readings['pressure'])
    avg_pressure = total_pressure / sum(len(r['pressure']) for r in data.values())
    
    # Step 3: Analyze temporal consistency (distractor call)
    for readings in data.values():
        _ = detect_spikes(readings['temp'], 0.5)
        _ = compute_entropy(readings['temp'])
    
    # Step 4: Rank sensors by response latency (critical path)
    latency_ranking = []
    for sid in valid_ids:
        latency_score = sum(data[sid]['response']) / len(data[sid]['response'])
        latency_ranking.append((sid, latency_score))
    
    # Sort ascending (lower latency = better)
    latency_ranking.sort(key=lambda x: x[1])
    ranked_ids = [sid for sid, _ in latency_ranking]
    
    # Step 5: Map ranks to positions (used in flag extraction)
    position_map = {sid: idx for idx, sid in enumerate(ranked_ids)}
    
    # Step 6: Extract signal coherence from phase data (irrelevant)
    coherence_values = []    
    for readings in data.values():
        if 'phase' in readings:
            coherence = sum(abs(readings['phase'][i] - readings['phase'][i-1]) 
                          for i in range(1, len(readings['phase'])))
            coherence_values.append(coherence)
    
    # Step 7: Build diagnostic vector from multiple sources (partial use)
    diagnostics = defaultdict(float)
    for i, sid in enumerate(ranked_ids):
        temp_val = sum(data[sid]['temp']) / len(data[sid]['temp'])
        diagnostics[sid] = temp_val * (i + 1)  # Weight by rank position
    
    # Step 8: Generate flag vector from top performers
    top_performers = ranked_ids[:4]  # At most 4
    sensor_ranks = [position_map[sid] for sid in top_performers]
    flag_code = extract_critical_flags(sensor_ranks)
    
    # Step 9: Compute integrity of diagnostic sequence (ACTUALLY USED)
    diag_sequence = [int(diagnostics[sid]) for sid in top_performers]
    integrity = core_integrity_score(diag_sequence)
    
    # Step 10: Final nonlinear transformation (ANSWER DEPENDS ON THIS)
    raw_metric = (flag_code * 256) + integrity
    scaled = raw_metric * 0.75
    adjusted = math.floor(scaled) + 17
    
    # FINAL ANSWER
    final_diagnostic = adjusted
    
    # Irrelevant final checks (dead code path)
    if evaluate_stability(temp_readings):
        _ = auxiliary_checksum(temp_readings)
    
    return final_diagnostic

# Simulated input data
health_data = {
    101: {
        'temp': [22.1, 22.3, 21.9, 22.0, 22.2],
        'pressure': [101.3, 101.4, 101.2],
        'response': [0.45, 0.47, 0.44],
        'phase': [0.1, 0.12, 0.09]
    },
    102: {
        'temp': [23.5, 23.7, 23.6, 23.8],
        'pressure': [102.1, 102.0],
        'response': [0.33, 0.31, 0.35, 0.34],
        'phase': [0.25, 0.27, 0.26]
    },
    103: {
        'temp': [18.0, 17.8, 18.2, 17.9],
        'pressure': [99.8, 99.9],
        'response': [0.55, 0.58, 0.54],
        'phase': [0.41, 0.43]
    },
    104: {
        'temp': [24.1, 24.3, 24.0],
        'pressure': [103.2],
        'response': [0.28, 0.29, 0.27, 0.30],
        'phase': [0.18, 0.20, 0.19, 0.21]
    },
    105: {
        'temp': [16.5, 16.7],  # Below min_temp, will be filtered out
        'pressure': [98.0],
        'response': [0.61, 0.63],
        'phase': [0.55, 0.57]
    }
}

thresholds = {
    'min_temp': 17.0,
    'max_temp': 25.0
}

# Execution point
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")