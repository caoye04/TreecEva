import re
from collections import defaultdict

class WordStateMachine:
    def __init__(self):
        self.state = 'unseen'
    
    def process(self):
        if self.state == 'unseen':
            self.state = 'seen_once'
            return False
        elif self.state == 'seen_once':
            self.state = 'seen_twice'
            return False
        elif self.state == 'seen_twice':
            self.state = 'multiple_times'
            return True
        else:  # multiple_times
            return True

text_document = """functional programming embraces immutable data structures while object oriented programming favors mutable state changes"""

# Normalize and tokenize
tokens = re.findall(r'\b\w+\b', text_document.lower())
word_machines = {}
multiple_timers = set()

for token in tokens:
    if token not in word_machines:
        word_machines[token] = WordStateMachine()
    if word_machines[token].process():
        multiple_timers.add(token)

# Compute hash-based score from words that reached 'multiple_times' state
hash_scores = {word: hash(word) % 1000 for word in multiple_timers}
final_score = sum(hash_scores.values())

print(f"Result: {final_score}")