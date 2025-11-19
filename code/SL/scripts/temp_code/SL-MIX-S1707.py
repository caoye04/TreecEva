from collections import defaultdict

def calculate_priority(product_count, threshold):
    return max(0, threshold - product_count) * 2 + (1 if product_count < threshold else 0)

# State definitions
STATES = {'IN_STOCK': 0, 'LOW_STOCK': 1, 'OUT_OF_STOCK': 2}

# Product inventory: product_id -> count
inventory = {
    'COLA_12oz': 15,
    'CHIPS_REG': 8,
    'CANDY_BAR': 0,
    'JUICE_BOX': 3,
    'SODA_CAN': 12
}

# Thresholds for each product
thresholds = {
    'COLA_12oz': 10,
    'CHIPS_REG': 15,
    'CANDY_BAR': 5,
    'JUICE_BOX': 5,
    'SODA_CAN': 20
}

# State tracking
product_states = {}

# Calculate states and priority scores
priority_scores = defaultdict(int)
for product_id, count in inventory.items():
    threshold = thresholds[product_id]
    if count == 0:
        product_states[product_id] = STATES['OUT_OF_STOCK']
        priority_scores[product_id] = calculate_priority(count, threshold)
    elif count < threshold:
        product_states[product_id] = STATES['LOW_STOCK']
        priority_scores[product_id] = calculate_priority(count, threshold)
    else:
        product_states[product_id] = STATES['IN_STOCK']
        priority_scores[product_id] = 0

# Apply bonus for OUT_OF_STOCK items
for product_id, state in product_states.items():
    if state == STATES['OUT_OF_STOCK']:
        priority_scores[product_id] += 10

# Final calculation - sum of all priority scores with a modifier
modifier_func = lambda x: x * 1.5 if x > 10 else x + 5
adjusted_scores = [modifier_func(score) for score in priority_scores.values()]
priority_score = int(sum(adjusted_scores))

print(f"Result: {priority_score}")