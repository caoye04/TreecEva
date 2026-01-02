def optimize_storage(config, limit):
    # Simulate storage optimization across shelves with constraints
    capacity = 0
    overflow_count = 0
    temp_buffer = []

    for shelf in config:
        base_load = sum(shelf[:len(shelf)//2]) if len(shelf) > 1 else shelf[0]
        extra_load = sum(shelf[len(shelf)//2:]) if len(shelf) > 2 else 0
        
        # Irrelevant transformation (distractor)
        transformed = list(map(lambda x: x ** 0.5 + 2, shelf))
        avg_transformed = sum(transformed) / len(transformed)

        adjusted_load = base_load * 1.1 + extra_load * 0.85

        if adjusted_load > limit:
            overflow_count += 1
            adjusted_load = limit  # clamp to threshold

        capacity += adjusted_load
        temp_buffer.append(adjusted_load)  # not used later

    # Dead code path - never executed due to logic above (mild red herring)
    if overflow_count < 0:
        capacity *= 1.1

    # Secondary calculation with slicing distraction
    history_log = temp_buffer[::-1]
    recent_sum = sum(history_log[:3]) if len(history_log) >= 3 else 0

    # Final adjustment based on system efficiency
    efficiency_factor = 0.95 if overflow_count == 0 else 0.88
    capacity *= efficiency_factor

    return int(capacity)

# System initialization
shelf_config = [
    [12, 15, 10, 8],
    [20, 5],
    [7, 9, 14],
    [25, 3, 6, 11, 13]
]
threshold = 22

# Misleading intermediate calculations
baseline = sum(sum(row) for row in shelf_config)  # unused in final logic
debug_snapshot = [row[-1] for row in shelf_config]  # irrelevant tracking

final_capacity = optimize_storage(shelf_config, threshold)
print(f"Result: {final_capacity}")