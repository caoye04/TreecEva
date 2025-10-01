#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct ComplexData {
    int values[5];
    double weights[5];
    char label[20];
};

struct Container {
    struct ComplexData data[3];
    int count;
};

int process_values(struct ComplexData* cd) {
    int sum = 0;
    for(int i = 0; i < 5; i++) {
        sum += (int)(cd->values[i] * cd->weights[i]);
    }
    return sum;
}

int main() {
    struct Container container;
    container.count = 3;
    
    // Initialize first data set
    strcpy(container.data[0].label, "Dataset_A");
    int vals1[] = {2, 4, 6, 8, 10};
    double weights1[] = {0.5, 1.5, 2.0, 0.25, 1.0};
    for(int i = 0; i < 5; i++) {
        container.data[0].values[i] = vals1[i];
        container.data[0].weights[i] = weights1[i];
    }
    
    // Initialize second data set
    strcpy(container.data[1].label, "Dataset_B");
    int vals2[] = {1, 3, 5, 7, 9};
    double weights2[] = {1.0, 0.5, 1.5, 2.0, 0.75};
    for(int i = 0; i < 5; i++) {
        container.data[1].values[i] = vals2[i];
        container.data[1].weights[i] = weights2[i];
    }
    
    // Initialize third data set
    strcpy(container.data[2].label, "Dataset_C");
    int vals3[] = {10, 20, 30, 40, 50};
    double weights3[] = {0.1, 0.2, 0.3, 0.4, 0.5};
    for(int i = 0; i < 5; i++) {
        container.data[2].values[i] = vals3[i];
        container.data[2].weights[i] = weights3[i];
    }
    
    // Process all datasets
    int results[3];
    for(int i = 0; i < container.count; i++) {
        results[i] = process_values(&container.data[i]);
    }
    
    // Perform complex calculation
    double intermediate = pow(results[0], 1.5) + sqrt(results[1]) * log(results[2] + 1);
    
    // Bitwise operations
    int mask = (results[0] & 0xF0) | (results[1] >> 2) ^ results[2];
    
    // Final calculation
    int final_result = ((int)intermediate) & mask;
    
    // Apply rotation
    final_result = (final_result << 3) | (final_result >> (sizeof(int)*8-3));
    
    printf("Result: %d\n", final_result);
    return 0;
}