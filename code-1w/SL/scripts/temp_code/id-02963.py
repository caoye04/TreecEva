def process_performance(data_str, extra):
    # Irrelevant string cleaning
    cleaned = data_str.strip().lower().replace(' ', '_')
    temp_hash = sum(ord(c) for c in cleaned[:5]) % 100
    
    # Misleading statistical distraction
    avg_ascii = sum(ord(c) for c in data_str) / len(data_str)
    deviation_pool = [abs(ord(c) - avg_ascii) for c in data_str]
    pseudo_entropy = sum(d ** 0.5 for d in deviation_pool[:3])

    # Core logic disguised among noise
    tokens = data_str.split(',')
    values = []
    for t in tokens:
        stripped = t.strip()
        if stripped.isdigit():
            values.append(int(stripped))
    
    # Secondary red herring: unused transformation
    shifted_vals = [v >> 1 for v in values if v > 5]
    filtered_sum = sum(v for v in values if v % 2 == 1)
    
    # Key computation interwoven with distractions
    base_score = sum(values) * 2
    adjustment = len(tokens) - len(values)  # penalty for non-digits
    raw_bonus = int(pseudo_entropy // 3) if pseudo_entropy > 10 else 0
    
    # Another dead-end variable
    temporal_weight = (temp_hash * extra) % 7
    
    # Final score depends only on specific derived values
    final_score = base_score + filtered_sum + raw_bonus
    return final_score

# Setup data with mixed content
raw_data = "12, 7, abc, 15, 3, x9y, 8"
bonus_multiplier = 3

# Execute main logic
target_result = process_performance(raw_data, bonus_multiplier)
print(f"Result: {target_result}")