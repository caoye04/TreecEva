import itertools

def analyze_pattern(sequence):
    even_count = sum(1 for x in sequence if x % 2 == 0)
    odd_count = len(sequence) - even_count
    ratio = even_count / odd_count if odd_count != 0 else 0
    return ratio > 1.5

def filter_noise(data, limit):
    filtered = [x for x in data if x > limit]
    temp_sum = sum(x ** 0.5 for x in filtered if x < 50)  # Distractor: not used later
    return filtered if len(filtered) > 3 else [0]

def validate_stability(readings):
    diffs = [abs(a - b) for a, b in zip(readings, readings[1:])]
    stable = all(d < 10 for d in diffs)
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    spike_count = len([d for d in diffs if d > 8])
    return stable and spike_count <= 2

def process_signals(raw_input, threshold):
    # Step 1: Initial filtering
    cleaned = filter_noise(raw_input, threshold)
    
    # Step 2: Generate sliding windows of size 3 using itertools
    windows = list(itertools.windowed(cleaned, n=3))
    valid_windows = [w for w in windows if sum(w) > 20 and min(w) > threshold]
    
    # Step 3: Pattern analysis on first valid window (if exists)
    if valid_windows:
        primary_window = valid_windows[0]
        has_even_dominance = analyze_pattern(primary_window)
    else:
        has_even_dominance = False
    
    # Step 4: Stability check on original signal (modified by condition)
    adjusted_signal = [x - 5 for x in raw_input if x % 3 == 1]  # Semi-relevant transformation
    stable = validate_stability(adjusted_signal)
    
    # Step 5: Conditional logic with expression
    base_score = 42 if has_even_dominance and stable else 18
    
    # Step 6: Final adjustment based on length and sum
    length_factor = len(valid_windows) * 2
    sum_bonus = sum(valid_windows[0]) if valid_windows else 0
    final_output = base_score + length_factor + (sum_bonus // 10 if valid_windows else 0)
    
    # Irrelevant computations (distraction)
    _ = [x * x for x in range(len(raw_input))]  # Dead computation
    dummy_counter = 0
    for i in range(100):
        dummy_counter += i % 7
    
    return final_output

# Main execution
signal_data = [12, 15, 24, 8, 33, 41, 6, 19]
detection_threshold = 10
final_output = process_signals(signal_data, detection_threshold)
print(f"Target result: {final_output}")