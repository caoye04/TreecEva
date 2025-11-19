from collections import deque

def calculate_inspection_score(batch_id, stage_count):
    base_score = sum(ord(c) for c in str(batch_id))
    return base_score * stage_count + (base_score & 0xF)

def process_textile_batches():
    pending_inspections = []  # Stack for pending inspections
    completed_batches = deque()  # Queue for completed batches
    
    batch_data = [
        ('FAB001', 3),
        ('FAB002', 2),
        ('FAB003', 4),
        ('FAB004', 1)
    ]
    
    # Push all batches to pending inspections stack
    for batch_id, stages in batch_data:
        pending_inspections.append((batch_id, stages))
    
    # Process inspections
    while pending_inspections:
        batch_id, stages = pending_inspections.pop()
        score = calculate_inspection_score(batch_id, stages)
        completed_batches.append((batch_id, score))
    
    # Calculate final adjustment using bitwise operations
    aggregate_score = 0
    xor_accumulator = 0xFF
    
    while completed_batches:
        _, score = completed_batches.popleft()
        aggregate_score += score
        xor_accumulator ^= (score & 0xFF)
    
    # Final adjustment combines arithmetic and bitwise operations
    final_adjustment_score = (aggregate_score >> 2) + (xor_accumulator << 1)
    
    return final_adjustment_score

final_adjustment_score = process_textile_batches()
print(f"Result: {final_adjustment_score}")