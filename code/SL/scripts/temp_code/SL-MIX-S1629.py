from collections import deque

def process_batch(stages_stack, initial_score):
    scores_queue = deque([initial_score])
    adjustment_func = lambda x, y: (x * 2 + y) // 3 if x > y else (y - x) * 2
    
    while stages_stack:
        stage = stages_stack.pop()
        current_score = scores_queue[-1]
        
        if stage == 'tensile':
            adjusted = adjustment_func(current_score, 7)
            scores_queue.append(adjusted)
        elif stage == 'colorfast':
            transformed = ''.join(chr((ord(c) - ord('a') + 3) % 26 + ord('a')) for c in str(current_score))
            numeric_transform = sum(ord(ch) for ch in transformed)
            scores_queue.append(numeric_transform % 100)
        elif stage == 'weave':
            fib_a, fib_b = 1, 1
            for _ in range(current_score % 10 + 1):
                fib_a, fib_b = fib_b, fib_a + fib_b
            scores_queue.append(fib_a)
        else:
            scores_queue.append(current_score + 5)
    
    return scores_queue[-1]

def calculate_quality_metric(batch_data):
    processing_stages = ['tensile', 'colorfast', 'weave', 'finish']
    stage_stack = processing_stages[::-1]  # Reverse to simulate stack behavior
    initial_rating = batch_data['base_score']
    
    with open('temp_log.txt', 'w') as f:
        f.write(f"Processing batch {batch_data['batch_id']}\n")
    
    final_metric = process_batch(stage_stack, initial_rating)
    
    # Apply final adjustment based on batch metadata
    if batch_data['material_type'] == 'synthetic':
        final_metric *= 2
    elif batch_data['material_type'] == 'natural':
        final_metric += 15
    
    return final_metric

batch_info = {
    'batch_id': 'TEX2024BQ9',
    'base_score': 23,
    'material_type': 'synthetic',
    'production_date': '2024-03-15'
}

final_metric = calculate_quality_metric(batch_info)
print(f"Result: {final_metric}")