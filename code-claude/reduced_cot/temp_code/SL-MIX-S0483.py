def process_tags(tags_string):
    # Extract tags and count them
    if not tags_string:
        return 0
    tags = tags_string.split(',')
    unique_tags = set(tags)
    return len(unique_tags)

def calculate_importance(text):
    # Calculate importance based on text characteristics
    word_count = len(text.split())
    character_count = len(text)
    importance = word_count * 0.6 + character_count * 0.1
    return importance

# Sample text data with tags
text_data = "Machine learning algorithms require extensive data preprocessing, feature engineering, and model validation #AI,#DataScience,#ML,#AI"

# Process text characteristics
words = text_data.split()
word_count = len(words)

# Extract hashtags for processing
tags_part = text_data.split('#')[1:] if '#' in text_data else []
tags_string = ','.join([tag.strip() for tag in tags_part])

# Calculate text metrics
character_density = len(text_data) / (word_count + 1)
long_words = len([w for w in words if len(w) > 7])

# Set importance factors
importance_base = 25
importance_factor = 3

# Lambda function for priority calculation
calculate_weight = lambda x, y: (x * 2 + y) // 3

# Process tags from the text
tag_count = process_tags(tags_string)
distracting_metric = character_density * long_words

# Calculate priority based on various factors
def calculate_priority(text, factor):
    importance = calculate_importance(text)
    base_priority = importance + tag_count * 5
    weighted_priority = calculate_weight(base_priority, importance_base)
    
    # Apply adjustments based on factor
    adjusted_priority = weighted_priority * (factor / 2)
    
    # Round to nearest integer
    return round(adjusted_priority)

# Calculate final priority
final_priority = calculate_priority(text_data, importance_factor)

# Display the result
print(f"Result: {final_priority}")