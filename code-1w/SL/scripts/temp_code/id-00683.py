def analyze_genomic_data():
    # Gene sets from two different studies
    study_a_genes = {"BRCA1", "TP53", "MYC", "KRAS", "APC", "PTEN"}
    study_b_genes = {"EGFR", "ALK", "ROS1", "BRAF", "TP53", "MET"}

    # Simulated patient-specific mutation data
    patient_mutations = ["EGFR", "TP53", "MYC", "PIK3CA", "BRCA1"]
    mutated_genes = set(patient_mutations)

    # Core overlapping genes between the two studies
    common_genes = study_a_genes.intersection(study_b_genes)

    # Irrelevant distraction: unused variable (minimal interference)
    control_group_size = 128

    # Scaling factor based on cohort size
    cohort_size = 256
    scaling_factor = cohort_size / 64

    # Key computation step
    result = len(common_genes.intersection(mutated_genes)) * scaling_factor

    # Output the result as required
    print(f"Result: {result}")

analyze_genomic_data()