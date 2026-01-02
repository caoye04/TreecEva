def process_item(item):
    base_value = item * 2 + 3
    temp_offset = (item % 7) ** 2
    adjusted = base_value - temp_offset
    return adjusted if adjusted > 0 else 0

def validate_sequence(seq):
    return all(x > 0 for x in seq)

def generate_lookup(keys):
    # Irrelevant computation: builds a map not fully used
    lookup = {}
    for k in keys:
        lookup[k] = f"item_{k * 3 + 1}"
    return lookup

def calculate_final_score(raw_data):
    filtered = [x for x in raw_data if x % 2 == 1]  # Keep odd numbers
    transformed = [process_item(x) for x in filtered]

    # Dead code path: validation not affecting logic
    is_valid = validate_sequence(transformed)
    status_msg = "Valid" if is_valid else "Invalid"

    # Auxiliary structure with partial use
    indices = list(range(len(transformed)))
    metadata_map = {i: f"entry_{i}" for i in indices}
    unused_summary = ''.join(metadata_map.values())  # Never used

    # Core accumulation logic
    accumulator = 0
    for i, val in enumerate(transformed):
        if i % 2 == 0:
            accumulator += val * (i + 1)
        else:
            accumulator -= val // (i + 1) if (i + 1) != 0 else 0

    scaling_factor = 1.5 if len(transformed) > 3 else 1.0
    intermediate = accumulator * scaling_factor

    # Conditional expression with string method red herring
    log_entry = f"Score_{intermediate:.2f}".upper().replace("_", "-")
    extra_penalty = len(log_entry.split("-")[0]) if "SCORE" in log_entry else 0

    final_score = int(intermediate - extra_penalty)
    return final_score

data = [4, 9, 2, 11, 6, 13, 8]
lookup_table = generate_lookup(data)  # Computed but not used
initial_flag = any(x > 10 for x in data)
temp_result = sum(x for x in data if x < 5)
final_score = calculate_final_score(data)
print(f"Result: {final_score}")