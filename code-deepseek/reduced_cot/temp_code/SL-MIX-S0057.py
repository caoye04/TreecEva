text_data = "algorithmic processing demonstration"
character_set = ['e', 's', 'm']
processed_text = text_data.upper().replace(' ', '_')
character_count = len(processed_text)
final_count = processed_text.count(character_set[0])
print(f"Result: {final_count}")