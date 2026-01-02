from collections import defaultdict, Counter
import math

# Simulated network packet analysis with decoy computations
def analyze_packet_sequence(packets):
    stats = defaultdict(int)
    temporal_gaps = []
    cumulative_xor = 0
    
    for i, pkt in enumerate(packets):
        size = pkt['size']
        timestamp = pkt['ts']
        checksum = pkt['chk']
        
        stats['total_size'] += size
        stats['packet_count'] += 1
        
        if i > 0:
            gap = timestamp - packets[i-1]['ts']
            temporal_gaps.append(gap)
            
        # Red herring: bit manipulation on checksum (not used in final result)
        cumulative_xor ^= (checksum & 0xFF) | (size << 2)
        
    # Distractor: frequency analysis of gaps (unused)
    gap_counter = Counter(temporal_gaps)
    avg_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
    
    # Irrelevant transformation chain
    transformed = [math.sin(g * 0.01) for g in temporal_gaps]
    smoothed = sum(abs(t) for t in transformed) / len(transformed) if transformed else 0
    
    # Meaningless recursive helper (dead code path)
    def useless_tree_depth(n):
        if n <= 1:
            return 1
        return 1 + useless_tree_depth(n // 2) + useless_tree_depth((n // 3))
    
    # Dummy variables to increase interference
    entropy_estimate = len(gap_counter) * 0.5
    jitter_metric = max(temporal_gaps) - min(temporal_gaps) if temporal_gaps else 0
    
    # Key intermediate values (only some are used later)
    metrics = {
        'base': stats['total_size'],
        'count': stats['packet_count'],
        'avg_gap': avg_gap,
        'smoothed': smoothed
    }
    
    return metrics

# Decoy function that appears related but isn't called in main logic
def evaluate_latency_pattern(sequence):
    score = 0
    for s in sequence:
        score += (s % 7) ** 2
    return score * 1.5

# Core computation with embedded distractions
def compute_aggregate(data_stream, threshold=256):
    # Real work begins here
    raw_values = [x for x in data_stream if x > 0]
    filtered = list(filter(lambda x: x < threshold, raw_values))
    
    # Complex unpacking and conditional expressions
    primary_sum = sum(filtered)
    backup_sum = sum(x for x in raw_values if x >= threshold)
    
    # Tuple unpacking with dummy elements
    (main_payload, _, _) = (primary_sum, backup_sum, len(filtered))
    
    # Conditional expression using bitwise and arithmetic mix
    adjustment_factor = 0.85 if (main_payload & 1023) > 500 else 1.15
    
    # Simulated multi-stage processing pipeline
    stage1 = main_payload * adjustment_factor
    stage2 = int(stage1 + 0.5)
    
    # Dead branch: never executed due to constant condition
    debug_mode = False
    if debug_mode and len(raw_values) > 1000:
        stage2 = int(stage1 * 1.1)
    
    # Another layer of distraction: string-based key derivation (unused)
    key_parts = [str(len(raw_values)), str(primary_sum % 100), 'XOR']
    derived_key = '-'.join(key_parts).replace('XOR', 'CHK')
    validation_hash = hash(derived_key) & 0xFFFF
    
    # Final computation chain (this is what actually matters)
    temp_result = stage2 >> 2  # Divide by 4 using bit shift
    correction = (temp_result % 97)  # Modulo operation for fine adjustment
    final_score = temp_result - correction + 42  # Deterministic offset
    
    # Spurious print statements (distractors)
    # print(f'Debug: validation_hash={validation_hash}')
    # print(f'Simulated entropy: {validation_hash % 13}')
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated input data
    packet_data = [
        {'size': 64, 'ts': 1000, 'chk': 0x1A2B},
        {'size': 128, 'ts': 1005, 'chk': 0x3C4D},
        {'size': 256, 'ts': 1012, 'chk': 0x5E6F},
        {'size': 512, 'ts': 1020, 'chk': 0x7G8H},  # Note: G,H not hex - but parsed as int below
        {'size': 1024, 'ts': 1035, 'chk': 0x9I0J}
    ]
    
    # Fix non-hex characters for actual execution
    for p in packet_data:
        # Simulate numeric checksum from truncated hex string
        chk_str = str(p['chk'])[-4:]
        p['chk'] = int(chk_str, 16) if chk_str.isalnum() else 0
    
    # Extract stream for core function (this is the real input)
    data_stream = [p['size'] * 2 + (i * 16) for i, p in enumerate(packet_data)]
    
    # Run analysis (result not used - red herring)
    analysis_results = analyze_packet_sequence(packet_data)
    
    # Compute the actual target value
    final_score = compute_aggregate(data_stream, threshold=256)
    
    # Output the required result
    print(f"Target result: {final_score}")