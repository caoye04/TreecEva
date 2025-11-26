text = "Product ID: ABC123-XYZ456"
non_alpha_count = sum(1 for c in text if not c.isalpha())
total_digits = sum(1 for c in text if c.isdigit())
print(f"Result: {total_digits}")