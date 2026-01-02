def analyze_patterns(data, limits):
    count_valid = 0
    temp_sum = 0
    max_value = float('-inf')
    shift_accum = 0

    for index, (val, lim) in enumerate(zip(data, limits)):
        if val > lim:
            count_valid += 1
            temp_sum += val
            if val > max_value:
                max_value = val

        # Distractor: Bitwise shifting that doesn't impact result
        shift_accum ^= index << 1
        shift_accum %= 1000  # Irrelevant modulo to increase computation noise

    # Secondary distractor loop: processes dummy data
    dummy_data = [i ** 2 for i in range(len(data))]
    offset_correction = 0
    for item in dummy_data:
        if item % 7 == 0:
            offset_correction += 1  # Unused correction factor

    # Actual logic contribution: combine valid count and sum with fixed bias
    aggregate = temp_sum + count_valid * 2
    return aggregate + 5  # Final transformation independent of distractors


def main():
    # Input setup
    raw_values = [12, 15, 8, 20, 9, 16]
    thresholds = [10, 14, 9, 18, 10, 15]
    flags = [True, False, True, False, True, True]

    # Destructuring with enumerate - relevant use
    processed = []
    for i, v in enumerate(raw_values):
        if flags[i]:
            processed.append(v + i)
        else:
            processed.append(v - i)

    # Use of set operations (union and difference) - partially relevant
    unique_processed = set(processed)
    baseline_set = {x for x in range(5, 25)}
    filtered_range = unique_processed & baseline_set  # Intersection used indirectly

    # Simulate alternate path: unused branch
    if len(filtered_range) > 10:
        adjustment = sum(x for x in filtered_range if x % 2 == 0)
    else:
        adjustment = 0  # Dead end - not used later

    # Combine original and processed lists using zip
    combined_results = []
    for v, p in zip(raw_values, processed):
        combined_results.append((v + p) // 2)

    # Introduce red herring variable
    diagnostic_trace = []
    for cr in combined_results:
        diagnostic_trace.append(cr * 2 + 1)  # Computed but never used

    # Key execution point
    final_score = analyze_patterns(combined_results, thresholds)

    # Print result as required
    print(f"Result: {final_score}")

    return final_score

if __name__ == "__main__":
    main()