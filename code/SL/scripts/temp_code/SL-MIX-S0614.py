text = "  DataAnalysis 2024  "
base_count = len(text)
processed_count = len(text.strip()) if text.strip().isalpha() else len(text.strip().replace(" ", ""))
print(f"Result: {processed_count}")