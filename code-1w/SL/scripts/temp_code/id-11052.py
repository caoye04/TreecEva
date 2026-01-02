def calculate_performance(data):
    weights = [0.2, 0.3, 0.5]
    adjusted = []
    
    for i, (value, flag) in enumerate(data):
        if flag:
            adjusted.append(value * weights[i])
    
    temp_sum = sum(adjusted)
    scaling_factor = 1.1
    final_score = int(temp_sum * scaling_factor)
    
    # Irrelevant auxiliary variable (minimal distraction)
    debug_info = f'Processed {len(data)} entries'
    
    return final_score

# Main data input
benchmark_data = [(85, True), (90, True), (78, True)]
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")