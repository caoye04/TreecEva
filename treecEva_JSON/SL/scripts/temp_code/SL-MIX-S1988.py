from collections import defaultdict
import statistics

def process_signal(amplitude_data):
    # Initialize data structures
    raw_signals = defaultdict(float)
    smoothed_signals = {}
    
    # Populate raw signals
    for time_idx, amplitude in enumerate(amplitude_data):
        raw_signals[time_idx] = float(amplitude)
    
    # Apply moving average smoothing with window size 3
    for t in range(len(amplitude_data)):
        if t == 0:
            window_values = [raw_signals[t], raw_signals[t+1], raw_signals[t+2]]
        elif t == len(amplitude_data) - 1:
            window_values = [raw_signals[t-2], raw_signals[t-1], raw_signals[t]]
        else:
            window_values = [raw_signals[t-1], raw_signals[t], raw_signals[t+1]]
        smoothed_signals[t] = sum(window_values) / len(window_values)
    
    # Calculate variance of smoothed signal
    signal_values = [smoothed_signals[key] for key in sorted(smoothed_signals.keys())]
    final_variance = statistics.variance(signal_values)
    return final_variance

# Input data representing amplitude measurements over time
input_amplitudes = [10, 15, 20, 25, 30, 35, 40]
final_variance = process_signal(input_amplitudes)
print(f"Result: {final_variance}")