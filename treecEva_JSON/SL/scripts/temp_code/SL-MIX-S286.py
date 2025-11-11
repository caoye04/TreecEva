from collections import deque
import statistics

def process_sensor_data():
    # Initialize data structures
    signal_queue = deque([12, 8, 15, 22, 5, 18, 9])
    result_stack = []
    
    # Process signals while queue is not empty
    while signal_queue:
        current_signal = signal_queue.popleft()
        
        # Apply logical filtering conditions
        if (current_signal > 10 and current_signal % 2 == 0) or (current_signal < 7 and not signal_queue):
            # Calculate statistical adjustment factor
            sample_window = [x for x in [current_signal, current_signal*0.5, current_signal*1.5] if x > 6]
            adjustment_factor = statistics.mean(sample_window) if sample_window else 0
            
            # Apply nested logical condition
            if adjustment_factor > 10 or (adjustment_factor > 5 and len(result_stack) >= 2):
                transformed_value = int(adjustment_factor) & 0xF  # Bitwise AND with 15
                result_stack.append(transformed_value)
            else:
                result_stack.append(int(adjustment_factor) | 0x3)  # Bitwise OR with 3
        
        # Special handling for middle values
        elif 7 <= current_signal <= 15:
            # Create dictionary mapping using comprehension
            signal_map = {i: val for i, val in enumerate([current_signal, current_signal+1, current_signal-1])}
            merged_map = {**signal_map, **{3: statistics.variance(signal_map.values())}}
            result_stack.append(int(merged_map[3]))
    
    # Calculate final metric from stack
    valid_results = [x for x in result_stack if x > 0 and (x % 2 == 1 or x > 10)]
    final_metric = sum(valid_results) ^ 0xA  # XOR with 10
    return final_metric

final_metric = process_sensor_data()
print(f"Result: {final_metric}")