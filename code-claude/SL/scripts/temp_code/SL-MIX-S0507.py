import itertools

# Customer satisfaction ratings for different products
ratings = [3, 4, 2, 5, 1, 4, 3, 5, 2]

# Threshold for considering a rating as positive
positive_threshold = 4

# Calculate average rating
average_rating = sum(ratings) / len(ratings)
print(f"Average rating: {average_rating}")

# Use lambda with filter to get ratings above positive threshold
filter_result = list(filter(lambda x: x >= positive_threshold, ratings))

# Count the occurrences of each rating using itertools
rating_counts = [(key, len(list(group))) for key, group in itertools.groupby(sorted(ratings))]
print(f"Rating distribution: {rating_counts}")

# Calculate the sum of filtered positive ratings
filtered_sum = sum(filter_result)

# Get the percentage of positive ratings
positive_percentage = (len(filter_result) / len(ratings)) * 100
print(f"Positive ratings percentage: {positive_percentage}%")

# Calculate weighted score based on positive ratings
weighted_score = filtered_sum / len(filter_result) if filter_result else 0

print(f"Result: {filtered_sum}")