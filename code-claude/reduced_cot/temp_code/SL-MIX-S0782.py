# Video analytics processing for a content creator channel
video_titles = ["Introduction", "Basic Tutorial", "Advanced Tips", "Expert Guide", "Q&A Session"]
video_stats = [1200, 3450, 2800, 1900, 3200]

# Metadata for processing
creator_name = "TechTutor"
channel_age_days = 365

# Process videos from the middle section
start_idx = 1
end_idx = 4

# Extract relevant segment and calculate stats
selected_titles = video_titles[start_idx:end_idx]
max_views = max(video_stats[start_idx:end_idx])
min_views = min(video_stats[start_idx:end_idx])

# Calculate total views for the selected segment
total_views = sum(video_stats[start_idx:end_idx])

# Average views per video (all videos)
avg_all = sum(video_stats) / len(video_stats)

# Display results
print(f"Selected videos: {selected_titles}")
print(f"View statistics - Max: {max_views}, Min: {min_views}")
print(f"Total views for selected segment: {total_views}")
