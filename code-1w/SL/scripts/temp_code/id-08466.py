import itertools

def generate_pattern(n):
    return [i ** 2 % 7 for i in range(n)]

def validate_sequence(seq):
    return all(x >= 0 for x in seq) and sum(seq) % 2 == 0

def calculate_entropy(data):
    # Irrelevant helper function (dead weight)
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

def calculate_equilibrium(matrix, limits):
    temp_result = 0
    adjustment_factor = 1.5
    
    # Real computation begins
    flat_data = list(itertools.chain.from_iterable(matrix))
    filtered_values = [v for v in flat_data if v > limits[0]]
    
    # Distractor: complex but unused filtering
    masked_data = []
    for row in matrix:
        masked_row = []
        for val in row:
            if val % 5 == 0:
                masked_row.append(val + 3)
            else:
                masked_row.append(val - 1)
        masked_data.append(masked_row)
    
    # Another distractor: unused entropy calculation
    _ = calculate_entropy(flat_data)
    
    # Actual logic path
    cumulative = 0
    for i, val in enumerate(filtered_values):
        if i % 2 == 0:
            cumulative += val * (i + 1)
        else:
            cumulative -= val // (i + 1) if i + 1 != 0 else 0
    
    # Conditional expression used
    scaling = 2 if len(filtered_values) > 5 else 1
    temp_result = cumulative * scaling
    
    # Secondary real operation: count transitions above threshold
    transitions = 0
    for i in range(len(flat_data) - 1):
        if flat_data[i] < limits[1] <= flat_data[i+1]:
            transitions += 1
    
    final_adjustment = transitions * 10
    return temp_result + final_adjustment

# Setup problem context: network flow analysis
base_seeds = [3, 7, 12, 15]
flow_matrix = [[s * (i+1) + j for j in range(4)] for i, s in enumerate(base_seeds)]

# Threshold parameters
thresholds = [8, 14]

# Dead code: unused pattern generation
pattern_sequence = generate_pattern(10)
dummy_validation = validate_sequence(pattern_sequence)

# Key computational statement
equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)

# Print result as required
print(f"Target result: {equilibrium_score}")