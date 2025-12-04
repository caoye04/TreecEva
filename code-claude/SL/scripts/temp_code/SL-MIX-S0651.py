# Calculate total points in a spelling bee competition

words = ['python', 'algorithm', 'function', 'variable', 'dictionary']

# Initialize tracking variables
difficulty_factor = 2
base_score = 5
processed_words = 0

# Calculate points for each word based on length and letter case
points = []
for word in words:
    # Count uppercase letters (though none exist in this list)
    uppercase_count = sum(1 for char in word if char.isupper())
    
    # Calculate word score based on length
    word_score = len(word) * base_score
    
    # Apply small adjustment for words ending with 'n'
    if word.endswith('n'):
        word_score += 3
        
    points.append(word_score)
    processed_words += 1

# Calculate total score
total_points = sum(points)

print(f"Result: {total_points}")