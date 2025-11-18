from enum import Enum
from collections import namedtuple
from functools import reduce
import itertools

class BatchState(Enum):
    RECEIVED = 1
    SPUN = 2
    WOVEN = 3
    DYED = 4
    FINISHED = 5

Batch = namedtuple('Batch', ['id', 'state', 'quality_base'])

# Initial batch data
batches = [
    Batch(101, BatchState.RECEIVED, 85),
    Batch(102, BatchState.RECEIVED, 92),
    Batch(103, BatchState.RECEIVED, 78)
]

# Quality multipliers for each stage
multipliers = {
    BatchState.RECEIVED: 1.0,
    BatchState.SPUN: 1.1,
    BatchState.WOVEN: 1.25,
    BatchState.DYED: 1.15,
    BatchState.FINISHED: 1.3
}

# Process all batches through state machine until finished
final_quality_score = 0
for i in range(len(batches)):
    current_batch = batches[i]
    while current_batch.state != BatchState.FINISHED:
        # Apply multiplier for current state
        stage_quality = current_batch.quality_base * multipliers[current_batch.state]
        
        # State transition with switch-case logic
        if current_batch.state == BatchState.RECEIVED:
            next_state = BatchState.SPUN
        elif current_batch.state == BatchState.SPUN:
            next_state = BatchState.WOVEN
        elif current_batch.state == BatchState.WOVEN:
            next_state = BatchState.DYED
        elif current_batch.state == BatchState.DYED:
            next_state = BatchState.FINISHED
        else:
            break
            
        # Update batch with new state
        current_batch = Batch(current_batch.id, next_state, current_batch.quality_base)
    
    # Add final stage quality to cumulative score
    final_quality_score += current_batch.quality_base * multipliers[current_batch.state]

# Apply sorting and search for verification (not affecting final result but part of process)
batch_ids = sorted([b.id for b in batches])
search_target = 102
found_index = -1
low, high = 0, len(batch_ids) - 1
while low <= high:
    mid = (low + high) // 2
    if batch_ids[mid] == search_target:
        found_index = mid
        break
    elif batch_ids[mid] < search_target:
        low = mid + 1
    else:
        high = mid - 1

# Final adjustment based on search result
if found_index >= 0:
    final_quality_score = round(final_quality_score)
else:
    final_quality_score = int(final_quality_score)

print(f"Result: {final_quality_score}")