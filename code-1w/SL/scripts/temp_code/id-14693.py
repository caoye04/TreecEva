def analyze_trend(data, base):
    trend = 0
    offset = len(data) // 2
    temp_sum = sum(data[:offset])  # Irrelevant computation
    for i in range(len(data)):
        if data[i] > base:
            trend += (i + 1) * data[i]
    return trend

initial_weights = [3, 1, 4, 1, 5, 9, 2]
dummy_calc = sum(x ** 2 for x in initial_weights if x % 2 == 0)
adjusted = [w * 1.5 for w in initial_weights]

# Simulate sensor metrics over time
data_stream = [12, 15, 10, 18, 14]
baseline = 13
raw_trend = analyze_trend(data_stream, baseline)

# Performance metrics from system logs
metrics = [85, 90, 78, 92, 88]
threshold = 80

# Secondary distraction: simulate packet loss rates
packet_data = [0.01, 0.03, 0.02, 0.05]
avg_loss = sum(packet_data) / len(packet_data)
projection = [p * 1000 for p in packet_data if p > 0.02]

# Core logic with slicing and conditional expressions
slice_window = metrics[1:4]
boosted = [val * 1.1 if val < threshold else val * 1.05 for val in slice_window]

def process_performance(scores, limit):
    count_above = len([s for s in scores if s >= limit])
    adjustment = 0.95 if count_above >= 3 else 0.90
    
    # Extra distraction: unused helper logic
    def normalize(val, min_val=70, max_val=100):
        return (val - min_val) / (max_val - min_val)
    
    filtered = scores[::2]  # Every other score
    temp_avg = sum(filtered) / len(filtered)
    
    # Main calculation
    raw_score = sum(boosted)  # Uses outer scope variable
    penalty = 5 if raw_trend < 30 else 10
    final = raw_score - penalty + (temp_avg * 0.1)
    
    return int(final)  # Deterministic integer result

final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")