from collections import defaultdict, Counter

# Simulate system benchmark data with noise
def generate_noisy_data():
    raw_inputs = [12, 15, 12, 18, 15, 22, 25, 18, 30, 22, 12]
    noise_offsets = [i % 3 for i in range(len(raw_inputs))]
    return [raw_inputs[i] + noise_offsets[i] for i in range(len(raw_inputs))]

def analyze_trends(data):
    trend_counter = defaultdict(int)
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_counter['increasing'] += 1
        elif data[i] < data[i-1]:
            trend_counter['decreasing'] += 1
        else:
            trend_counter['stable'] += 1
    return trend_counter

def calculate_stability_index(data):
    # Irrelevant helper function for distraction
    frequencies = Counter(data)
    unique_count = len(frequencies)
    total = len(data)
    return round(unique_count / total, 4) if total else 0

def calculate_performance(metrics):
    base_points = sum(metrics)
    adjustments = 0
    
    # Misleading intermediate calculations
    temp_analysis = analyze_trends(metrics)
    stability = calculate_stability_index(metrics)
    
    if temp_analysis['increasing'] > temp_analysis['decreasing']:
        adjustments += 5
    
    # Real logic: count how many values are above threshold and appear at least twice
    freq_map = Counter(metrics)
    high_freq_high_val = [k for k, v in freq_map.items() if k > 15 and v >= 2]
    bonus_points = len(high_freq_high_val) * 3
    
    # Distractor variables
    avg_value = sum(metrics) / len(metrics) if metrics else 0
    peak_value = max(metrics) if metrics else 0
    normalized_score = (base_points + adjustments) * 0.1
    
    # Final score depends only on base_points, adjustments, and bonus_points
    final_score = base_points + adjustments + bonus_points
    
    # Dead code path - never executed but adds cognitive load
    if stability > 1.0:
        final_score -= 10
        
    return final_score

# Main execution
benchmark_data = generate_noisy_data()
interim_stats = analyze_trends(benchmark_data)
dummy_check = [x for x in benchmark_data if x % 2 == 0]  # unused list comprehension
total_sum = sum(benchmark_data)
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")