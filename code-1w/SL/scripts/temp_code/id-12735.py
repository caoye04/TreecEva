def calculate_final_score(records):
    total_points = 0
    bonuses = {"A": 5, "B": 3, "C": 1}
    penalties = set(["X", "Y", "Z"])

    for record in records:
        category = record["type"].upper()
        value = record["value"]

        if category in penalties:
            total_points -= 2
            continue

        if category in bonuses:
            multiplier = bonuses[category]
            total_points += value * multiplier

        # Irrelevant string operation (minor distraction)
        status_msg = f"Processing {category}".replace("P", "p")

    return total_points

# Simulated dataset
data = [
    {"type": "a", "value": 4},
    {"type": "b", "value": 7},
    {"type": "x", "value": 5},  # Penalty case
    {"type": "c", "value": 10},
    {"type": "z", "value": 1}   # Penalty case
]

initial_offset = 10
final_score = calculate_final_score(data)
final_score += initial_offset

print(f"Target result: {final_score}")