def calculate_final_score(ranks, points):
    adjusted = [points / (i + 1) for i in range(len(ranks))]
    filtered = [val for val in adjusted if val >= 5]
    total = sum(filtered)
    bonus = 10 if len(filtered) > 3 else 5
    return int(total + bonus) if total > 20 else int(total)

base_points = 25
rank_list = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
initial_score = base_points * len(rank_list) // 2

# Key computation step
calculate_flag = len(rank_list) > 4 and base_points % 5 == 0
final_score = calculate_final_score(rank_list, base_points) if calculate_flag else 0

print(f"Result: {final_score}")