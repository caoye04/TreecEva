#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 10

struct DataPoint {
    int values[3];
    double weight;
};

typedef struct {
    struct DataPoint points[2];
    int count;
} DataSet;

int calculate_sum(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i] * (i + 1);
    }
    return sum;
}

double compute_weighted_avg(struct DataPoint dp) {
    double sum = 0.0;
    for(int i = 0; i < 3; i++) {
        sum += dp.values[i] * pow(1.5, i);
    }
    return sum / dp.weight;
}

int main() {
    DataSet dataset;
    dataset.count = 2;
    
    // Initialize first DataPoint
    dataset.points[0].values[0] = 4;
    dataset.points[0].values[1] = 7;
    dataset.points[0].values[2] = 2;
    dataset.points[0].weight = 3.0;
    
    // Initialize second DataPoint
    dataset.points[1].values[0] = 1;
    dataset.points[1].values[1] = 5;
    dataset.points[1].values[2] = 9;
    dataset.points[1].weight = 2.0;
    
    int intermediate_sums[2];
    for(int i = 0; i < dataset.count; i++) {
        intermediate_sums[i] = calculate_sum(dataset.points[i].values, 3);
    }
    
    double weighted_averages[2];
    for(int i = 0; i < dataset.count; i++) {
        weighted_averages[i] = compute_weighted_avg(dataset.points[i]);
    }
    
    int sum_of_sums = intermediate_sums[0] + intermediate_sums[1];
    double product_of_averages = weighted_averages[0] * weighted_averages[1];
    
    int bitwise_result = (sum_of_sums & 0xF) | ((int)product_of_averages >> 2);
    
    double trig_result = sin(bitwise_result) * cos(sum_of_sums);
    
    int final_result = (int)(trig_result * 1000) + (bitwise_result ^ sum_of_sums);
    
    printf("Result: %d\n", final_result);
    
    return 0;
}