def calculate_final_score(data, mult):
    base = data['points'] // 7
    bonus = data['rank'] % 4
    if bonus > 2:
        base += 1
    else:
        base -= 1
    return base * mult + data.get('adjustment', 0)

# Irrelevant auxiliary variable (minimal distraction)
temp_log = {"timestamp": "2023-08-01", "user": "admin"}

rank_data = {
    'points': 89,
    'rank': 3,
    'adjustment': 2
}
base_multiplier = 6

final_score = calculate_final_score(rank_data, base_multiplier)
print(f"Result: {final_score}")