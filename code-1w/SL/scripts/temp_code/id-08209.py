def analyze_trends(data_slice, threshold=0.5):
    trend_count = 0
    temp_buffer = []
    for i in range(1, len(data_slice)):
        if data_slice[i] > data_slice[i-1]:
            trend_count += 1
            temp_buffer.append(data_slice[i])
    return trend_count

# Simulate sensor drift compensation (distractor logic)
def correct_drift(signal):
    adjusted = [x * 0.98 for x in signal]
    baseline = sum(adjusted[:5]) / 5
    return [x - baseline for x in adjusted]

# Core performance calculation
def calculate_performance(raw_series):
    # Extract critical phase using slicing
    activation_window = raw_series[10:30]
    
    # Distractor: irrelevant transformation
    normalized = [x / max(activation_window) for x in activation_window]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    
    # Key metric: volatility-adjusted trend score
    volatility = 0
    for i in range(1, len(activation_window)):
        volatility += abs(activation_window[i] - activation_window[i-1])
    
    # Secondary distractor: unused frequency analysis
    freq_analysis = {}
    for val in activation_window:
        rounded = round(val)
        freq_analysis[rounded] = freq_analysis.get(rounded, 0) + 1
    
    # Real computation path
    trend_strength = analyze_trends(activation_window)
    avg_magnitude = sum(activation_window) / len(activation_window)
    
    # Final formula
    adjustment_factor = 1.0 if volatility > 15 else 0.8
    final_score = int((trend_strength * avg_magnitude * adjustment_factor) + 42)
    
    return final_score

# Input data generation (realistic pattern)
base_sequence = []
for t in range(25):
    val = 3 * (t / 5) + 1.5 * (t % 3) + 0.8 * (t // 4)
    base_sequence.append(round(val, 2))

# Apply correction (distractor call - doesn't affect final input)
corrected_signal = correct_drift(base_sequence)

# Actual benchmark data used
benchmark_data = [round(x * 1.1, 2) for x in base_sequence]

# Main execution point
temp_var = benchmark_data[::-1]  # Reverse slice - distractor usage
summary_stats = {"length": len(benchmark_data), "peak": max(benchmark_data)}
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")