# Processing text messages to find average length of filtered messages
text_messages = [
    "Hello there!",
    "How are you doing today?",
    "OK",
    "See you at the meeting tomorrow.",
    "Yes",
    "Please send the documents when you can.",
    "No"
]

# Calculate the length of each message
message_lengths = [len(message) for message in text_messages]
print(f"Message lengths: {message_lengths}")

# Filter out short messages (less than 5 characters)
filtered_lengths = [length for length in message_lengths if length >= 5]
print(f"Filtered lengths: {filtered_lengths}")

# Find some statistics about our messages
max_length = max(message_lengths)
min_filtered = min(filtered_lengths)

# Calculate the average length of filtered messages
filtered_avg = sum(filtered_lengths) / len(filtered_lengths)

# Track message categories for reporting
short_messages = len(message_lengths) - len(filtered_lengths)
long_messages = len(filtered_lengths)

print(f"Result: {filtered_avg}")