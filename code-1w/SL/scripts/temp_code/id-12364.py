from collections import defaultdict

# Simulate financial transaction analysis with noise and intermediate steps

def preprocess_transactions(raw_data, filter_flag=True):
    # Irrelevant transformation for some entries
    temp_offset = 0
    for item in raw_data:
        if 'type' in item and item['type'] == 'CREDIT':
            temp_offset += 1  # Distractor: not used later

    # Actual processing
    processed = []
    for entry in raw_data:
        amount = entry.get('amount', 0)
        direction = entry.get('direction', 'neutral')
        transformed = abs(amount) * (1 if direction == 'in' else -1)
        if filter_flag and amount > 500:
            transformed *= 0.9  # Apply fee simulation
        processed.append(transformed)
    return processed


# Helper lambda for conditional weighting (semi-relevant)
calculate_weight = lambda x: 1.05 if x > 0 else 0.95

# Raw input dataraw_transactions = [
    {'amount': 600, 'direction': 'in', 'type': 'CREDIT'},
    {'amount': 300, 'direction': 'out'},
    {'amount': 800, 'direction': 'in'},
    {'amount': 450, 'direction': 'out'},
    {'amount': 150, 'direction': 'in'}
]

# Preprocessing stepprocessed_records = preprocess_transactions(raw_transactions)

# Begin analysis with redundant countersstate_counter = defaultdict(int)
total_volume = 0
positive_count = 0

for val in processed_records:
    total_volume += abs(val)
    state_counter['total_entries'] += 1
    if val > 0:
        positive_count += 1
        state_counter['gains'] += 1
    else:
        state_counter['losses'] += 1

# Secondary transformation using list comprehension with filteringfiltered_impact = [x * calculate_weight(x) for x in processed_records if abs(x) > 200]

# Dummy combinatorial check (distractor)combination_score = 0
for i in range(len(filtered_impact)):
    for j in range(i + 1, len(filtered_impact)):
        if filtered_impact[i] * filtered_impact[j] < 0:
            combination_score += 1  # Counts sign changes, not used later

# Core logic: compute threshold balance based on adjusted net flowadjusted_net = sum([x * 1.02 for x in processed_records])  # Minor adjustment
penalty_factor = len([x for x in processed_records if x < -400]) * 50  # Only triggers if large withdrawals
base_reserve = 1000

# Final risk-adjusted balance calculation
intermediate_shift = sum(filtered_impact) * 0.1  # Small influence
threshold_balance = base_reserve + adjusted_net - penalty_factor + intermediate_shift

# Dead code path (never executed, adds confusion)
if False:
    threshold_balance *= 0.9
    backup_ref = [1, 2, 3]
    backup_ref.clear()

# Key analysis functiondef analyze_data(data):
    summary = sum(data) * 0.01
    return int(summary) + 500  # Irrelevant to threshold_balance

final_analysis = analyze_data(processed_records)

print(f"Result: {threshold_balance}")