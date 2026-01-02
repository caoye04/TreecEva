def evaluate_performance(log_entries, baseline):
    # Irrelevant counters (distractors)
    temp_sum = 0
    dummy_counter = 0
    placeholder_value = 1
    for entry in log_entries:
        if len(entry) > 5:
            temp_sum += len(entry) % 3
        dummy_counter += 1  # Dead computation

    # Real logic begins: analyze performance metrics
    valid_records = []
    for record in log_entries:
        stripped = record.strip().lower()
        if 'error' not in stripped and 'fail' not in stripped:
            valid_records.append(stripped)
    
    # Character frequency analysis (partially relevant)
    char_freq = {}
    for record in valid_records:
        for char in record:
            if char.isalpha():
                char_freq[char] = char_freq.get(char, 0) + 1
    
    # Extract top character (red herring - not used later)
    top_char = None
    if char_freq:
        top_char = max(char_freq, key=char_freq.get)

    # Actual metric calculation
    total_length = sum(len(r) for r in valid_records)
    avg_length = total_length / len(valid_records) if valid_records else 0

    # Bit manipulation on baseline (key operation)
    transformed_base = baseline ^ 0b101010  # XOR with magic number
    adjusted_base = transformed_base << 2  # Shift left by 2

    # Conditional expression based on string pattern
    bonus = 100 if any(r.endswith('success') for r in valid_records) else 0

    # Early termination red herring (never triggered due to data)
    if len(valid_records) == 0:
        return -1  # Dead path

    # Core formula: combines arithmetic, bit ops, and conditional
    raw_score = (avg_length * 7.3) + (adjusted_base % 89)
    
    # Multiple assignment distraction
    multiplier, offset, _ = (1.05, 17, 'unused_string')
    
    # Destructuring decoy
    info_tuple = (raw_score, bonus, placeholder_value)
    a, b, c = info_tuple

    # Final computation chain
    intermediate = (a + b) * multiplier
    final_score = int(intermediate + offset)

    # Decoy print that looks important
    debug_info = f"Final state: {final_score}, Top char: {top_char}"

    return final_score

# Setup input data
log_entries = [
    "System initialized successfully",      # valid, ends with success
    "  Data fetch complete  ",              # valid
    "WARNING: retry attempt 1",             # valid
    "error_code_404",                       # invalid
    "Operation succeeded in 2.1s",          # valid, ends with success
    "",                                     # invalid
    "retry_successful"                    # valid, ends with success
]
baseline = 42

# Execute main logic
final_score = evaluate_performance(log_entries, baseline)
print(f"Result: {final_score}")