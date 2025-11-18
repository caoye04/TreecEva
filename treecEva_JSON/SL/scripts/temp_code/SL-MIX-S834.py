import re
from functools import reduce

def process_feedback(feedback_entries):
    # Extract numeric sentiment values using regex
    sentiment_values = [int(re.search(r'value:(-?\d+)', entry).group(1)) for entry in feedback_entries]
    
    # Filter out neutral sentiments (0 values)
    non_zero_sentiments = list(filter(lambda x: x != 0, sentiment_values))
    
    # Square each sentiment value
    squared_sentiments = list(map(lambda x: x**2, non_zero_sentiments))
    
    # Sum all squared values
    final_sentiment_score = reduce(lambda a, b: a + b, squared_sentiments, 0)
    
    return final_sentiment_score

# Sample feedback entries with encoded sentiment values
feedback_data = [
    "FeedbackID:001|value:3|type:positive",
    "FeedbackID:002|value:0|type:neutral",
    "FeedbackID:003|value:-2|type:negative",
    "FeedbackID:004|value:4|type:positive",
    "FeedbackID:005|value:0|type:neutral"
]

final_sentiment_score = process_feedback(feedback_data)
print(f"Result: {final_sentiment_score}")