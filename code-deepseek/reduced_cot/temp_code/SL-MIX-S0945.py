def process_reviews(reviews):
    # Convert ratings to lowercase and strip whitespace
    cleaned_reviews = list(map(lambda x: x.strip().lower(), reviews))
    
    # Filter valid ratings (numeric strings)
    valid_ratings = list(filter(lambda x: x.isdigit(), cleaned_reviews))
    
    # Convert to integers and calculate average
    if valid_ratings:
        numeric_ratings = list(map(int, valid_ratings))
        average_rating = sum(numeric_ratings) / len(numeric_ratings)
        return round(average_rating, 2)
    else:
        return 0.0

review_data = ['4', ' 5 ', '3', 'invalid', '2', ' 4 ']
final_rating = process_reviews(review_data)
print(f"Result: {final_rating}")