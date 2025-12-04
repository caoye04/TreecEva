player_stats = {'level': 5, 'experience': 120, 'health': 85}
base_score = player_stats['level'] * 10
bonus_check = True if player_stats['experience'] > 100 else False
modifier = 15 if bonus_check else 5
final_score = base_score + modifier
print(f"Result: {final_score}")