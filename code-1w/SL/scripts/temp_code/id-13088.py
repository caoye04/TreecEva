def main():
    # Simulate warehouse inventory optimization with filtering logic
    inventory = [15, 0, 23, 8, 0, 42, 17, 0, 9, 31]
    backup_slots = [x * 2 for x in inventory if x > 10]  # Distractor: not used later

    # Threshold logic based on dynamic condition
    min_required = 10
    max_allowed = 50

    # Irrelevant statistical summary (distractor)
    avg_inventory = sum(inventory) / len(inventory) if inventory else 0
    zero_count = len([x for x in inventory if x == 0])
    spike_detected = any(inventory[i] > 2 * inventory[i-1] for i in range(1, len(inventory)))

    # Define dynamic threshold as a lambda (required feature)
    threshold_func = lambda x: x >= min_required and x <= max_allowed and x % 3 != 1

    # Secondary filter using set operations (suggested paradigm)
    valid_set = set(range(min_required, max_allowed + 1))
    filtered_candidates = [x for x in inventory if x in valid_set]

    # Additional distraction: simulate slot reallocation that isn't used
    def reallocate_slots(items):
        return [item + 1 for item in items if item < max_allowed]

    tentative_reallocation = reallocate_slots(filtered_candidates)

    # Core recursive filtering process (suggested paradigm)
    def deep_filter(items, func):
        if not items:
            return []
        head, tail = items[0], items[1:]
        result = deep_filter(tail, func) if tail else []
        if func(head):
            return [head] + result
        return result

    # Apply recursive filter
    approved_items = deep_filter(inventory, threshold_func)

    # Compute capacity score with weighted contribution
    weight_map = {k: 1.5 if k % 5 == 0 else 1.0 for k in approved_items}
    weighted_sum = sum(item * weight_map[item] for item in approved_items)

    # Final adjustment using only non-zero, approved values
    adjustment_factor = 1.2 if len(approved_items) > 3 else 1.0
    final_capacity = int(weighted_sum * adjustment_factor)

    # Print result as required
    print(f"Result: {final_capacity}")

main()