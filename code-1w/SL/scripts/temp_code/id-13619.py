from collections import defaultdict
import math

def analyze_fragmentation(blocks):
    # Irrelevant helper function: analyzes block fragmentation but not used in final result
    frag_score = 0
    for size in blocks:
        if size < 8:
            frag_score += 1
    return frag_score

def validate_allocation(allocation):
    # Semi-relevant validation that modifies state but doesn't affect core logic
    if sum(allocation) > 1000:
        return False
    threshold = 50
    adjusted = [x for x in allocation if x > threshold]
    return len(adjusted) > 3

def calculate_remaining_capacity(storage, log_list):
    total_capacity = 500
    reserved = 42  # Fixed reservation
    usage_tracker = defaultdict(int)
    
    temp_buffer = []
    for entry in log_list:
        usage_tracker[entry] += 1
        temp_buffer.append(entry * 0.1)  # Distractor: buffer never used
    
    # Core logic: count unique large allocations
    large_allocs = 0
    for val in log_list:
        if val > 75:
            large_allocs += 1
    
    # Secondary distraction: unnecessary string processing
    status_msg = "Allocation verified"
    char_count = len(status_msg.replace(" ", ""))
    dummy_score = math.ceil(char_count / 3)
    
    # Real computation chain
    base_usage = sum(log_list)
    if base_usage > total_capacity:
        base_usage = total_capacity * 0.9  # Cap usage
    
    adjusted_usage = base_usage - (reserved * 0.5)
    efficiency_ratio = (adjusted_usage / total_capacity) if total_capacity else 0
    
    # Final determination
    if efficiency_ratio > 0.7 and large_allocs >= 2:
        final_capacity = int(total_capacity - adjusted_usage - (dummy_score * 0))
    else:
        final_capacity = int(total_capacity * 0.4)
    
    return final_capacity

# Simulated system state
storage_map = defaultdict(lambda: 0, {"A": 100, "B": 200, "C": 150})
allocation_log = [80, 60, 90, 40, 70]  # Five allocation events

# Dead code path: never executed but present for distraction
if __name__ == "__main__":
    debug_mode = True
    if debug_mode:
        print("Debug: System initializing...")

# Key execution point
final_capacity = calculate_remaining_capacity(storage_map, allocation_log)

# Print result as required
print(f"Result: {final_capacity}")