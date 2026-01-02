def main():
    # Real-world scenario: Evaluating employee performance with weighted metrics
    base_metrics = {'productivity': 85, 'accuracy': 92, 'punctuality': 78, 'teamwork': 88}
    weights = {'productivity': 0.4, 'accuracy': 0.3, 'punctuality': 0.2, 'teamwork': 0.1}

    # Irrelevant preprocessing: Normalize all values to 100 scale (already are)
    normalized = {k: v / 100.0 for k, v in base_metrics.items()}
    scaled_back = {k: int(v * 100) for k, v in normalized.items()}  # Redundant step

    # Distractor: Calculate variance for no reason
    mean_val = sum(scaled_back.values()) / len(scaled_back)
    variance = sum((x - mean_val) ** 2 for x in scaled_back.values()) / len(scaled_back)

    # Semi-relevant transformation: Boost accuracy if above threshold
    adjusted_metrics = scaled_back.copy()
    if adjusted_metrics['accuracy'] > 90:
        adjusted_metrics['accuracy'] += 5  # Max capped at 100 later
        adjusted_metrics['accuracy'] = min(adjusted_metrics['accuracy'], 100)

    # Dead code path: never executed due to logic
    debug_mode = False
    temp_offset = 0
    if debug_mode and temp_offset > 0:
        for k in adjusted_metrics:
            adjusted_metrics[k] -= temp_offset

    # Core evaluation function using lambda for dynamic weighting
    apply_weight = lambda val, w: val * w

    def evaluate_performance(metrics, weights):
        total = 0.0
        for key in weights:
            total += apply_weight(metrics[key], weights[key])
        bonus = 0
        # Performance bonus if overall weighted score > 85 before rounding
        preliminary = total
        if preliminary > 85:
            bonus = 3
        return int(total + bonus)  # Final integer score

    # Additional distraction: simulate peer reviews that aren't used
    peer_reviews = [88, 90, 85, 92]
    avg_peer = sum(peer_reviews) / len(peer_reviews)
    consistency = abs(avg_peer - mean_val) < 5

    final_score = evaluate_performance(adjusted_metrics, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()