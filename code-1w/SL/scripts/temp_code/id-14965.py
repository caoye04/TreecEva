def calculate_harmony(sequences):
    total_harmony = 0
    for idx, seq in enumerate(sequences):
        if len(seq) % 2 == 0:
            adjustment = 1
        else:
            adjustment = -1
        
        # Irrelevant tracking (low interference)
        step_log = f'Processing sequence {idx}'
        
        char_sum = sum(ord(c) for c in seq)
        position_factor = idx + 1
        
        # Core harmony calculation
        sequence_score = char_sum * position_factor * adjustment
        total_harmony += sequence_score
    
    return total_harmony

# Additional irrelevant variable (minimal distraction)
baseline_reference = 42

sequences = ['ai', 'model', 'eval', 'test']
total_harmony = calculate_harmony(sequences)
print(f"Result: {total_harmony}")