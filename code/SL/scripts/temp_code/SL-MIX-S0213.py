data_entries = ["file1.txt", "document.pdf", "image.jpg", "data.csv", "notes.txt", "archive.zip"]
file_extensions = []
for entry in data_entries:
    if "." in entry:
        file_extensions.append(entry.split(".")[-1])
text_files = [ext for ext in file_extensions if ext == "txt"]
valid_entries = [entry for entry in data_entries if entry.endswith(".txt") or entry.endswith(".csv")]
final_count = len(valid_entries)
print(f"Result: {final_count}")