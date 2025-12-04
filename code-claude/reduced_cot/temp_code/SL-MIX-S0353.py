# Calculate player scores in a bowling tournament
player_names = ['Alice', 'Bob', 'Charlie', 'David']

# Frame scores for each player (last 3 frames)
frame_data = {
    'Alice': [8, 10, 9],
    'Bob': [7, 8, 10],
    'Charlie': [10, 10, 8],
    'David': [9, 7, 6]
}

# Bonus points from previous tournament
bonus_points = {'Alice': 5, 'Bob': 0, 'Charlie': 3, 'David': 2}

# Calculate total scores
player_scores = {}
for player in player_names:
    # Sum the frame scores
    frame_sum = sum(frame_data[player])
    
    # Add bonus points if the player scored a strike (10) in any frame
    if 10 in frame_data[player]:
        player_scores[player] = frame_sum + bonus_points[player]
    else:
        player_scores[player] = frame_sum

# Get scores for players whose names start with letters after 'C'
late_alphabet_players = {name: score for name, score in player_scores.items() 
                        if name[0] > 'C'}

# Calculate average score of remaining players
remaining_players = {name: score for name, score in player_scores.items() 
                   if name not in late_alphabet_players}
avg_score = sum(remaining_players.values()) / len(remaining_players) if remaining_players else 0

# Calculate total score across all players
total_score = sum(player_scores.values())

print(f"Result: {total_score}")