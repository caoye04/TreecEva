text_data = "  data processing pipeline efficiency metrics  "
initial_count = len(text_data)
processed_count = len(text_data.strip().split()) * 2
print(f"Result: {processed_count}")