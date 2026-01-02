import itertools

# System health monitoring simulation with red herrings and complex data flow

def analyze_signal_strength(readings):
    if not readings:
        return 0
    filtered = [r for r in readings if r > 0]
    if len(filtered) < 3:
        return -1
    sorted_readings = sorted(filtered, reverse=True)
    top_three_product = sorted_readings[0] * sorted_readings[1] * sorted_readings[2]
    return top_three_product // len(filtered)


def evaluate_consistency(patterns):
    if not patterns:
        return False
    lengths = [len(p) for p in patterns]
    avg_len = sum(lengths) / len(lengths)
    deviation = sum(abs(l - avg_len) for l in lengths)
    return deviation < 5

# Irrelevant helper - decoy function (dead logic path)
def legacy_checksum(data):
    return sum((d * (i + 1)) % 7 for i, d in enumerate(data)) % 13

# Unused transformation chain
def transform_sequence(seq):
    paired = list(itertools.pairwise(seq))
    rolled = [(a + b, b - a) for a, b in paired]
    flattened = list(itertools.chain.from_iterable(rolled))
    return [x for x in flattened if x != 0]

# Misleading diagnostic with side effects that don't matter
def false_diagnostic_trace(inputs):
    state = 100
    for val in inputs:
        if val % 2 == 0:
            state ^= val % 17
        else:
            state += val % 5
    return state * 2  # Diversion: never used in final result

# Core processing function with critical logic interwoven with noise
def aggregate_metrics(chains, flags):
    total = 0
    
    # Real computation branch
    for chain in chains:
        segment_sum = 0
        for step in chain:
            if isinstance(step, dict) and 'ops' in step:
                for op in step['ops']:
                    if op['type'] == 'shift':
                        segment_sum += (op['value'] << 2)
                    elif op['type'] == 'factor':
                        segment_sum *= 2
                        segment_sum += op['value']
        total += segment_sum
    
    # Distractor block: looks important but unused
    debug_snapshot = []
    for i, flag in enumerate(flags):
        snapshot_entry = {
            'index': i,
            'hash': (i * 31 + hash(flag)) % 1000,
            'status': 'nominal' if 'OK' in flag else 'degraded'
        }
        debug_snapshot.append(snapshot_entry)
    
    # Another red herring: complex but irrelevant string manipulation
    log_header = """DGN-TRACE|{'nodes':8}|mode=deep"""
    tokens = log_header.split('|')
    parsed_config = {part.split('=')[0]: part.split('=')[1] for part in tokens if '=' in part}
    node_count = int(parsed_config.get('nodes', 1))
    
    # Decoy bit manipulation sequence
    accumulator = 0xDEADBEEF
    for _ in range(node_count):
        accumulator = ((accumulator << 3) | (accumulator >> 29)) & 0xFFFFFFFF
        accumulator ^= 0xCAFEBABE
    
    # Critical answer derivation (interleaved with noise)
    base_score = total
    adjustment_factor = len(flags) if evaluate_consistency(flags) else 1
    raw_diagnostic = base_score * adjustment_factor
    
    # Final computation using real data
    final_diagnostic = raw_diagnostic + analyze_signal_strength([4, 7, 2, 9, 5])
    
    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Orchestration with misleading setup
if __name__ == '__main__':
    # Actual relevant data structure
    processing_chain = [
        [
            {'ops': [{'type': 'shift', 'value': 3}, {'type': 'factor', 'value': 2}]},
            {'ops': [{'type': 'shift', 'value': 1}, {'type': 'factor', 'value': 4}]}
        ],
        [
            {'ops': [{'type': 'shift', 'value': 5}, {'type': 'factor', 'value': 1}]}
        ]
    ]
    
    # Flags used in real logic
    diagnostics = ['OK-STATUS', 'OK_READY', 'NORMAL_OP']
    
    # Irrelevant variables (distraction)
    buffer_pool = [legacy_checksum([1,2,3,4]), legacy_checksum([5,6,7])]
    temp_state = false_diagnostic_trace([3, 6, 9, 12])
    audit_log = list(itertools.accumulate([1, -1, 2, -2, 3], lambda a, b: a + b))
    
    # Key execution point
    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)