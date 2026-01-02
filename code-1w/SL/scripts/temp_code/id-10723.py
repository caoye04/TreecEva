from itertools import groupby

def analyze_sequences(values):
    # Misleading function: computes run lengths but not used in final result
    runs = []
    for k, g in groupby(values):
        runs.append((k, len(list(g))))
    return runs

def validate_constraints(arr):
    # Another red herring: checks monotonicity, never actually called
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def calculate_final_score(records, modifiers):
    base_total = 0
    adjustment = 0
    temp_result = []
    
    # Real computation begins
    for rank, entries in records.items():
        count = len(entries)
        if count >= 3:
            base_total += rank * count
        else:
            adjustment -= rank  # penalty for small groups

        # Irrelevant transformation
        squared_entries = [x**2 for x in entries if x > 2]
        temp_result.extend(squared_entries)
    
    # Distractor loop: modifies temp_result but unused
    for i in range(len(temp_result)):
        temp_result[i] += 5
        if temp_result[i] > 50:
            temp_result[i] //= 2

    # Actual use of modifiers (bonus_map)
    multiplier = 1
    for key in sorted(modifiers.keys()):
        if key < base_total:
            multiplier += modifiers[key]

    intermediate = base_total + adjustment
    final_score = intermediate * multiplier

    # Dead code path: never reached due to logic above
    if False and len(temp_result) > 100:
        final_score -= sum(temp_result) // 10

    return final_score

# Main data setup
rank_data = {
    1: [10, 12, 15],
    2: [8, 7],
    3: [5, 6, 9, 11],
    4: [3],
    5: [4, 2, 1, 13]
}

bonus_map = {
    1: 1,
    3: 2,
    6: 1
}

# Trigger analysis (unused)
dummy_runs = analyze_sequences([1,1,2,2,2,3])

# Key computation
final_score = calculate_final_score(rank_data, bonus_map)

print(f"Result: {final_score}")