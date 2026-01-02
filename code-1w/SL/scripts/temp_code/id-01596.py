from collections import defaultdict, Counter

# Simulate network packet analysis with performance scoring
def analyze_packets(packet_data):
    total_packets = len(packet_data)
    size_counter = Counter()
    timing_stats = defaultdict(int)
    error_flags = []

    valid_count = 0
    cumulative_delay = 0
    peak_magnitude = 0
    transient_value = 0

    for i, packet in enumerate(packet_data):
        size = len(packet['payload'])
        delay = packet['delay_ms']
        is_corrupted = packet['status'] == 'ERROR'

        size_counter[size] += 1
        timing_stats['max_delay'] = max(timing_stats['max_delay'], delay)
        timing_stats['total_delay'] += delay

        if delay > 50:
            timing_stats['jitter_count'] += 1

        if not is_corrupted and size > 4:
            valid_count += 1
            cumulative_delay += delay
            if delay > 30:
                transient_value += size * 0.5
        elif is_corrupted:
            error_flags.append(i)

    # Distractor calculations - not directly used in final score
    avg_size = sum(size_counter.elements()) / total_packets if total_packets else 0
    penalty_rate = len(error_flags) / total_packets if total_packets else 0
    base_efficiency = (valid_count / total_packets) * 100 if total_packets else 0

    # Critical path: performance metric based on constrained logic
    stability_factor = 1.0
    if timing_stats['jitter_count'] > total_packets * 0.3:
        stability_factor = 0.6
    elif timing_stats['max_delay'] > 80:
        stability_factor = 0.8

    # Secondary distractor: unused throughput estimate
    estimated_throughput = (sum(len(p['payload']) for p in packet_data) * 1000) // (timing_stats['total_delay'] + 1) if timing_stats['total_delay'] > 0 else 0

    # Core scoring logic
    raw_score = valid_count * 10 + (100 - timing_stats['max_delay'])
    adjusted_score = raw_score * stability_factor

    # Final interference: conditional adjustment based on rare condition
    if size_counter[8] >= 2 and timing_stats['jitter_count'] == 0:
        adjusted_score += 15

    # Key assignment point
    final_score = int(adjusted_score + transient_value - len(error_flags))

    # Irrelevant post-processing (dead-end computation)
    summary_report = {"packets": total_packets, "valid": valid_count, "errors": len(error_flags)}
    for k, v in summary_report.items():
        summary_report[k] = v * 2  # Unused transformation

    return final_score

# Generate deterministic input
packet_stream = [
    {'payload': 'data1', 'delay_ms': 20, 'status': 'OK'},
    {'payload': 'batch22', 'delay_ms': 60, 'status': 'OK'},
    {'payload': 'log3', 'delay_ms': 15, 'status': 'ERROR'},
    {'payload': 'event4', 'delay_ms': 90, 'status': 'OK'},
    {'payload': 'state555', 'delay_ms': 25, 'status': 'OK'},
    {'payload': 'config6666', 'delay_ms': 40, 'status': 'OK'},
    {'payload': 'meta777777', 'delay_ms': 70, 'status': 'ERROR'},
    {'payload': 'sync88888888', 'delay_ms': 35, 'status': 'OK'},
    {'payload': 'info9', 'delay_ms': 55, 'status': 'OK'},
    {'payload': 'sync88888888', 'delay_ms': 45, 'status': 'OK'}
]

result = analyze_packets(packet_stream)
final_score = result
print(f"Result: {final_score}")