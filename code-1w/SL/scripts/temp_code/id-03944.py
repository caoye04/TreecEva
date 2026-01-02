from itertools import cycle

def analyze_phase_shift(elements, pivot):
    shift_count = 0
    temp_buffer = []
    for i, val in enumerate(elements):
        if val % 2 == 0:
            shifted = (val >> 1) ^ pivot
            temp_buffer.append(shifted)
            shift_count += 1
        else:
            temp_buffer.append(val | pivot)
    return temp_buffer, shift_count

def calculate_stabilization(metrics, limit):
    adjusted = []
    history = []
    accumulator = 0
    
    for idx, (a, b) in enumerate(zip(metrics[:-1], metrics[1:])):
        diff = abs(b - a)
        smoothed = (a + b) / 2
        
        # Distractor: irrelevant phase tracking
        phase_flag = True if idx % 3 == 0 else False
        if phase_flag:
            accumulator += diff
        
        if diff > limit:
            adjusted.append(smoothed * 1.1)
        else:
            adjusted.append(smoothed * 0.95)
    
    # Real logic branch
    for x in adjusted:
        if x < 50:
            history.append(x ** 0.5)
        elif x < 75:
            history.append(x * 0.8)
        else:
            history.append(x - 10)
    
    # Final computation
    total = sum(history)
    penalty = len([h for h in history if h > 60]) * 2.5
    final_score = total - penalty
    
    # Key red herring variables
    dummy_cycle = cycle([1, 2])
    sync_offset = sum(1 for _ in range(3)) * 0.7  # unused in final result
    
    return int(final_score)

# Main execution
raw_data = [120, 44, 68, 22, 91, 53, 88]
baseline = 25

# Irrelevant preprocessing
processed, count = analyze_phase_shift(raw_data, 7)
scaled_input = [p + 5 for p in processed if p > 10]

# Introduce misleading intermediate calculation
aggregate_peak = max(scaled_input) * len(scaled_input) // 2

# Core computation path
flow_metrics = [x - 3 for x in scaled_input]
threshold = baseline * 0.4

# Key statement
final_flux = calculate_stabilization(flow_metrics, threshold)

print(f"Result: {final_flux}")