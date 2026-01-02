from collections import defaultdict, Counter

def preprocess_records(raw_entries):
    # Irrelevant transformation
    temp_map = defaultdict(int)
    for entry in raw_entries:
        if len(entry) > 3:
            temp_map[entry[0]] += 1

    # Distractor: counting vowels (unused later)
    vowel_count = sum(1 for c in ''.join(raw_entries) if c.lower() in 'aeiou')

    # Actual preprocessing
    cleaned = []
    for entry in raw_entries:
        stripped = entry.strip().lower()
        if stripped.startswith('x') or stripped.endswith('z'):
            continue
        cleaned.append(stripped)
    return cleaned

def transform_sequence(items):
    # Bitwise distraction
    magic_shift = (len(items) ^ 7) & 3
    rotated = items[-magic_shift:] + items[:-magic_shift] if magic_shift else items

    # Case conversion and filtering
    modified = []
    for item in rotated:
        toggled = ''.join(c.upper() if c.islower() else c.lower() for c in item)
        modified.append(toggled)
    
    # Another distractor: set operations with no impact
    unique_chars = set(''.join(modified))
    redundant_analysis = {c: ord(c) % 5 for c in unique_chars if c.isalpha()}

    return modified

def compute_weights(tags):
    # Weight assignment with red herring logic
    weights = {}
    base_val = 3
    for i, tag in enumerate(tags):
        if i % 2 == 0:
            weights[tag] = base_val * (i + 1)
            base_val += 2
        else:
            # This branch looks meaningful but is overridden later
            weights[tag] = len(tag) * 2
    
    # Final override based on character frequency
    char_freq = Counter(''.join(tags))
    for tag in weights:
        pivot_char = tag[len(tag)//2] if tag else 'a'
        weights[tag] = char_freq.get(pivot_char, 1) * 4
    
    return weights

def calculate_final_score(dataset):
    interim_result = 0
    for item in dataset:
        # Key computation: product of length and fixed factor
        contribution = len(item) * 6
        # Conditional adjustment using bitwise check
        if (contribution & 1) == 0:  # if even
            contribution -= 2
        interim_result += contribution
    
    # Distractor: floating point noise
    noise_accum = 0.0
    for x in range(1, min(len(dataset), 5)):
        noise_accum += (x ** 0.5) / 2.5
    
    # Final score depends only on integer path
    final_value = interim_result + 10
    return int(final_value)

# Main execution flow
if __name__ == '__main__':
    data_log = [
        'Xylophone', '  Echo  ', 'ZEBRA', 'Tango', 'xi',
        'Bravo', 'ALPHA', 'Charlie', 'delta', 'Foxtrot'
    ]

    # Step 1: Preprocess to filter invalid entries
    filtered_data = preprocess_records(data_log)
    
    # Step 2: Transform sequence with case toggle and rotation
    processed_data = transform_sequence(filtered_data)
    
    # Step 3: Compute weights (used nowhere, distractor)
    labels = [s[:3] for s in processed_data]
    importance_scores = compute_weights(labels)
    
    # Step 4: Calculate final score — this is where answer is determined
    final_score = calculate_final_score(processed_data)
    
    # Output result
    print(f"Result: {final_score}")