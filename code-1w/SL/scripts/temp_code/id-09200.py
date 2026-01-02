def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    adjustment = 0.0

    # Preprocess: extract execution times and success rates
    times = [entry['time'] for entry in data]
    successes = [entry['success'] for entry in data]
    avg_time = sum(times) / len(times)
    success_rate = sum(successes) / len(successes)

    # Irrelevant statistical distraction
    variance = sum((t - avg_time) ** 2 for t in times) / len(times)
    std_deviation = variance ** 0.5

    # Performance core logic
    base_score = 100 * success_rate - (avg_time / 10)

    # Conditional bonus based on slicing top performers
    top_quartile = sorted(times)[:len(times)//4]
    if len(top_quartile) > 0:
        elite_speed = sum(top_quartile) / len(top_quartile)
        if elite_speed < 12:
            base_score += 10

    # Apply dynamic adjustment using conditional expression
    adjustment = 5 if success_rate >= 0.9 else (-3 if avg_time > 20 else 0)
    
    # Secondary irrelevant computation (dead-end path)
    hypothetical_gains = 0
    for i in range(len(data)):
        if data[i]['success'] and data[i]['time'] < 5:
            hypothetical_gains += 1.7
    # This gain is never used

    # Final score calculation with multiplier and penalty
    raw_final = base_score + adjustment
    final_score = raw_final * base_multiplier

    if success_rate < 0.7:
        final_score *= penalty_factor

    return int(final_score)

# Benchmark dataset
benchmark_data = [
    {'time': 15, 'success': True},
    {'time': 10, 'success': True},
    {'time': 25, 'success': False},
    {'time': 8, 'success': True},
    {'time': 12, 'success': True},
    {'time': 30, 'success': False},
    {'time': 11, 'success': True},
    {'time': 14, 'success': True}
]

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")