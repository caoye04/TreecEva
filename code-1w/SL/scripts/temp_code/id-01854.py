from itertools import compress, count

def analyze_text_data(text_blocks):
    char_count = sum(len(block) for block in text_blocks)
    upper_case_count = sum(1 for c in ''.join(text_blocks) if c.isupper())
    lower_case_count = sum(1 for c in ''.join(text_blocks) if c.islower())
    
    # Irrelevant statistical distraction
    avg_length = len(text_blocks) and char_count / len(text_blocks) or 0
    ratio = upper_case_count / lower_case_count if lower_case_count else 0

    # Distractor variables with plausible but unused computations
    entropy_approx = (upper_case_count + 1) * (lower_case_count + 1) % 997
    padding_offset = (char_count % 17) * 3

    return char_count, upper_case_count

def validate_entries(raw_values):
    filtered = []
    validation_log = []

    for val in raw_values:
        is_valid = isinstance(val, int) and val > 0
        validation_log.append(f'{val}:{"OK" if is_valid else "INVALID"}')
        if is_valid:
            filtered.append(val)
    
    # Dead code path - never accessed in normal flow
    if False:
        backup_result = [x * 2 for x in raw_values if isinstance(x, float)]
        return backup_result

    return filtered

def calculate_adjusted_sum(items, factor):
    base_total = sum(items)
    modifier = 0
    
    # Conditional expression used for subtle control
    modifier += 10 if len(items) > 5 else 5
    modifier -= 3 if any(x > 100 for x in items) else 0

    # Linear search embedded in logic
    has_outlier = False
    for x in items:
        if x > 200:
            has_outlier = True
            break
    
    modifier -= 7 if has_outlier else 0
    
    return int((base_total * factor) + modifier)

# Main execution sequence
blocks = ['Hello WORLD', 'PyThon Code', 'LLM EVALUATION']
counts = analyze_text_data(blocks)
raw_data = [12, -5, 30, 0, 45, 200, 88, 3]

valid_entries = validate_entries(raw_data)
adjustment_factor = 1.25

# Key statement
final_score = calculate_adjusted_sum(valid_entries, adjustment_factor)

Result: {final_score}