def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.5]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(length):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:length]


def shift_cipher(text, offset):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result


def analyze_pattern(data, limit):
    count = 0
    running_sum = 0
    for i in range(len(data)):
        if i % 2 == 0 and data[i] > 0:
            count += 1
            running_sum += data[i]
    avg = running_sum / count if count != 0 else 0
    return int(avg * 100)

# Irrelevant test data
noise_floor = [0.1, -0.3, 0.05, 0.2, -0.7, 0.01]
dummy_text = "Encrypt this!"
offset_key = 7
cipher_test = shift_cipher(dummy_text, offset_key)

# Real signal input
raw_input = [-2.1, 3.5, 0.0, -1.8, 4.2, 2.9, -3.3, 1.4, 0.2, 5.1]
processed = preprocess_signal(raw_input)

# Transform via slicing and reversal
reversed_half = processed[::-1]
mirrored = reversed_half[:len(processed)//2]
completed = mirrored + processed
shifted = [x + 0.1 for x in completed]

# Threshold logic
threshold = len(shifted) * 0.75

# Generate Fibonacci-based weights (unused distractor)
fib_weights = generate_sequence(len(shifted))
scaled_weights = [w * 0.01 for w in fib_weights]

# Actual transformation: slice and scale
central_slice = shifted[2:6]
transformed_data = [round(x * 2.5, 3) for x in central_slice]

# Final diagnostic computation
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")