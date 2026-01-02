from collections import Counter


def analyze_frequency(text: str) -> dict:
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return Counter(cleaned)


def compute_uniqueness(freq_dict: dict) -> float:
    total_chars = sum(freq_dict.values())
    unique_chars = len([char for char, count in freq_dict.items() if count == 1])
    return round(unique_chars / total_chars, 4) if total_chars > 0 else 0.0


def calculate_score(content: str) -> int:
    frequencies = analyze_frequency(content)
    uniqueness = compute_uniqueness(frequencies)
    score = int(uniqueness * 100)
    
    # Irrelevant helper (minimal distraction)
    temp_debug = [k for k, v in frequencies.items() if v > 2]
    
    return score

# Main execution
text_data = "Dynamic programming solves complex problems by breaking them into simpler subproblems."
result = calculate_score(text_data)
print(f"Result: {result}")