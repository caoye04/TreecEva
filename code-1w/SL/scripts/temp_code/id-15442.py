import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Misleading transformation chain
def decoy_transform(sequence):
    temp = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            temp.append(sequence[i] + 5)
        else:
            temp.append(sequence[i] * 2)
    return sorted(temp, reverse=True)

# Real processing function
def apply_filters(values, threshold):
    result = []
    for val in values:
        if val > threshold and val % 2 == 1:
            result.append(val)
    return result

# Secondary filter with bit manipulation distraction
def bitwise_mask(arr):
    masked = []
    mask = 7  # arbitrary bitmask
    for num in arr:
        processed = num & mask  # irrelevant to final logic
        masked.append(processed)
    return masked  # never used

# Core transformation logic
def transform_sequence(raw):
    scaled = [int(x * 1.5) for x in raw]
    adjusted = [y + 3 for y in scaled]
    return adjusted

# Dictionary-based configuration router (real use)
def get_config(mode):
    modes = {
        'A': {'threshold': 10, 'factor': 2, 'active': False},
        'B': {'threshold': 8, 'factor': 3, 'active': True},
        'C': {'threshold': 12, 'factor': 1, 'active': True}
    }
    return modes.get(mode, modes['B'])

# Real data processor
def process_data(items, settings):
    filtered = apply_filters(items, settings['threshold'])
    total = 0
    for n in filtered:
        total += n * settings['factor']
    return total

# Irrelevant sorting routine (distractor)
def sort_snapshot(data):
    copies = [{"val": x, "key": f"item_{x}"} for x in data]
    copies.sort(key=lambda z: z["val"], reverse=True)
    return copies

# Main execution flow
if __name__ == "__main__":
    # Initial dataset
    raw_input = [4, 7, 9, 12, 15, 18, 21]

    # Dead-end variables (red herrings)
    outlier_check = [x for x in raw_input if x > 20]
    baseline_avg = sum(raw_input) / len(raw_input)
    normalized = [round(x / baseline_avg, 2) for x in raw_input]

    # Apply real transformation
    transformed = transform_sequence(raw_input)

    # Generate decoy outputs (never used)
    decoy_result = decoy_transform(raw_input)
    dummy_map = {i: math.log(i + 1) for i in range(1, 6)}
    shadow_copy = raw_input.copy()
    shadow_copy.reverse()

    # Real configuration
    config = get_config('B')

    # Critical computation path
    interim_values = [x - 4 for x in transformed]
    cleaned = [y for y in interim_values if y > 0]  # remove negatives

    # Final output computation
    final_output = process_data(cleaned, config)

    # Print required result
    print(f"Result: {final_output}")