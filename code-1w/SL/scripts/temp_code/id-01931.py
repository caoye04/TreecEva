def calculate_final_score(data, mult):
    base = data['score'] * mult
    penalty = 10 if data['errors'] > 0 else 0
    bonus = 5 if data['streak'] >= 3 else 0
    adjusted = base - penalty + bonus
    return int(adjusted) if adjusted >= 0 else 0

rank_data = {'score': 87, 'errors': 2, 'streak': 4}
base_multiplier = 3

# Key computation step
distraction_counter = 0
temp_results = [i**2 for i in range(5)]  # Irrelevant list comprehension
distraction_counter += sum(temp_results)

final_score = calculate_final_score(rank_data, base_multiplier)
print(f"Result: {final_score}")