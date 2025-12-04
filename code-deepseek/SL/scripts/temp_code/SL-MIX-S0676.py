from collections import Counter

def process_operations(data_items):
    temp_analysis = Counter(data_items)
    intermediate_sum = sum(data_items)
    unused_computation = len(data_items) * 3.14
    
    filter_threshold = 15
    filtered_count = sum(1 for item in data_items if item > filter_threshold)
    redundant_check = max(data_items) - min(data_items)
    
    target_items = [item for item in data_items if item % 2 == 0]
    final_count = len(target_items) + filtered_count
    
    return final_count

data_items = [12, 8, 25, 6, 18, 30, 7, 22, 14, 9]
result = process_operations(data_items)
print(f"Target result: {result}")