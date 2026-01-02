from collections import defaultdict, Counter

# Simulate player game session analytics with scoring logic
def analyze_sessions(player_logs):
    stats = defaultdict(int)
    event_counter = Counter()

    for log in player_logs:
        action = log['action']
        duration = log['duration']
        stats['total_time'] += duration
        stats['actions_count'] += 1
        event_counter[action] += 1

        if action == 'powerup_collected':
            stats['boost_count'] += 1
        elif action == 'obstacle_hit':
            stats['penalty_count'] += 1

    # Irrelevant aggregation (distractor)
    avg_duration = stats['total_time'] / len(player_logs) if player_logs else 0
    stats['avg_duration'] = avg_duration

    return stats


def calculate_ranking(raw_scores):
    sorted_players = sorted(raw_scores.items(), key=lambda x: x[1], reverse=True)
    rank_mapping = {}
    for rank, (player, score) in enumerate(sorted_players, 1):
        rank_mapping[player] = rank
    
    # Dummy transformation (semi-relevant but not used directly)
    normalized_ranks = {p: 1 / r for p, r in rank_mapping.items()}
    return rank_mapping


def calculate_final_score(ranks, multiplier):
    base_total = sum(100 // rank for rank in ranks.values())
    adjustment = 0

    # Apply tiered bonus based on ranking
    for rank in ranks.values():
        if rank == 1:
            adjustment += 25
        elif rank == 2:
            adjustment += 15
        elif rank <= 5:
            adjustment += 5

    # Extra distraction: unused calculation path
    hypothetical_max = sum(100 // r for r in range(1, len(ranks) + 1))
    efficiency_ratio = base_total / hypothetical_max if hypothetical_max > 0 else 0

    final_score = (base_total + adjustment) * multiplier
    return int(final_score)

# Main execution
if __name__ == "__main__":
    # Sample gameplay logs for 5 players (simulated data)
    logs_v1 = [{'action': 'move', 'duration': 12}, {'action': 'powerup_collected', 'duration': 3}]
    logs_v2 = [{'action': 'move', 'duration': 8}, {'action': 'obstacle_hit', 'duration': 4}, {'action': 'powerup_collected', 'duration': 5}]
    logs_v3 = [{'action': 'move', 'duration': 15}, {'action': 'move', 'duration': 7}, {'action': 'obstacle_hit', 'duration': 2}]
    logs_v4 = [{'action': 'powerup_collected', 'duration': 6}, {'action': 'move', 'duration': 9}]
    logs_v5 = [{'action': 'move', 'duration': 20}]

    all_logs = [logs_v1, logs_v2, logs_v3, logs_v4, logs_v5]
    players = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

    raw_scores = {}
    performance_meta = {}

    for i, logs in enumerate(all_logs):
        result = analyze_sessions(logs)
        base_score = result['total_time'] * 10 - result['penalty_count'] * 15 + result['boost_count'] * 25
        raw_scores[players[i]] = base_score

        # Store extra metadata (not used later)
        performance_meta[players[i]] = {
            'actions': result['actions_count'],
            'efficiency': result['total_time'] / (result['actions_count'] + 1)
        }

    # Calculate rankings from raw scores
    rank_data = calculate_ranking(raw_scores)

    # Bonus determined by external rule (fixed for determinism)
    bonus_multiplier = 1.2

    # Key statement: compute final adjusted score
    final_score = calculate_final_score(rank_data, bonus_multiplier)

    print(f"Result: {final_score}")