def analyze_performance(metrics):
    # Distractor: processing unrelated data
    raw_scores = [m['response_time'] for m in metrics]
    processed_scores = [score * 2 for score in raw_scores]
    
    # Relevant processing for quality scores
    quality_scores = [m['accuracy'] * 100 for m in metrics]
    adjusted_scores = [score + (score % 7) for score in quality_scores]
    
    # Distractor: unused calculations
    time_variance = max(raw_scores) - min(raw_scores)
    performance_index = time_variance * len(metrics)
    
    # Critical path: sorting and indexing
    sorted_scores = sorted(adjusted_scores)
    score_gap = sorted_scores[-1] - sorted_scores[0]
    
    # More distractors: misleading computations
    quality_modifier = sum(adjusted_scores) // len(metrics) if len(metrics) > 0 else 0
    efficiency_ratio = score_gap / quality_modifier if quality_modifier != 0 else 0
    
    # Dead code path
    if efficiency_ratio > 10:
        bonus_points = efficiency_ratio * 2
    else:
        bonus_points = 0
    
    # Final calculation with string manipulation
    score_labels = [f"Score_{i}" for i in range(len(sorted_scores))]
    label_index = len(score_labels) - 1
    
    # Key statement: final computation
    final_score = sorted_scores[-1] - quality_modifier
    
    print(f"Result: {final_score}")

# Test data
performance_metrics = [
    {'response_time': 45, 'accuracy': 0.87},
    {'response_time': 32, 'accuracy': 0.92},
    {'response_time': 51, 'accuracy': 0.85},
    {'response_time': 28, 'accuracy': 0.95}
]

analyze_performance(performance_metrics)