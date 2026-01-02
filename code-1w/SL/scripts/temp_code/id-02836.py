def process_records(data_list):
    temp_results = []
    cumulative = 0
    threshold = 42
    decoy_value = 0

    for item in data_list:
        if len(item) < 3:
            continue
        
        # Irrelevant string transformation (distractor)
        transformed = item.upper().replace('X', 'Z').strip()
        if 'ERROR' in transformed:
            decoy_value += 1
            break

        # Real logic begins: extract digits and sum them
        digit_sum = sum(int(c) for c in item if c.isdigit())
        if digit_sum % 2 == 0:
            cumulative += digit_sum * 2
        else:
            cumulative -= digit_sum // 3

        temp_results.append(digit_sum)

    # Dead code path (never executed due to loop logic above)
    if decoy_value > 100:
        return [x * 10 for x in temp_results]

    return temp_results


def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log2(prob)
    return round(entropy, 6)

# Unused function - red herring
def validate_checksum(s):
    return sum(ord(c) for c in s) % 17 == 0

# Simulated dataset with mixed content
raw_data = ['A1B2C3', 'X9Y8', 'D4E5F6G7', 'H1I1J1', 'K0L2M5', 'ERROR9', 'N3O4P5']

# Step 1: Process raw data
interim = process_records(raw_data)

# Step 2: Compute derived stats (some irrelevant)
sum_interim = sum(interim)
mean_interim = sum_interim / len(interim) if interim else 0
max_interim = max(interim) if interim else 0

# Step 3: Generate auxiliary metrics (partial use)
aux_metrics = {
    'count': len(interim),
    'peak': max_interim,
    'stdev': (sum((x - mean_interim)**2 for x in interim) / len(interim))**0.5 if interim else 0,
    'flagged': False
}

# Step 4: Bit manipulation red herring
bit_fiddle = 0
for x in interim[:3]:
    bit_fiddle ^= (x << 2) | (x >> 1)
bit_fiddle &= 0xFF  # Limit to 8 bits

# Step 5: Set operations with partial relevance
unique_digits = set()
for entry in raw_data:
    unique_digits.update(c for c in entry if c.isdigit())
digit_set_complement = set('0123456789') - unique_digits  # unused

# Step 6: Determine rank based on criteria
rank_criteria = {
    'high': aux_metrics['count'] >= 5,
    'stable': aux_metrics['stdev'] < 2.0,
    'growing': mean_interim > 4.0
}

if rank_criteria['high'] and rank_criteria['stable']:
    rank = 1
elif rank_criteria['high'] or rank_criteria['growing']:
    rank = 2
else:
    rank = 3

# Step 7: Base points from combinatorics (irrelevant formula included)
base_points = 0
n = aux_metrics['count']
r = 2
# Real calculation
if n >= r:
    # C(n,2) = n*(n-1)/2
    base_points = n * (n - 1) // 2

# Decoy combinatoric (unused)
decoy_comb = 0
if n >= 3:
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                decoy_comb += 1

# Step 8: Final evaluation (key statement)
def evaluate_performance(rank, base_points):
    multiplier = {1: 3.5, 2: 2.0, 3: 1.0}[rank]
    penalty = 0
    
    # Additional condition based on string pattern (uses string method)
    valid_patterns = [s for s in raw_data if s.lower().startswith('a') or '5' in s]
    if len(valid_patterns) < 4:
        penalty += 15
    
    # Actual score computation
    score = base_points * multiplier - penalty
    
    # Round to nearest integer using integer division logic
    if score >= 0:
        final_rounded = (int(score) + (1 if (score - int(score)) >= 0.5 else 0))
    else:
        final_rounded = (int(score) - (1 if (score - int(score)) <= -0.5 else 0))
    
    return final_rounded

final_score = evaluate_performance(rank, base_points)
print(f"Target result: {final_score}")