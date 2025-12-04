def process_text(text):
    # Apply some text transformations
    reversed_text = text[::-1]
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())
    
    # Calculate meaningless ratio (distraction)
    if len(text) > 0:
        ratio = uppercase_count / len(text)
    else:
        ratio = 0
    
    return reversed_text, uppercase_count, lowercase_count

def calculate_checksum(text):
    # Calculate a simple checksum
    checksum = 0
    for i, char in enumerate(text):
        # Use modular arithmetic with position influence
        checksum = (checksum + ord(char) * (i % 5 + 1)) % 1000
    
    # Apply some additional operations (partially distracting)
    factor = len(text) % 10 + 1
    checksum = (checksum * factor) % 1000
    
    return checksum

def calculate_final_score(encrypted_message):
    # Process the message
    reversed_message, upper_count, lower_count = process_text(encrypted_message)
    
    # Calculate primary score components
    base_score = len(encrypted_message) * 5
    modifier = upper_count - lower_count
    
    # Calculate checksum
    checksum = calculate_checksum(encrypted_message)
    
    # Some distracting calculations
    alternative_score = base_score + (modifier * 2)
    special_chars = sum(1 for char in encrypted_message if not char.isalnum())
    bonus_points = special_chars * 10
    
    # These variables aren't used in final calculation
    message_entropy = sum(ord(char) for char in encrypted_message) % 255
    complexity_factor = len(set(encrypted_message)) / max(1, len(encrypted_message))
    
    # Calculate final score
    if modifier > 0:
        final_score = base_score + checksum + (modifier * 3)
    else:
        final_score = base_score + checksum - (abs(modifier) * 2)
    
    return final_score

# Main execution
encrypted_message = "Hello123!@#"

# Some distracting operations
test_message = "Test" + encrypted_message[4:8]
backup_message = encrypted_message + "_backup"

# Calculate the final score
final_score = calculate_final_score(encrypted_message)

# Output the result
print(f"Result: {final_score}")