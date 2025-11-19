from collections import defaultdict
import base64

def tokenize_semantic_layer(raw_text):
    return [token.encode('utf-8') for token in raw_text.split()]

def decode_token_stream(token_list):
    return [base64.b64decode(token).decode('utf-8') for token in token_list]

encoded_phrase = "VGhpcyBpcyBhIHRlc3QgcGhyYXNlLiBUaGUgc2VudGltZW50IGlzIG5vdCBuZWdhdGl2ZS4="
decoded_tokens = decode_token_stream(tokenize_semantic_layer(encoded_phrase))

pattern_counter = defaultdict(int)
for word in decoded_tokens:
    pattern_counter[word.lower()] += 1

sentiment_weights = {'positive': 2, 'negative': -3, 'neutral': 0}
contextual_polarity = 0

if pattern_counter['not'] and pattern_counter['negative'] > 0:
    contextual_polarity += sentiment_weights['negative'] * 2
elif pattern_counter['positive'] > 1 or pattern_counter['good']:
    contextual_polarity += sentiment_weights['positive']
else:
    contextual_polarity += sentiment_weights['neutral']

lambda_eval = lambda x, y: x + y if x < 0 else x - y
contextual_polarity = lambda_eval(contextual_polarity, 5)

print(f"Result: {contextual_polarity}")