def analyze_text_properties(text1, text2):
    # Convert texts to sets for analysis
    set1 = set(text1.lower())
    set2 = set(text2.lower())
    
    # Find common and unique characters
    common = set1.intersection(set2)
    unique_to_first = set1 - set2
    unique_to_second = set2 - set1
    
    # Calculate some metrics that may be useful
    total_unique = len(set1.union(set2))
    similarity_ratio = len(common) / total_unique if total_unique > 0 else 0
    
    # Count alphanumeric characters
    alphanumeric_count = sum(1 for c in common if c.isalnum())
    
    return {
        "common": common,
        "unique_first": unique_to_first,
        "unique_second": unique_to_second,
        "similarity": similarity_ratio,
        "alphanumeric": alphanumeric_count
    }

# Sample texts for analysis
sample1 = "Python programming is fun!"
sample2 = "Programming in Python is enjoyable."
sample3 = "Java development can be challenging."

# Process the samples
result1 = analyze_text_properties(sample1, sample2)
result2 = analyze_text_properties(sample1, sample3)
result3 = analyze_text_properties(sample2, sample3)

# Extract metrics for comparison
similarity_12 = result1["similarity"] * 100
similarity_13 = result2["similarity"] * 100
similarity_23 = result3["similarity"] * 100

# Determine which texts are most similar
most_similar = max(similarity_12, similarity_13, similarity_23)
if most_similar == similarity_12:
    text_analysis = result1
elif most_similar == similarity_13:
    text_analysis = result2
else:
    text_analysis = result3

# Calculate additional metrics
unique_chars = len(text_analysis["unique_first"]) + len(text_analysis["unique_second"])
total_chars = unique_chars + len(text_analysis["common"])

# This is the key statement
common_chars = len(text_analysis["common"])

# Some additional processing that doesn't affect the result
metric_a = unique_chars * 2 - common_chars
metric_b = total_chars - unique_chars
final_score = metric_a + metric_b if metric_a > metric_b else metric_b - metric_a

print(f"Result: {common_chars}")