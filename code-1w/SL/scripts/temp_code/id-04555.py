def calculate_performance(data, threshold=5.0):
    avg = sum(data) / len(data)
    above_threshold = [x for x in data if x > threshold]
    bonus = len(above_threshold) * 0.5 if avg >= 4.0 else -1.0
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_debug_log = f'Processing {len(data)} entries'
    
    adjustment = 2.0 if avg >= 4.5 else (1.0 if avg >= 3.5 else 0.0)
    return avg + bonus + adjustment

# Main execution
data_stream = [4.2, 5.1, 3.8, 6.3, 4.7]
base_metric = sum(data_stream[:3]) / 3
is_stable = base_metric > 4.0 and len(data_stream) % 2 == 1

final_score = calculate_performance(data_stream) if is_stable else -999
print(f"Result: {final_score}")