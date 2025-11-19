import itertools

def tokenize_notes(note_string):
    return [token.strip() for token in note_string.split(',')]

def normalize_duration(duration_str):
    mapping = {'whole': 1.0, 'half': 0.5, 'quarter': 0.25, 'eighth': 0.125, 'sixteenth': 0.0625}
    return mapping.get(duration_str, 0.0)

def merge_sort_durations(durations):
    if len(durations) <= 1:
        return durations
    mid = len(durations) // 2
    left = merge_sort_durations(durations[:mid])
    right = merge_sort_durations(durations[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def calculate_rhythmic_complexity(sorted_durations):
    # Use itertools to generate all combinations of 3 durations
    combinations = list(itertools.combinations(sorted_durations, 3))
    score = 0
    for combo in combinations:
        # Complexity increases if durations form a geometric progression
        if combo[1] != 0 and combo[2] != 0 and abs(combo[1]/combo[0] - combo[2]/combo[1]) < 1e-9:
            score += 1
    return score

# Main processing pipeline
note_sequence = "quarter, eighth, half, sixteenth, eighth, quarter, half, sixteenth, quarter, eighth"
tokens = tokenize_notes(note_sequence)
durations = [normalize_duration(token) for token in tokens]
sorted_durations = merge_sort_durations(durations)
rhythmic_complexity_score = calculate_rhythmic_complexity(sorted_durations)

print(f"Result: {rhythmic_complexity_score}")