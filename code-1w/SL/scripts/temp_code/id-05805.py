def calculate_inventory_score(items, thresholds):
    weights = [0.5, 1.0, 1.5, 2.0, 2.5]
    base_scores = [item['quantity'] * item['value'] for item in items]
    
    # Normalize scores using min-max scaling
    min_score = min(base_scores)
    max_score = max(base_scores)
    normalized_scores = [(s - min_score) / (max_score - min_score + 1e-8) for s in base_scores]
    
    # Apply threshold-based masking
    masked_scores = []
    for i, score in enumerate(normalized_scores):
        if base_scores[i] > thresholds[i % len(thresholds)]:
            masked_scores.append(score)
        else:
            masked_scores.append(0.0)
    
    # Slice only the top 4 contributing items
    relevant_scores = masked_scores[:4]
    
    # Scale each score by corresponding weight using zip
    scaled_weights = [score * w for score, w in zip(relevant_scores, weights)]
    
    # Irrelevant variable - distraction (minimal interference)
    avg_score = sum(base_scores) / len(base_scores) if base_scores else 0
    
    total_weight = sum(scaled_weights)
    return total_weight

# Input data
equipment = [
    {'name': 'sensor', 'quantity': 10, 'value': 8},
    {'name': 'actuator', 'quantity': 6, 'value': 15},
    {'name': 'controller', 'quantity': 4, 'value': 25},
    {'name': 'relay', 'quantity': 12, 'value': 6},
    {'name': 'transmitter', 'quantity': 7, 'value': 18}
]

thresholds = [90, 100, 85]

result = calculate_inventory_score(equipment, thresholds)
print(f"Target result: {result}")