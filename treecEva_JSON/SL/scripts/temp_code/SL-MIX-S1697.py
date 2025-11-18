from collections import defaultdict
import math

class ListNode:
    def __init__(self, defect_type, count=0, next=None):
        self.defect_type = defect_type
        self.count = count
        self.next = next

def defect_monitor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def create_defect_log(entries):
    head = None
    for entry in reversed(entries):
        head = ListNode(entry[0], entry[1], head)
    return head

@defect_monitor
def process_logs(log_heads):
    defect_counter = defaultdict(int)
    total_products = 0
    
    for head in log_heads:
        current = head
        while current:
            defect_counter[current.defect_type] += current.count
            total_products += current.count
            current = current.next
    
    severity_weights = {'A': 5, 'B': 3, 'C': 1}
    weighted_sum = 0
    
    for defect_type, count in defect_counter.items():
        if defect_type in severity_weights:
            weighted_sum += count * severity_weights[defect_type]
    
    # Nested loop to simulate quality adjustments
    adjustment_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    adjustment_factor = 0
    
    for i in range(len(adjustment_matrix)):
        row_sum = 0
        for j in range(len(adjustment_matrix[i])):
            if i*j < len(defect_counter):
                row_sum += adjustment_matrix[i][j]
        adjustment_factor += row_sum
    
    # Calculate final score
    if total_products > 0:
        base_score = (total_products * 100 - weighted_sum) / total_products
        final_score = base_score + (adjustment_factor / 10)
    else:
        final_score = 100
    
    return final_score

# Create defect logs for three product lines
log1_entries = [('A', 2), ('B', 5), ('C', 10)]
log2_entries = [('A', 1), ('B', 3), ('C', 7)]
log3_entries = [('A', 3), ('B', 2), ('C', 5)]

log1 = create_defect_log(log1_entries)
log2 = create_defect_log(log2_entries)
log3 = create_defect_log(log3_entries)

logs = [log1, log2, log3]
final_score = process_logs(logs)
print(f"Result: {final_score}")