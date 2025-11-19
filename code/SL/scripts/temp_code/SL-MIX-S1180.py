from collections import defaultdict
import math

def calculate_variance(weights):
    if len(weights) < 2:
        return 0
    mean = sum(weights) / len(weights)
    return sum((w - mean) ** 2 for w in weights) / (len(weights) - 1)

def get_batch_classification(weights):
    if not weights:
        return 'REJECTED'
    mean_weight = sum(weights) / len(weights)
    variance = calculate_variance(weights)
    
    # State machine logic
    if mean_weight >= 99.5 and mean_weight <= 100.5:
        if variance < 1.0:
            return 'ACCEPTED'
        else:
            return 'RETEST'
    else:
        return 'REJECTED'

# Batch data: batch_id -> list of pill weights
batch_data = {
    'BATCH_001': [99.8, 100.1, 99.9, 100.0, 100.2],
    'BATCH_002': [98.5, 98.7, 99.0, 98.8, 98.9],
    'BATCH_003': [100.2, 100.3, 99.9, 100.1, 100.0, 100.4],
    'BATCH_004': [101.0, 101.2, 100.8, 101.1],
    'BATCH_005': [99.9, 100.0, 100.1, 99.8, 100.2]
}

# Scoring system
score_map = {'ACCEPTED': 3, 'RETEST': 1, 'REJECTED': -2}
final_decision_score = 0

for batch_id, weights in batch_data.items():
    classification = get_batch_classification(weights)
    final_decision_score += score_map[classification]
    
    # Early return simulation for special case
    if batch_id == 'BATCH_003' and classification == 'ACCEPTED':
        final_decision_score += 2  # Bonus for perfect batch

print(f"Result: {final_decision_score}")