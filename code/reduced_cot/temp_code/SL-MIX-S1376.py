from collections import defaultdict
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def calculate_batch_score(measurements):
    if not measurements:
        return 0
    mean_val = sum(measurements) / len(measurements)
    variance = sum((x - mean_val) ** 2 for x in measurements) / len(measurements)
    return int(mean_val * 100 + variance * 10)

class BatchProcessor:
    def __init__(self):
        self.state = 'IDLE'
        self.total_score = 0
        self.batches_processed = 0
        
    def process_batch(self, measurements):
        score = calculate_batch_score(measurements)
        # State machine transitions
        if self.state == 'IDLE' and score > 500:
            self.state = 'HIGH_QUALITY'
        elif self.state == 'IDLE' and score <= 500:
            self.state = 'REWORK_NEEDED'
        elif self.state == 'HIGH_QUALITY' and score < 400:
            self.state = 'QUALITY_DROP'
        elif self.state == 'REWORK_NEEDED' and score > 600:
            self.state = 'RECOVERED'
        
        self.total_score += score
        self.batches_processed += 1
        return score

# Production parameters
batch_measurements = [
    [12.5, 13.2, 12.8, 13.0, 12.9],  # Batch 1
    [15.1, 14.8, 15.3, 14.9, 15.2],  # Batch 2
    [10.2, 10.1, 10.3, 10.0, 10.4],  # Batch 3
    [18.7, 19.2, 18.9, 19.0, 18.8],  # Batch 4
    [11.5, 11.8, 11.3, 11.7, 11.6],  # Batch 5
    [20.1, 19.8, 20.3, 19.9, 20.2],  # Batch 6
]

# Calculate target threshold using LCM of first three batch scores
initial_scores = [calculate_batch_score(batch) for batch in batch_measurements[:3]]
target_threshold = reduce(lcm, initial_scores) % 1000

processor = BatchProcessor()
final_batch_count = 0

# Process batches until target is reached
i = 0
while processor.total_score < target_threshold and i < len(batch_measurements):
    current_score = processor.process_batch(batch_measurements[i])
    # Short-circuit evaluation for special condition
    if processor.state == 'HIGH_QUALITY' and current_score > 700:
        processor.total_score += 100  # Bonus points
    i += 1
    
final_batch_count = processor.batches_processed

print(f"Result: {final_batch_count}")