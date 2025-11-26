def process_results(input_data):
    base_score = len(input_data.strip().split())
    modifier = 1 if input_data.endswith('completed') else 0
    processed = input_data.upper().replace('TEST', 'RESULT')
    adjustment = len(processed) % 10
    return (base_score + modifier) * adjustment

data = "test case analysis completed"
final_score = process_results(data)
print(f"Target result: {final_score}")