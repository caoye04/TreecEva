import itertools

def custom_hash(s):
    hash_val = 0
    for char in s:
        hash_val = (hash_val * 31 + ord(char)) & 0xFFFFFFFF
    return hash_val

def transform_fragment(fragment):
    transformed = ''
    for i, char in enumerate(fragment):
        if i % 2 == 0:
            transformed += char.upper()
        else:
            transformed += char.lower()
    return transformed[::-1]  # Reverse the string

def get_protein_marker(fragment):
    transformed = transform_fragment(fragment)
    hash_val = custom_hash(transformed)
    
    # Protein marker mapping
    if hash_val % 7 == 0:
        return 1000 + (hash_val % 100)
    elif hash_val % 5 == 0:
        return 2000 + (hash_val % 100)
    elif hash_val % 3 == 0:
        return 3000 + (hash_val % 100)
    else:
        return 4000 + (hash_val % 100)

# DNA fragment analysis
fragments = ['atgctag', 'ccggaatt', 'ggccttaa', 'ttaaccgg']
marker_id = 0

for fragment in fragments:
    if len(fragment) > 7:
        # Process only longer fragments
        sub_fragments = [fragment[i:i+6] for i in range(len(fragment)-5)]
        for sub in sub_fragments:
            if 'GG' in sub.upper():
                marker_id += get_protein_marker(sub)
                break  # Early return to avoid double counting
    else:
        # For shorter fragments, combine with others
        combinations = itertools.combinations(fragments, 2)
        for combo in combinations:
            if fragment in combo:
                combined = ''.join(combo)
                if len(set(combined)) <= 6:  # If 6 or fewer unique nucleotides
                    marker_id += get_protein_marker(combined)
                    break  # Early return

print(f'Result: {marker_id}')