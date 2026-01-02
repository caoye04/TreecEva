text = 'hello world welcome to the hello world of programming'
words = text.split()

# Track word frequencies
greeting_text = 'hello hi welcome greetings'
greeting_words = greeting_text.split()

# Using enumerate to find positions of initial occurrences
first_occurrences = {word: idx for idx, word in enumerate(words) if word not in words[:idx]}

# Set operations to find overlap between greeting-related words and processed text
common_greetings = set(greeting_words)
unique_words = set(words)

# Key computational step
result = len(common_greetings & unique_words)

print(f'Result: {result}')