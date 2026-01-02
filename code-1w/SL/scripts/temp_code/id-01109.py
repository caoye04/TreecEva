from itertools import accumulate

def calculate_residual(segments, limit):
    peak_flows = [min(segment, limit) for segment in segments]
    flow_sum = sum(accumulate(peak_flows))
    total_capacity = limit * len(segments)
    residual_capacity = total_capacity - flow_sum
    return residual_capacity

def main():
    max_limit = 17
    flow_segments = [5, 12, 8, 20, 3]
    # Some auxiliary computation - minimal distraction
    avg_flow = sum(flow_segments) / len(flow_segments)
    normalized = [x / avg_flow for x in flow_segments]
    
    residual_capacity = calculate_residual(flow_segments, max_limit)
    
    # Final output
    print(f"Result: {residual_capacity}")

if __name__ == "__main__":
    main()