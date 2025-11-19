from collections import defaultdict

def tokenize(sentence):
    return sentence.lower().split()

def get_modifier_type(word):
    if word.startswith('un'):
        return 'negation'
    elif word.endswith('ing'):
        return 'continuous'
    elif word in ['very', 'extremely', 'quite']:
        return 'intensifier'
    else:
        return 'neutral'

def calculate_base_weight(pos, modifier):
    base = pos * 2
    if modifier == 'negation':
        return -base
    elif modifier == 'intensifier':
        return base * 3
    elif modifier == 'continuous':
        return base + 1
    else:
        return base

def process_sentence(text):
    tokens = tokenize(text)
    weights = defaultdict(int)
    
    for idx, word in enumerate(tokens):
        if word == 'but':
            # Early return pattern - reset and only consider words after 'but'
            weights.clear()
            continue
            
        mod_type = get_modifier_type(word)
        weight = calculate_base_weight(idx+1, mod_type)
        
        # Conditional branch for special cases
        if word == 'not' and idx < len(tokens)-1:
            next_word_mod = get_modifier_type(tokens[idx+1])
            if next_word_mod != 'neutral':
                weight *= 2  # Double the impact of negated modifiers
        
        weights[word] += weight
        
        # Break condition for long sentences
        if len(weights) > 10:
            break
    
    # String transformation - remove neutral words with low weights
    filtered_weights = {k: v for k, v in weights.items() if v != 0}
    
    # Final aggregation with positional bonus
    aggregate_sentiment = 0
    for i, (word, weight) in enumerate(filtered_weights.items()):
        positional_bonus = i if weight > 0 else -i
        aggregate_sentiment += weight + positional_bonus
    
    return aggregate_sentiment

# Main execution
sentence = "quite exciting but not uninteresting"
aggregate_sentiment = process_sentence(sentence)
print(f"Result: {aggregate_sentiment}")