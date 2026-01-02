from collections import defaultdict, Counter
import math

# Simulated sensor pattern buffer with redundant and diagnostic data
def generate_pattern_buffer():
    raw_samples = [i ^ (i >> 2) for i in range(150) if i % 3 != 0]
    filtered = [x for x in raw_samples if x & 1]  # Only odd values
    history_log = defaultdict(int)
    for val in filtered:
        history_log[val] += 1
    
    # Irrelevant aggregation
    stats_summary = {
        'peak': max(filtered),
        'entropy': sum(math.log(x) if x > 1 else 0 for x in filtered),
        'median_approx': sorted(filtered)[len(filtered)//2]
    }
    
    # Actual signal pattern used later
    return [filtered[i] * 2 for i in range(0, len(filtered), 4)]

# Fault signature generator — only some outputs are relevant
def generate_fault_mask():
    base_mask = [i * 3 + 1 for i in range(40)]
    decoy_shift = [(x << 2) | 1 for x in base_mask if x % 5 != 0]
    decoy_stats = Counter(decoy_shift)
    
    # Red herring computation
    anomaly_score = sum(1 for x in decoy_shift if bin(x).count('1') % 2 == 0)
    normalization_factor = math.sqrt(sum(x*x for x in decoy_shift[:10]))
    
    # Relevant compressed mask
    return [base_mask[i] ^ base_mask[-i-1] for i in range(len(base_mask)//2)]

# Signal analyzer with multiple internal distractions
def analyze_signal(signal, mask):
    # Misleading pre-analysis
    noise_floor = sum(s & 0xFF for s in signal) / len(signal)
    spectral_density = [math.sin(math.pi * s / 100) for s in signal]
    
    # Distractor: unused transformation chain
    temp_grid = [[s + m for m in mask[:5]] for s in signal[:10]]
    grid_checksum = sum(sum(row) for row in temp_grid) % 1000
    
    # Real computation begins
    aligned_pairs = list(zip(signal[:len(mask)], mask))
    processed = []
    for s, m in aligned_pairs:
        if m % 4 == 0:
            processed.append(s ^ m)
        elif m % 3 == 0:
            processed.append(s + (m & 7))
        else:
            processed.append(s - (m % 5))
    
    # Accumulation with irrelevant modifiers
    modifier_pool = [x for x in processed if x > 0]
    decay_factor = len(modifier_pool) / len(processed) if processed else 0
    
    # Final integration
    aggregate = 0
    for i, val in enumerate(processed):
        if i % 5 == 0:
            aggregate += val * 2
        elif i % 3 == 0:
            aggregate -= val // 2
        else:
            aggregate += val
    
    # Key result obscured among other variables
    diagnostic_weight = sum(math.ceil(val / 10) for val in processed) // len(processed)
    final_diagnostic = int(abs(aggregate) * (1 + decay_factor)) + diagnostic_weight
    
    # Dead code path — never executed but looks important
    if False:
        backup_repair = [val ^ 0xFFFF for val in processed]
        final_diagnostic = sum(backup_repair) // 100
    
    return final_diagnostic

# Execution flow with red herrings
if __name__ == "__main__":
    # Unused initialization (distractor)
    system_ticks = sum(i * i for i in range(100)) % 10000
    runtime_cache = {i: math.factorial(i) % 1000 for i in range(10)}

    # Critical data generation
    pattern_buffer = generate_pattern_buffer()
    fault_mask = generate_fault_mask()

    # Irrelevant validation check
    if len(pattern_buffer) < 20 or len(fault_mask) < 20:
        raise RuntimeError("Buffer underflow")  # This never triggers

    # Core analysis
    final_diagnostic = analyze_signal(pattern_buffer, fault_mask)
    
    # Unused post-processing
    normalized_result = final_diagnostic / (math.pi * 2)
    rounded_trace = round(normalized_result, 3)

    print(f"Result: {final_diagnostic}")