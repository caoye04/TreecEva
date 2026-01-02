def analyze_data_stream():
    raw_samples = [18, 23, 45, 67, 89, 12, 34, 56, 78, 91]
    sample_flags = [True, False, True, False, True, True, False, True, False, True]
    
    # Preprocessing: categorize by parity and magnitude
    even_count = 0
    large_values = set()
    for x in raw_samples:
        if x % 2 == 0:
            even_count += 1
        if x > 50:
            large_values.add(x)

    # Misleading transformation (not used in final result)
    transformed = [((x * 2) + 3) // 7 for x in raw_samples]
    avg_transformed = sum(transformed) / len(transformed)

    # Core logic with conditional filtering
    flagged_large_evens = []
    temp_product = 1
    for i, val in enumerate(raw_samples):
        if sample_flags[i] and val in large_values and val % 2 == 0:
            flagged_large_evens.append(val)
            temp_product *= val  # distractor: product not used

    # Secondary filter based on string representation properties
    str_filtered = []
    for num in flagged_large_evens:
        num_str = str(num)
        if '8' not in num_str and len(num_str) == 2:
            str_filtered.append(num)

    # Final selection using tuple unpacking and conditionals
    backup_default = (0, 0)
    primary_candidate = (str_filtered[0], len(str_filtered)) if str_filtered else backup_default
    selected_value = primary_candidate[0]

    # Compute auxiliary statistics (irrelevant to answer)
    deviation_score = abs(selected_value - 50) if selected_value else 0
    status_flag = "valid" if deviation_score < 40 else "review"

    # Key computation path
    relevant_values = [v for v in raw_samples if v > selected_value and v % 3 == 0]
    filtered_sum = sum(relevant_values)
    
    # Output required variable
    print(f"Result: {filtered_sum}")

analyze_data_stream()