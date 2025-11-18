def calculate_prep_time(steps, index=0):
    if index >= len(steps) or steps[index] == -1:
        return 0
    base_time = steps[index]
    if index % 3 == 0:  # Every third step involves marinating
        base_time *= 2
    return base_time + calculate_prep_time(steps, index + 1)

recipe_steps = [10, 5, 7, 15, 3, 9, 12, -1, 8]
total_time = calculate_prep_time(recipe_steps)
print(f"Result: {total_time}")