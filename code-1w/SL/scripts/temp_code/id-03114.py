def normalize(data):
    return round(sum(data) / len(data), 3) if data else 0

def process_records(values):
    threshold = 75
    index = 0
    for i, val in enumerate(values):
        if val > threshold:
            index = i
            break
    
    scores = [82, 67, 91, 73, 88, 76]
    base_factor = 1.5
    adjustment = 0.8
    multiplier = base_factor * adjustment
    
    final_score = normalize(scores[:index]) * multiplier
    
    temp = [x for x in values if x % 2 == 0]  # irrelevant filtering
    count_even = len(temp)
    
    return final_score

result = process_records([60, 70, 80, 95])
print(f"Target result: {result}")