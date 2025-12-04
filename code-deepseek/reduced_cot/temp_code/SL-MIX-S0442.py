def validate_dataset_quality():
    validation_flags = [True, False, True, True, False]
    compliance_scores = [85, 92, 78, 95, 82]
    
    # Calculate data quality score using enumerate and zip
    data_quality_score = sum(val + score for idx, (val, score) in enumerate(zip(validation_flags, compliance_scores), start=1) if val)
    
    print(f"Target result: {data_quality_score}")

validate_dataset_quality()