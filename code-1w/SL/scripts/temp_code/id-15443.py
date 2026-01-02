import math

# System health monitoring simulation with red herrings and complex data flow
def monitor_system_health():
    raw_signals = [0.78, 0.65, 0.92, 0.45, 0.88, 0.71, 0.59, 0.96]
    calibration_offsets = [0.1, -0.05, 0.08, -0.12, 0.03, 0.07, -0.09, 0.04]
    
    # Irrelevant preprocessing: signal smoothing (unused later)
    smoothed = [raw_signals[i] + calibration_offsets[i] * 0.5 for i in range(len(raw_signals))]
    normalized = [x / max(raw_signals) for x in raw_signals]
    
    # Decoy transformation chain
    fft_magnitude = sum([math.sin(x * math.pi) for x in raw_signals])  # Unused in final logic
    entropy_proxy = -sum([x * math.log(x) for x in normalized if x > 0])

    # Real processing begins here — masked by prior noise
    binary_flags = [1 if x >= 0.7 else 0 for x in raw_signals]
    
    # Misleading intermediate aggregation
    avg_flag = sum(binary_flags) / len(binary_flags)  # Looks important, not used
    spike_count = sum(1 for x in raw_signals if x > 0.9)

    # Critical data structure: processing chain (used in answer)
    processing_chain = []
    for i, val in enumerate(raw_signals):
        record = {
            'id': i,
            'raw': val,
            'weight': math.log(val + 1) if val > 0 else 0,
            'category': 'high' if val >= 0.7 else 'low'
        }
        if val > 0.5:
            record['tier'] = 'A' if val > 0.8 else 'B'
        else:
            record['tier'] = 'C'
        processing_chain.append(record)
    
    # Dead code path — looks like it modifies chain but doesn't
    def inject_metadata(chain):
        for item in chain:
            item['checksum'] = (item['id'] + len(str(item['raw'])) ) % 7
        return chain  # never called

    # Threshold system with decoy values
    thresholds = {
        'critical': 0.9,
        'warning': 0.7,
        'info': 0.5,
        'decoy_key': entropy_proxy  # irrelevant
    }

    # Core diagnostic logic — depends only on tier B and C counts
    def aggregate_metrics(chain, limits):
        tier_b_count = 0
        tier_c_count = 0
        for entry in chain:
            if entry['tier'] == 'B':
                tier_b_count += 1
            elif entry['tier'] == 'C':
                tier_c_count += 1
        
        # Complex-looking but actually straightforward computation
        base_score = tier_b_count * 17
        penalty = tier_c_count * 5
        adjustment = 3 if len([r for r in chain if r['category'] == 'high']) > 4 else -2
        
        # Final result derived from multiple reasoning steps
        result = base_score - penalty + adjustment
        
        # Red herring: complicated modular arithmetic that doesn't affect anything
        debug_trace = (base_score * penalty + adjustment) % 97
        
        return result

    # Execution point of interest
    final_diagnostic = aggregate_metrics(processing_chain, thresholds)
    
    # Unused visualizations
    def plot_distribution(data):
        return ''.join(['*' * int(x*10) for x in data])
    
    # Output required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Trigger execution
result_value = monitor_system_health()
