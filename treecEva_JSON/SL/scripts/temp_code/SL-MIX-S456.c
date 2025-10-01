#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

struct DataPoint {
    int values[3];
    double weight;
};

struct ComplexRecord {
    struct DataPoint points[2];
    char label[20];
    int count;
};

int calculate_weighted_sum(struct DataPoint* dp) {
    return (int)(dp->values[0] * dp->weight + dp->values[1] * sin(dp->weight) + dp->values[2] * cos(dp->weight));
}

int process_records(struct ComplexRecord records[], int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < records[i].count; j++) {
            total += calculate_weighted_sum(&records[i].points[j]);
        }
    }
    return total;
}

int main() {
    struct ComplexRecord dataset[2];
    
    // Initialize first record
    strcpy(dataset[0].label, "Primary");
    dataset[0].count = 2;
    dataset[0].points[0].values[0] = 5;
    dataset[0].points[0].values[1] = 3;
    dataset[0].points[0].values[2] = 7;
    dataset[0].points[0].weight = 1.2;
    dataset[0].points[1].values[0] = 2;
    dataset[0].points[1].values[1] = 8;
    dataset[0].points[1].values[2] = 4;
    dataset[0].points[1].weight = 0.8;
    
    // Initialize second record
    strcpy(dataset[1].label, "Secondary");
    dataset[1].count = 1;
    dataset[1].points[0].values[0] = 6;
    dataset[1].points[0].values[1] = 1;
    dataset[1].points[0].values[2] = 9;
    dataset[1].points[0].weight = 2.5;
    
    int intermediate_result = process_records(dataset, 2);
    
    // Perform bit operations
    int bit_result = (intermediate_result & 0xF) | ((intermediate_result >> 4) ^ 0x3);
    
    // Mathematical transformations
    double trig_result = sin(bit_result) * cos(bit_result/2.0);
    int final_calc = (int)(trig_result * 1000) + 0x1A;
    
    // TARGET ASSIGNMENT
    int target_result = ((final_calc << 2) & 0xFF) ^ (final_calc >> 3);
    
    printf("Result: %d\n", target_result);
    return 0;
}