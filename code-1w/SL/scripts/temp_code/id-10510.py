def analyze_filtration_sequence(elements, base_modifier):
    # Irrelevant pre-processing: count vowels in element names
    vowel_count = sum(1 for e in elements for v in 'aeiou' if v in e.lower())

    # Distractor: unused transformation map
    transform_map = {e: hash(e) % 100 for e in elements}

    process_chain = []
    temp_value = 0

    for idx, elem in enumerate(elements):
        # Apply complex but partially irrelevant transformation
        encoded = len(elem) * (idx + 1) + base_modifier
        if encoded % 2 == 0:
            temp_value += encoded ** 0.5
            process_chain.append(int(temp_value))
        else:
            temp_value -= len(elem)
            if temp_value < 0:
                temp_value = abs(temp_value)
            process_chain.append(temp_value * 2)

    # Dead code path: never executed due to values
    overflow_flag = False
    for val in process_chain:
        if val > 1000:
            overflow_flag = True
            break
    if overflow_flag:
        process_chain = [x // 2 for x in process_chain]

    # Define lambda for dynamic filtering (used later)
    activation_filter = lambda x, th: x > th and (x % 3 == 0 or x % 5 == 0)

    def calculate_efficiency(chain, threshold):
        # Semi-relevant: counts how many pass threshold logic
        valid_nodes = 0
        penalty = 0
        for i, node in enumerate(chain):
            if activation_filter(node, threshold):
                valid_nodes += 1
            elif i % 2 == 0:
                penalty += 1  # minor penalty on even indices

        # Core calculation: efficiency score
        raw_score = valid_nodes * threshold - penalty
        return max(raw_score, 0)  # ensure non-negative

    # Unused helper: misleading function definition
    def diagnose_chain_integrity(seq):
        return set(seq) & {0, 1, -1}  # never called

    # Key configuration parameter
    activation_threshold = 12

    # Critical execution point
    filtration_score = calculate_efficiency(process_chain, activation_threshold)

    # Print final result as required
    print(f"Result: {filtration_score}")

    # Return nothing; only side effect is printing
    return None

# Input data with meaningful naming
chemical_series = ['Hydrogen', 'Oxygen', 'Nitrogen', 'Chlorine', 'Xenon']
base_offset = 7

# Execute function
analyze_filtration_sequence(chemical_series, base_offset)