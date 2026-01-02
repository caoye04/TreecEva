def analyze_soil_composition(data):
    # Irrelevant analysis with decoy computations
    ph_levels = [7.1, 6.9, 7.3, 6.8, 7.0]
    nutrient_score = sum((x - 7.0) ** 2 for x in ph_levels) * 100
    texture_analysis = {k: v * 1.5 for k, v in enumerate([3, 5, 4])}
    return nutrient_score  # Dead-end return, not used


def preprocess_field_blocks(raw_blocks):
    # Real preprocessing with embedded distractions
    filtered = [b for b in raw_blocks if sum(b) > 25]
    normalized = [[val / max(block) * 100 for val in block] for block in filtered]
    
    # Distractor: unused transformation
    inverted = [[100 - x for x in row] for row in normalized if len(row) == 4]
    
    stats_summary = {
        'count': len(normalized),
        'max_row': max(normalized, key=sum),
        'threshold_met': all(sum(row) > 150 for row in normalized)
    }
    
    # Conditional expression used
    processed = [row for row in normalized if stats_summary['count'] > 1]
    return processed


def calculate_irrigation_efficiency(blocks):
    # Red herring function: looks important but doesn't affect final result
    efficiency = 0
    for i, block in enumerate(blocks):
        if i % 2 == 0:
            efficiency += sum(block) * 0.1
        else:
            efficiency -= sum(block) * 0.05
    return round(efficiency, 4)


def bit_manipulate_sequence(seq):
    # Bit manipulation distractor
    transformed = []
    for num in seq:
        shifted = (num << 2) ^ 0b1010
        transformed.append(shifted & 255)
    return transformed


def optimize_harvest(blocks):
    # Core logic hidden among noise
    base_yield = 0
    adjustment_factor = 1.0
    
    for block in blocks:
        block_sum = sum(block)
        
        # Real conditional affecting result
        if block_sum > 200:
            adjustment_factor *= 1.1
        elif block_sum < 180:
            adjustment_factor *= 0.95

        # Accumulate actual yield contribution
        base_yield += block_sum * adjustment_factor
    
    # Final adjustment using set operation (core concept)
    unique_sums = set(int(sum(b)) for b in blocks)
    bonus_multiplier = 1.05 if len(unique_sums & {200, 210, 220}) > 0 else 1.0
    
    return int(base_yield * bonus_multiplier)

# Main execution with decoys
if __name__ == '__main__':
    field_data = [
        [45, 50, 60, 40],
        [55, 55, 58, 45],
        [60, 62, 50, 53],
        [48, 52, 55, 47]
    ]

    # Irrelevant preprocessing chain
    _ = analyze_soil_composition(field_data)
    
    # Critical data transformation
    processed_blocks = preprocess_field_blocks(field_data)
    
    # Distractor calls
    _irr_eff = calculate_irrigation_efficiency(processed_blocks)
    _bit_seq = bit_manipulate_sequence([sum(b)//10 for b in processed_blocks])
    
    # Key statement
    final_yield = optimize_harvest(processed_blocks)
    
    # Print target result
    print(f"Target result: {final_yield}")