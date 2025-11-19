from collections import defaultdict

def tokenize_stream(input_stream):
    tokens = []
    i = 0
    while i < len(input_stream):
        if input_stream[i] == '<':
            j = input_stream.find('>', i)
            if j != -1:
                tokens.append(('TAG', input_stream[i+1:j]))
                i = j + 1
                continue
        if input_stream[i].isalpha():
            j = i
            while j < len(input_stream) and input_stream[j].isalnum():
                j += 1
            tokens.append(('ID', input_stream[i:j]))
            i = j
            continue
        if input_stream[i].isdigit():
            j = i
            while j < len(input_stream) and input_stream[j].isdigit():
                j += 1
            tokens.append(('VAL', int(input_stream[i:j])))
            i = j
            continue
        i += 1
    return tokens

tag_weights = defaultdict(lambda: 1, {
    'bold': 3,
    'italic': 2,
    'underline': 4
})

transformers = {
    'ID': lambda x: x.upper(),
    'VAL': lambda x: x * 2,
    'TAG': lambda x: tag_weights[x]
}

token_categories = {
    'ID': 1,
    'VAL': 2,
    'TAG': 3
}

def process_tokens(tokens):
    score = 0
    for token_type, token_value in tokens:
        transformed = transformers[token_type](token_value)
        category = token_categories[token_type]
        match category:
            case 1:  # ID
                score += len(transformed)
            case 2:  # VAL
                score += transformed
            case 3:  # TAG
                score *= transformed
    return score

input_stream = "<bold>hello123<italic>world456"
tokens = tokenize_stream(input_stream)
final_score = process_tokens(tokens)
print(f"Result: {final_score}")