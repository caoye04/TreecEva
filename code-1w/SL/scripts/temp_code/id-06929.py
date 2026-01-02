def process_inventory(levels, disposal):
    inventory_snapshot = {}
    adjustment_factor = 3
    decay_rate = 0.9
    temp_buffer = []

    for idx, (item, count) in enumerate(zip(levels.keys(), levels.values())):
        if count < 5:
            inventory_snapshot[item] = count * adjustment_factor
        elif count > 10:
            inventory_snapshot[item] = count // 2
        else:
            inventory_snapshot[item] = count + 1

        # Irrelevant string processing - distractor
        status_msg = f"Item {item} processed."
        if 'spare' in status_msg.lower():
            temp_buffer.append(idx)

    # Secondary loop with partial relevance
    cumulative_shift = 0
    for _, action in enumerate(disposal):
        if action == 'quarantine':
            cumulative_shift += 2
        elif action == 'discard':
            cumulative_shift -= 1

    # Core logic influenced only by disposal length and inventory values
    base_total = sum(inventory_snapshot.values())
    modifier = len(disposal) % 4 if len(disposal) > 0 else 0
    final_tally = base_total - cumulative_shift + modifier

    # Dead code path - misleading
    if len(temp_buffer) > 100:
        final_tally *= 2

    return final_tally

# Setup data
restock_levels = {
    'gear_a': 3,
    'gear_b': 12,
    'gear_c': 7,
    'gear_d': 4,
    'gear_e': 15
}
disposal_log = ['quarantine', 'quarantine', 'discard', 'inspect', 'quarantine']

# Execution
final_tally = process_inventory(restock_levels, disposal_log)
print(f"Result: {final_tally}")