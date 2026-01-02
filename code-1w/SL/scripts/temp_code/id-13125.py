from collections import Counter

def calculate_final_score(data):
    # Convert usernames to lowercase for consistency
    processed_names = [name.lower() for name in data['users']]
    
    # Count frequency of each character across all usernames
    char_counter = Counter()
    for name in processed_names:
        char_counter.update(name)
    
    # Calculate base score: sum of ASCII values of unique characters
    unique_chars = set(''.join(processed_names))
    base_score = sum(ord(c) for c in unique_chars)
    
    # Adjust score based on most common character (arbitrary heuristic)
    most_common_char, count = char_counter.most_common(1)[0]
    adjustment = ord(most_common_char) // 10
    
    # Final score computation
    final_score = base_score - adjustment
    return final_score

# Example user data (irrelevant keys included as mild distraction)
data_package = {
    'users': ['Alice', 'Bob', 'alice', 'Charlie', 'bob'],
    'version': '2.1',
    'active': True
}

# Execution point of interest
final_score = calculate_final_score(data_package)
print(f"Result: {final_score}")