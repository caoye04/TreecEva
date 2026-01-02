def analyze_metrics(data, threshold=10):
    filtered = [x for x in data if x > threshold]
    count_high = len(filtered)
    sum_squares = sum([x**2 for x in filtered])
    avg = sum(filtered) / count_high if count_high > 0 else 0
    return count_high, avg, sum_squares

metrics = [5, 12, 15, 8, 20, 3, 18, 9]

# Irrelevant auxiliary variable (minor distraction)
baseline = [x for x in metrics if x < 10]

# Core computation
count, mean_val, total_sq = analyze_metrics(metrics)

def calculate_performance(count, mean_val, total_sq):
    performance_map = {
        'efficiency': count * mean_val,
        'power': total_sq // (count + 1),
        'bonus': 10 if mean_val >= 15 else 5
    }
    # Use dictionary to compute final score
    base_score = performance_map['efficiency'] + performance_map['power']
    final_bonus = performance_map['bonus']
    return int(base_score + final_bonus)

final_score = calculate_performance(count, mean_val, total_sq)
print(f"Result: {final_score}")