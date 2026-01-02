def analyze_efficiency(data, thresholds):
    efficiency_list = []
    for i, value in enumerate(data):
        if value > thresholds[i % len(thresholds)]:
            efficiency_list.append(value * 0.85)
        else:
            efficiency_list.append(value * 1.1)
    return efficiency_list

# Irrelevant helper function (decoy)
def calculate_entropy(seq):
    freq = {}
    for c in seq:
        freq[c] = freq.get(c, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 3)

# Another red herring: unused complex transformation
def transform_coordinates(coords):
    transformed = []
    for x, y in coords:
        rotated_x = x * 0.707 - y * 0.707
        rotated_y = x * 0.707 + y * 0.707
        magnitude = (rotated_x**2 + rotated_y**2)**0.5
        transformed.append((rotated_x, rotated_y, magnitude))
    return transformed

# Distractor variables
temp_log = ['error', 'warning', 'info', 'debug']
duplicate_filter = set(temp_log) | {'trace', 'fatal'}
useless_sum = sum(len(word) for word in temp_log if 'e' in word)

# Real data path
raw_metrics = [88, 92, 76, 81, 95]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Simulate preprocessing with some relevant and irrelevant steps
processed = []
for idx, (m, w) in enumerate(zip(raw_metrics, weights)):
    adjusted = m * (1 + 0.05 * (idx % 2))
    processed.append(adjusted)

# More distraction: string manipulation with no impact
diagnostic_msg = "System health check: OK"
status_flag = diagnostic_msg.replace('OK', 'PASS').split(': ')[-1]
if status_flag in duplicate_filter:
    status_flag = 'NORMAL'

# Actual logic buried among noise
def evaluate_performance(mets, wts):
    base_scores = []
    bonus = 0
    penalty = 0

    for i, (m, w) in enumerate(zip(mets, wts)):
        contribution = m * w
        base_scores.append(contribution)

        # Hidden rule: every odd index with metric > 80 gives bonus
        if i % 2 == 1 and m > 80:
            bonus += 3.5
        if m < 80:
            penalty += 2.0

    total_base = sum(base_scores)
    net_bonus = bonus - penalty

    # Secondary distraction: unused intermediate
    hypothetical_max = sum(m * w for m, w in zip([100]*5, wts))
    utilization_ratio = total_base / hypothetical_max if hypothetical_max else 0

    # Final computation
    final_raw = total_base + net_bonus

    # Additional red herring: bitwise that does nothing
    magic_offset = (len(mets) << 2) ^ 7
    decoy_result = final_raw & magic_offset | 15

    # Key assignment
    final_score = int(round(final_raw))

    # Dead code branch
    if final_score < 0:
        final_score *= -1

    return final_score

# Unused data structure
coordinates = [(1, 2), (3, 4), (5, 6)]
entropy_value = calculate_entropy('aabbc')
efficiency_data = analyze_efficiency([70, 85, 90], [75, 80])

# Critical execution point
final_score = evaluate_performance(processed, weights)
print(f"Result: {final_score}")