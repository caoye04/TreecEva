from collections import defaultdict

# Simulate daily transaction counts per category
category_transactions = [
    ('tech', 15), ('clothing', 23), ('tech', 12), ('books', 8),
    ('clothing', 19), ('books', 31), ('tech', 7), ('electronics', 44)
]

tx_counter = defaultdict(int)
for category, count in category_transactions:
    tx_counter[category] += count

tech_total = tx_counter['tech']
clothing_total = tx_counter['clothing']
electronics_total = tx_counter['electronics']
books_total = tx_counter['books']

# Irrelevant baseline offset (minimal distraction)
baseline_offset = 5
offset_adjusted = baseline_offset * 2

# Core accumulation
raw_sum = tech_total + clothing_total + books_total
final_sum = raw_sum + electronics_total
modulus_value = 17

total_mod_score = final_sum % modulus_value

# Print result as required
print(f"Target result: {total_mod_score}")