def calculate_team_stats(players, threshold=5):
    # Track player performance
    active_set = set()
    qualified_set = set()
    bench_players = {11, 23, 45, 67}
    
    for player_id, stats in players.items():
        # Process active players (those who played)
        if stats['minutes'] > 0:
            active_set.add(player_id)
            
        # Process qualified players (those meeting performance criteria)
        performance_score = stats['points'] * 1.0 + stats['assists'] * 0.7 + stats['rebounds'] * 0.5
        if performance_score >= threshold and player_id not in bench_players:
            qualified_set.add(player_id)
    
    # Calculate players in both sets (for reporting purposes)
    common_players = active_set.intersection(qualified_set)
    common_count = len(common_players)
    
    # Track players unique to each set
    only_active = active_set - qualified_set
    only_qualified = qualified_set - active_set
    
    # This is what we want to know: players in exactly one set (symmetric difference)
    active_players = active_set.copy()  # Create copies to avoid modifying originals
    qualified_players = qualified_set.copy()
    symmetric_difference_count = len(active_players.symmetric_difference(qualified_players))
    
    # Some additional processing (not affecting the answer)
    potential_improvement = sum(1 for player_id in only_active if player_id % 2 == 0)
    reserve_options = {x for x in range(10, 50, 10)} & bench_players
    
    return symmetric_difference_count

# Player data: ID -> stats dictionary
player_data = {
    12: {'minutes': 32, 'points': 8, 'assists': 4, 'rebounds': 2},
    23: {'minutes': 0, 'points': 0, 'assists': 0, 'rebounds': 0},   # Bench player
    34: {'minutes': 28, 'points': 12, 'assists': 2, 'rebounds': 8},
    45: {'minutes': 15, 'points': 4, 'assists': 1, 'rebounds': 3},  # Bench player
    56: {'minutes': 0, 'points': 0, 'assists': 0, 'rebounds': 0},
    67: {'minutes': 22, 'points': 6, 'assists': 7, 'rebounds': 1},  # Bench player
    78: {'minutes': 18, 'points': 10, 'assists': 3, 'rebounds': 4}
}

result = calculate_team_stats(player_data, threshold=8)
print(f"Result: {result}")