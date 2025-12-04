def calculate_performance():
    raw_scores = [85, 92, 78, 64, 91, 87, 95, 73]
    threshold = 80
    bonus_points = 5
    
    # Process scores above threshold with bonus
    qualifying_scores = [score + bonus_points for score in raw_scores if score > threshold]
    
    # Distractor calculations that don't affect final result
    avg_score = sum(raw_scores) // len(raw_scores)
    max_score = max(raw_scores)
    min_score = min(raw_scores)
    
    # Calculate total points from qualifying scores
    total_points = sum(qualifying_scores)
    
    # Multiplier based on score distribution
    high_performers = len([score for score in raw_scores if score >= 90])
    multiplier = 2 if high_performers >= 3 else 1
    
    # Bonus adjustment (irrelevant calculation)
    bonus_adjust = (max_score - min_score) // 10
    
    # Final calculation
    final_score = total_points * multiplier // bonus_adjust
    
    # Unused intermediate variable
    score_range = max_score - min_score
    
    print(f"Target result: {final_score}")

calculate_performance()