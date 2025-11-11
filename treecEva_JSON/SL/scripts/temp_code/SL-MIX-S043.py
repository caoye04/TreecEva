import math
from contextlib import contextmanager

def tokenize_signal(signal_data):
    return [ord(c) for c in signal_data]

def process_with_lambda(tokens):
    transform = lambda x: (x >> 2) & 0x3F if x > 100 else (x << 1) & 0xFF
    return [transform(token) for token in tokens]

@contextmanager
def processing_stage(name):
    print(f"Starting {name}")
    yield
    print(f"Finished {name}")

class SignalProcessor:
    def __init__(self):
        self.stages = []
    
    def add_stage(self, stage_name):
        self.stages.append(stage_name)
    
    def get_stage_count(self):
        return len(self.stages)

def categorize_result(value):
    # Switch-like structure using dictionary
    switch = {
        0: lambda: value * 2,
        1: lambda: value + 10,
        2: lambda: value - 5,
        3: lambda: value // 3,
        4: lambda: int(math.sqrt(value)) if value >= 0 else 0
    }
    
    category = (value // 10) % 5
    return switch.get(category, lambda: 0)()

def main():
    input_signal = "HelloAudio"
    processor = SignalProcessor()
    
    with processing_stage("Tokenization"):
        tokenized = tokenize_signal(input_signal)
        processor.add_stage("Tokenization")
    
    with processing_stage("Lambda Transformation"):
        transformed = process_with_lambda(tokenized)
        processor.add_stage("Lambda Transformation")
    
    matrix = [[transformed[i+j] if i+j < len(transformed) else 0 for j in range(3)] for i in range(0, len(transformed), 3)]
    
    flattened = [item for row in matrix for item in row]
    aggregated = sum(flattened) // len(flattened)
    
    processor.add_stage("Matrix Aggregation")
    
    final_category_score = categorize_result(aggregated) * processor.get_stage_count()
    
    print(f"Result: {final_category_score}")

if __name__ == "__main__":
    main()