def calculate_product_quality(ratings):
    base_scores = [rating * 2 for rating in ratings]
    adjusted_scores = []
    temp_calc = 0
    
    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            adjusted = score + 5
        else:
            adjusted = score - 3
        adjusted_scores.append(adjusted)
        temp_calc += score * i  # This calculation doesn't affect final result
    
    quality_ranges = {'high': 15, 'medium': 10, 'low': 5}
    intermediate_check = quality_ranges.get('medium', 0)
    
    quality_assessment = []
    for score in adjusted_scores:
        if score > 12:
            quality_assessment.append(score // 2)
        else:
            quality_assessment.append(score + 1)
    
    # Distractor operations that don't impact final result
    dummy_analysis = [x for x in quality_assessment if x > 7]
    verification_sum = sum(dummy_analysis)
    
    final_quality_score = quality_assessment[-1]
    print(f"Target result: {final_quality_score}")

# Test data
product_ratings = [4, 7, 3, 9, 6]
calculate_product_quality(product_ratings)