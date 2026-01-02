def process_data(data, cfg):
    # Irrelevant preprocessing: reverse and slice (distractor)
    temp_slice = data[::-1][:len(data)//2]
    offset = sum(temp_slice) % 5

    # Semi-relevant transformation with conditional expression
    transformed = [x * 2 if x > cfg['threshold'] else x + 1 for x in data]

    # Destructuring assignment (tuple unpacking)
    a, b, *rest = transformed[:4]

    # Misleading accumulation that doesn't affect final result
    dummy_accum = 0
    for val in rest:
        dummy_accum += val * val

    # Real computation: uses dictionary lookup and slicing
    window = transformed[1:-1]
    shift = cfg.get('shift', 1)
    adjusted = [window[i] + shift * i for i in range(len(window))]

    # Conditional logic with short-circuit evaluation
    base_score = 10 if len(adjusted) >= 5 else 5
    bonus = 7 if all(x > 0 for x in adjusted) and len(adjusted) > 3 else 0

    # Final composite calculation
    total = sum(adjusted) + base_score + bonus

    # Secondary distraction: unused function call
    def noise_function(seq):
        return [seq[i] ^ seq[-i-1] for i in range(len(seq)//2)]
    
    # Another red herring: bitwise operation on config
    flag_check = (cfg['mode'] & 3) == 1 and (cfg['debug'] or False)

    # Actual output depends only on total and offset, but offset is fixed due to prior constraints
    final_value = total - offset
    return final_value

# Main execution
stream_buffer = [3, 7, 2, 8, 5, 6]
config = {
    'threshold': 4,
    'shift': 2,
    'mode': 3,
    'debug': False
}

# Dummy string manipulation (irrelevant)
log_tag = "DATA_STREAM"
log_parts = log_tag.lower().split('_')
identifier = ''.join([p[0] for p in log_parts])

# Unused nested loop (dead code path)
summary_stats = []
for i in range(2):
    row = []
    for j in range(3):
        row.append(i * j + len(log_parts))
    summary_stats.append(row)

# Key statement
final_output = process_data(stream_buffer, config)

print(f"Result: {final_output}")