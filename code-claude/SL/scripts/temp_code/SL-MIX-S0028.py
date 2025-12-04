# Genetic analysis for disease susceptibility

# Patient genetic markers (represented as sets)
patient_a = {"BRCA1", "APOE", "TP53", "MTHFR", "COMT"}
patient_b = {"BRCA2", "APOE", "MTHFR", "PTEN"}

# Reference genetic markers for comparison
reference_markers = {"APOE", "TP53", "MTHFR", "BRCA1", "BRCA2"}

# Calculate genetic similarity between patients
all_markers = patient_a.union(patient_b)
total_markers = len(all_markers)

# Find markers present in both patients
common_genes = len(patient_a.intersection(patient_b))

# Calculate similarity percentage
similarity = (common_genes / total_markers) * 100

# Find markers in patients but not in reference
non_reference = all_markers - reference_markers

print(f"Result: {common_genes}")