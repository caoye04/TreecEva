# Email analysis function to count vowels in the subject line

def analyze_email_subject(subject):
    # Define the vowels to search for
    vowels = 'aeiou'
    
    # Initialize counters
    char_count = len(subject)
    space_count = subject.count(' ')
    text = subject.replace('-', '')
    
    # Count the vowels in the subject
    vowel_count = sum(text.lower().count(v) for v in vowels)
    
    # Calculate the consonant count (simplified approach)
    consonant_count = char_count - space_count - vowel_count
    
    return vowel_count, consonant_count

# Test with an example email subject
email_subject = "Data Analysis Report - Q2"
v_count, c_count = analyze_email_subject(email_subject)

print(f"Result: {v_count}")