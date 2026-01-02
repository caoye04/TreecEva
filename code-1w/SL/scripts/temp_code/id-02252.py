from collections import defaultdict
import math

# Simulate a user feedback analysis system for a learning platform

# Irrelevant utility function (decoy)
def normalize_data(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return [(x - mean) / math.sqrt(variance + 1e-8) for x in data]

# Another decoy function that is never called
def encrypt_log(log_entries):
    encrypted = []
    for entry in log_entries:
        enc = ''.join(chr((ord(c) + 3) % 128) for c in entry)
        encrypted.append(enc)
    return encrypted

# Misleading intermediate calculation with dead-end logic
temporary_weights = [0.1, 0.3, 0.4, 0.2]
adjusted_weights = [w ** 2 for w in temporary_weights]
scaled_weights = [w / sum(adjusted_weights) for w in adjusted_weights]  # Not used later

# Core data structures
feedback_levels = ['beginner', 'intermediate', 'advanced', 'expert']
user_feedback = [
    {'level': 'beginner', 'rating': 3, 'engagement': 1},
    {'level': 'intermediate', 'rating': 4, 'engagement': 2},
    {'level': 'advanced', 'rating': 5, 'engagement': 3},
    {'level': 'expert', 'rating': 4, 'engagement': 4}
]

# Build feedback chain using tuple packing/unpacking
feedback_chain = []
for fb in user_feedback:
    code_factor = 1 if fb['rating'] >= 4 else 0
    time_bonus = fb['engagement'] * 0.5
    # Use lambda to compute dynamic contribution
    contribution = (lambda lvl: 1.0 if lvl == 'beginner' else (1.5 if lvl == 'intermediate' else (2.0 if lvl == 'advanced' else 2.5)))(fb['level'])
    packed = (fb['rating'], fb['engagement'], code_factor, time_bonus, contribution)
    feedback_chain.append(packed)

# Distractor: unused transformation
transformed_chain = [tuple(math.sin(x) if isinstance(x, (int, float)) else hash(x) for x in item) for item in feedback_chain]

# Initialize scoring map with defaultdict (irrelevant keys included)
score_map = defaultdict(float)
score_map['base_offset'] = -1.2
score_map['penalty_rate'] = 0.05
score_map['bonus_multiplier'] = 1.1

# Real processing begins here
base_score = 0.0
penalty_count = 0

for rating, engagement, code_factor, time_bonus, contribution in feedback_chain:
    if rating < 4:
        penalty_count += 1
    base_score += rating * 10
    base_score += engagement * 2
    base_score += contribution * 3

# Apply fake normalization (distractor)
normalized_base = base_score / (1 + math.log(penalty_count + 1))

# Unused complex structure (red herring)
summary_matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        summary_matrix[i][j] = (i * j + 1) % 7

# Actual evaluation function with nested logic
def evaluate_performance(chain):
    total = 0.0
    level_counter = defaultdict(int)
    
    # Count levels using defaultdict
    for item in chain:
        level_value = item[4]  # contribution as proxy
        if level_value == 1.0:
            level_counter['beginner'] += 1
        elif level_value == 1.5:
            level_counter['intermediate'] += 1
        elif level_value == 2.0:
            level_counter['advanced'] += 1
        else:
            level_counter['expert'] += 1
    
    # Complex conditional scoring
    for item in chain:
        rating, engagement, code_factor, time_bonus, contribution = item
        
        # Primary score accumulation
        if rating >= 4:
            total += rating * (engagement + 1)
        else:
            total += rating * 1.5
            
        # Nested condition with bitwise distraction (irrelevant operation)
        temp_flag = (engagement << 2) & 7
        if temp_flag > 3 and code_factor:
            total += contribution * 1.2
        
        # Additional logic involving multiple concepts
        if contribution >= 2.0:
            total *= 1.05  # multiplier effect
    
    # Final adjustment based on level distribution (only experts matter here)
    expert_ratio = level_counter['expert'] / len(chain) if chain else 0
    if expert_ratio >= 0.25:
        total += 10
    
    return total

# Critical statement
final_score = evaluate_performance(feedback_chain)

# Print result
print(f"Result: {final_score}")