text_input = 'analyze   data with multiple  spaces   between words'
processed_count = (lambda x: len(x.strip().split()) * (x.count('a') + x.count('e')))(text_input)
print(f"Result: {processed_count}")