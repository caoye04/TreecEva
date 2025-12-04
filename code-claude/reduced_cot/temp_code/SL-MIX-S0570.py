from collections import Counter
import itertools

# Function to process survey data about favorite fruits
def process_survey_data(responses):
    # Count the occurrences of each fruit
    fruit_counts = Counter(responses)
    
    # Remove fruits with only one mention (considered outliers)
    filtered_fruits = [fruit for fruit in responses if fruit_counts[fruit] > 1]
    
    # Create a frequency counter for the filtered list
    filtered_frequencies = Counter(filtered_fruits)
    
    # Some fruits may appear multiple times in the elements expansion
    # We want to count unique fruits after filtering
    unique_count = len(set(filtered_frequencies.elements()))
    
    # Calculate average mentions per fruit for reporting
    avg_mentions = sum(filtered_frequencies.values()) / len(filtered_frequencies) if filtered_frequencies else 0
    
    return unique_count, avg_mentions

# Survey responses of favorite fruits
survey_data = ['apple', 'banana', 'apple', 'orange', 'banana', 
               'mango', 'kiwi', 'apple', 'banana', 'grape']

# Process the survey data
fruit_variety, average = process_survey_data(survey_data)

# Print the result
print(f"Result: {fruit_variety}")