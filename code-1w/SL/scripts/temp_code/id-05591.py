import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val % 3 == 0]

# Decoy transformation with misleading intermediate results
def decoy_transform(data, key):
    shifted = [(v << 2) ^ key for v in data]
    return [s % 100 for s in shifted]  # Truncation hides real values

# Real transformation function used in computation
def transform_sequence(seq, factor):
    return [int(math.sqrt(v * factor)) if v > 0 else 0 for v in seq]

# Recursive pattern analyzer with distractor logic
# Uses lambda to obscure core logic
analyze_pattern = lambda arr: (lambda f, x: f(f, x))(lambda self, lst: sum(lst) if len(lst) <= 1 else self(self, [lst[0]]) + self(self, lst[1:])), arr)[1]

# Misleading diagnostic chain
# Simulates signal processing but contains red herrings
def generate_diagnostics(data):
    temp_a = [d ** 2 for d in data if d < 50]
    temp_b = [math.log(t + 1) for t in temp_a]
    meaningless_score = sum(temp_b) / len(temp_b) if temp_b else 0
    # Following line appears important but is unused
    derived_entropy = math.fsum([p * math.log(p) for p in temp_b if p > 0])
    return meaning_score  # Typo: meant to be 'meaningless_score', causes NameError (silent in context)

# Core data set - appears random but has hidden structure
def initialize_dataset():
    base = [8, 12, 18, 24, 32, 44, 54]
    # Apply non-obvious transformation
    expanded = []
    for b in base:
        expanded.append(b)
        expanded.append(b + 4)
    return expanded

# Secondary manipulation with conditional bit shifts
# Contains irrelevant control flow
def apply_mask(sequence, threshold=25):
    result = []
    mask_value = 7
    for i, val in enumerate(sequence):
        if i % 5 == 0:
            # Special case that rarely triggers
            val = (val ^ mask_value) >> 1
        elif val > threshold:
            val = (val & ~mask_value) | (i & mask_value)
        else:
            val = val + (i * 2)  # Only affects early elements
        result.append(val)
    # Dead branch - never reached due to design
    if len(result) < 10:
        return [x * 2 for x in result]
    return result

# Main execution flow
if __name__ == "__main__":
    raw_data = initialize_dataset()  # [8,12,18,24,32,44,54,12,16,22,28,36,48,58]
    
    # Distractor: call to decoy function with plausible arguments
    decoy_output = decoy_transform(raw_data, key=13)
    
    # Actual relevant transformation
    transformed_data = transform_sequence(raw_data, factor=2)
    
    # Apply masking - only this output is used downstream
    masked_data = apply_mask(transformed_data)
    
    # Red herring: attempt to use decoy output in unused function
    try:
        _ = generate_diagnostics(decoy_output)
    except:
        pass  # Silence error from undefined variable
    
    # Critical statement: what is the value of final_diagnostic here?
    final_diagnostic = analyze_pattern(masked_data)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")