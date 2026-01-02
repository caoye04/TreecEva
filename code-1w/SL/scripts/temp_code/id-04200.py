from collections import defaultdict

def analyze_trend(data):
    trend_counter = defaultdict(int)
    prev = data[0]
    for curr in data[1:]:
        if curr > prev:
            trend_counter['up'] += 1
        elif curr < prev:
            trend_counter['down'] += 1
        else:
            trend_counter['flat'] += 1
        prev = curr
    return trend_counter

def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        avg = (signal[i-1] + signal[i] + signal[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(signal[-1])
    return smoothed

def calculate_performance(base, inputs):
    adjusted_inputs = [x - base for x in inputs]
    
    # Irrelevant transformation - distractor
    squared_offsets = [x**2 for x in adjusted_inputs if x > 0]
    total_offset = sum(adjusted_inputs)
    
    # Smoothing step that isn't used in final logic - red herring
    smoothed = smooth_signal(adjusted_inputs)
    
    trend_analysis = analyze_trend(adjusted_inputs)
    
    up_count = trend_analysis['up']
    down_count = trend_analysis['down']
    flat_count = trend_analysis['flat']
    
    # Dummy variables for distraction
    stability_index = flat_count * 0.5
    volatility_ratio = (up_count + down_count) / max(flat_count, 1)
    
    # Core logic hidden among distractions
    net_progression = up_count - down_count
    base_score = 100 if net_progression >= 0 else 80
    
    # Additional irrelevant calculation
    peak_deviation = max(adjusted_inputs) - min(adjusted_inputs) if adjusted_inputs else 0
    
    # Final score depends only on base_score and flat segments
    final_component = base_score + (flat_count * 2)
    
    return final_component

# Main execution
baseline = 75
readings = [70, 78, 85, 85, 90, 88, 88, 88, 95]

# Debugging block - not affecting result
if __name__ == "__main__":
    debug_mode = False
    if debug_mode:
        print("Debug: Starting analysis")

    intermediate_result = sum(readings) / len(readings)
    normalized = [round((r - baseline) * 0.1) for r in readings]
    
    # Enumerate and zip usage - semi-relevant but not critical
    indexed = list(enumerate(readings))
    shifted = [v - 5 for v in readings]
    paired = list(zip(indexed, shifted))
    
    # Conditional expression - affects nothing
    status = "active" if len(paired) > 5 else "idle"
    
    final_score = calculate_performance(baseline, readings)
    
    # Misleading secondary computation
    phantom_score = sum(normalized) * 3 if status == "active" else 0
    
    print(f"Result: {final_score}")