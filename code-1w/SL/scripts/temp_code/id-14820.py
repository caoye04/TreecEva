from collections import defaultdict, Counter

# Simulate user activity logs with redundant and irrelevant fields
timestamps = [100, 150, 200, 250, 300, 350]
user_actions = ['login', 'edit', 'save', 'edit', 'logout', 'edit']
dummy_weights = [0.1, 0.5, 0.3, 0.9, 0.2, 0.7]
irrelevant_multipliers = [2, 3, 1, 4, 2, 1]

# Initialize tracking structures
action_count = defaultdict(int)
edit_sequence_tracker = []
weight_accumulator = 0.0

# Process each action with extraneous computations
for i in range(len(user_actions)):
    action = user_actions[i]
    action_count[action] += 1
    
    # Irrelevant weight mixing
    weight_accumulator += dummy_weights[i] * irrelevant_multipliers[i]
    
    if action == 'edit':
        edit_sequence_tracker.append(i)
        
    # Fake normalization (not used later)
    normalized = weight_accumulator / (i + 1) if i != 2 else 0

# Misleading statistical summary
stats_summary = Counter(user_actions)
duplicate_count = sum(1 for x in stats_summary.values() if x > 1)

# Extract only edits for processing
edit_indices = [i for i, a in enumerate(user_actions) if a == 'edit']
offset_values = [idx * 2 + 1 for idx in edit_indices]

# Apply modular arithmetic and shift operations
shifted_offsets = [((val << 1) % 25) for val in offset_values]
reduced_score = sum(shifted_offsets) // len(shifted_offsets) if shifted_offsets else 0

# Case conversion distraction
action_strings = [a.upper() for a in user_actions]
lower_check = [a.lower() for a in action_strings]

# Core logic hidden among distractions: compute frequency-adjusted score
def calculate_edit_contribution(count, sequence):
    base = count * 3
    bonus = len(sequence) % 4  # extra complexity
    return base + bonus

edit_contribution = calculate_edit_contribution(action_count['edit'], edit_sequence_tracker)

# Secondary computation with red herring variables
phantom_score = 0
for j in range(3):
    phantom_score += j * duplicate_count  # unused later

# Final aggregation using relevant data only
processed_data = {
    'edit_contribution': edit_contribution,
    'reduced_score': reduced_score,
    'size_factor': len(edit_sequence_tracker)
}

# Key statement
final_score = calculate_final_score(processed_data)

# Definition of final scoring function
def calculate_final_score(data):
    contribution = data['edit_contribution']
    reduction = data['reduced_score']
    factor = data['size_factor']
    temp_debug = reduction * 0.5  # intermediate debug var, not critical
    return (contribution + reduction) * factor - 10  # deterministic formula

# Print result for execution verification
print(f"Result: {final_score}")