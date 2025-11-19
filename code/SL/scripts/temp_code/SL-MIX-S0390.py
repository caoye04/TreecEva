from math import log2

def compute_fragmentation_score(block_size, block_type):
    match block_type:
        case 'A':
            return (block_size << 2) ^ 0xF0
        case 'B':
            return (block_size >> 1) | 0x0F
        case 'C':
            return block_size & 0xAA
        case _:
            return block_size

def process_blocks(blocks):
    scores = []
    for size, btype in blocks:
        base_score = compute_fragmentation_score(size, btype)
        if base_score > 100:
            adjusted = base_score - (base_score % 10)
        else:
            adjusted = base_score + (10 - (base_score % 10))
        scores.append(adjusted)
    return scores

def calculate_final_score(scores):
    # Divide and conquer approach to sum scores
    if len(scores) == 1:
        return scores[0]
    mid = len(scores) // 2
    left_sum = calculate_final_score(scores[:mid])
    right_sum = calculate_final_score(scores[mid:])
    return left_sum + right_sum

# Data blocks: (size, type)
data_blocks = [
    (120, 'A'),
    (65, 'B'),
    (200, 'C'),
    (42, 'A'),
    (88, 'B')
]

processed_scores = process_blocks(data_blocks)
final_score = calculate_final_score(processed_scores)
print(f"Result: {final_score}")