from collections import defaultdict

# Simulate user engagement analytics across platform features
def analyze_engagement_metrics():
    raw_clicks = [124, 85, 203, 92, 158]
    feature_names = ['search', 'profile', 'feed', 'settings', 'messages']
    session_durations = {name: clicks * 0.75 for name, clicks in zip(feature_names, raw_clicks)}

    # Initialize tracking structures
    engagement_stats = defaultdict(int)
    temporal_trends = [0.88, 0.91, 1.02, 0.94, 0.85]
    volatility_index = 0
    for i in range(len(temporal_trends)):
        volatility_index += abs(temporal_trends[i] - 0.9)

    # Populate base engagement counts
    for name, clicks in zip(feature_names, raw_clicks):
        engagement_stats[name] += clicks
        engagement_stats[f'{name}_peak'] = max(engagement_stats[name], clicks * temporal_trends[i])

    # Calculate derived metrics (some are distractions)
    avg_duration = sum(session_durations.values()) / len(session_durations)
    duration_variance = sum((v - avg_duration) ** 2 for v in session_durations.values()) / len(session_durations)
    normalized_scores = {k: v / 100.0 for k, v in engagement_stats.items() if '_peak' not in k}

    # Bonus calculation with weighted ranking
    rank_data = sorted([(feat, engagement_stats[feat]) for feat in feature_names], key=lambda x: x[1], reverse=True)
    rank_weights = {item[0]: 5 - i for i, item in enumerate(rank_data)}

    # Misleading transformation (not used in final result)
    transformed_ranks = {k: v ** 0.5 for k, v in rank_weights.items()}
    temp_magnitude = sum(transformed_ranks.values()) * 0.1

    # Actual bonus system
    bonus_multipliers = {'feed': 1.8, 'search': 1.6, 'messages': 1.5, 'profile': 1.2, 'settings': 1.0}
    bonus_weights = {k: bonus_multipliers[k] * rank_weights[k] for k in feature_names}

    def calculate_final_score(ranks, bonuses):
        base = sum(entry[1] for entry in ranks)
        adjustment = 0
        for name, _ in ranks:
            if name in ['feed', 'search']:
                adjustment += bonuses[name] * 0.4
            elif name == 'messages':
                adjustment += bonuses[name] * 0.25
        # Final computation path
        scaling_factor = 0.03
        intermediate_shift = base * scaling_factor + adjustment
        return int(intermediate_shift * 2.1)  # Final score derivation

    final_score = calculate_final_score(rank_data, bonus_weights)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    # Return unused diagnostics to add distraction
    diagnostics = {
        'volatility': volatility_index,
        'avg_duration': avg_duration,
        'temp_magnitude': temp_magnitude
    }
    
    return final_score

# Execute function
def main():
    analyze_engagement_metrics()

if __name__ == '__main__':
    main()