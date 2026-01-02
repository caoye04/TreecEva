from collections import defaultdict

# Simulate a network packet processing system with efficiency metrics
def main():
    packet_sizes = [128, 256, 512, 64, 1024, 32, 192]
    transfer_rates = [8.5, 17.2, 33.8, 4.1, 67.3, 2.0, 14.6]
    latency_ms = [12, 25, 18, 30, 45, 50, 22]

    # Irrelevant statistic tracking (distractor)
    stats_tracker = defaultdict(int)
    for rate in transfer_rates:
        stats_tracker['total_bandwidth'] += rate
        if rate > 20:
            stats_tracker['high_perf_count'] += 1

    # Misleading preprocessing (does not affect final result)
    normalized_sizes = []
    max_size = max(packet_sizes)
    for size in packet_sizes:
        norm = (size / max_size) * 100
        normalized_sizes.append(round(norm))

    # Core data for calculation
    operations = sum([size * 2 for size in packet_sizes if size >= 128])
    overhead = sum([int(latency / 5) for latency in latency_ms])

    # Secondary computation path (unused, distractor)
    lambda_transform = lambda x: x ** 0.5 if x > 10 else x
    temp_result = [lambda_transform(rate) for rate in transfer_rates]
    avg_temp = sum(temp_result) / len(temp_result)

    # Conditional adjustment based on arbitrary threshold (semi-relevant but overridden)
    if avg_temp > 5:
        overhead += 10
    else:
        overhead -= 5

    # Reset overhead to original path (this makes previous block misleading)
    overhead = sum([int(latency / 5) for latency in latency_ms])  # Recompute

    def calculate_efficiency(op_count, overhead):
        base_efficiency = op_count / (overhead + 1)
        penalty_factor = 0.95 if op_count > 2000 else 1.0
        return int(base_efficiency * penalty_factor)

    # Key statement
    efficiency_score = calculate_efficiency(operations, overhead)

    # Dead code branch (never executed, distractor)
    if False:
        fallback = sum(normalized_sizes) // len(normalized_sizes)
        efficiency_score = fallback

    # Print final result as required
    print(f"Result: {efficiency_score}")

    return efficiency_score

if __name__ == "__main__":
    main()