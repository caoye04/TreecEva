#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

struct DataPoint {
    int values[3];
    double weight;
};

struct DataSet {
    struct DataPoint points[MAX_SIZE];
    int count;
    char label[20];
};

int main() {
    struct DataSet dataset;
    strcpy(dataset.label, "TestDataset");
    dataset.count = 5;
    
    // Initialize data points
    for (int i = 0; i < dataset.count; i++) {
        dataset.points[i].values[0] = i * 2 + 1;
        dataset.points[i].values[1] = i * 3 + 2;
        dataset.points[i].values[2] = i * 5 + 3;
        dataset.points[i].weight = sqrt(i + 1.0);
    }
    
    double weighted_sum = 0.0;
    int product_accum = 1;
    
    for (int i = 0; i < dataset.count; i++) {
        int local_sum = 0;
        for (int j = 0; j < 3; j++) {
            local_sum += dataset.points[i].values[j];
        }
        
        double weighted_local = local_sum * dataset.points[i].weight;
        weighted_sum += weighted_local;
        
        // Bitwise operations
        int xor_result = dataset.points[i].values[0] ^ dataset.points[i].values[1];
        product_accum *= (xor_result & 0xF); // Only consider lower 4 bits
    }
    
    // Complex calculation combining multiple operations
    int bit_shifted = (product_accum >> 2) | ((product_accum & 0x3) << 6);
    double trig_component = sin(weighted_sum / 100.0) * cos(weighted_sum / 50.0);
    
    // Final result computation
    int result = (int)(trig_component * 1000) + bit_shifted + (int)floor(weighted_sum);
    
    printf("Result: %d\n", result);
    return 0;
}