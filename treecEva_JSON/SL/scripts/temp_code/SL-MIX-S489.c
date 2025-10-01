#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 10

typedef struct {
    double values[3];
    int count;
} DataArray;

typedef struct {
    DataArray arrays[2];
    char tag[10];
    int id;
} Node;

int main() {
    Node nodes[MAX_NODES];
    
    // Initialize nodes
    for (int i = 0; i < MAX_NODES; i++) {
        sprintf(nodes[i].tag, "NODE%d", i);
        nodes[i].id = i * 3 + 7;
        
        // Initialize first DataArray
        nodes[i].arrays[0].count = 3;
        for (int j = 0; j < 3; j++) {
            nodes[i].arrays[0].values[j] = pow(i + 1, j + 1) * (j % 2 == 0 ? 1 : -1);
        }
        
        // Initialize second DataArray
        nodes[i].arrays[1].count = 2;
        nodes[i].arrays[1].values[0] = sqrt(nodes[i].id);
        nodes[i].arrays[1].values[1] = log(nodes[i].id + 1);
    }
    
    double accumulator = 0;
    int xor_result = 0;
    
    // Complex processing loop
    for (int i = 0; i < MAX_NODES - 2; i++) {
        // Perform bitwise operations
        xor_result ^= (nodes[i].id & 0xF) << (i % 4);
        
        // Mathematical transformations
        double temp1 = nodes[i].arrays[0].values[1] * nodes[i+1].arrays[1].values[0];
        double temp2 = nodes[i+2].arrays[0].values[2] / (nodes[i].arrays[1].values[1] + 1);
        
        // Trigonometric operations
        double trig_result = sin(temp1) * cos(temp2);
        
        // Accumulate with conditional logic
        if (trig_result > 0) {
            accumulator += trig_result * 10;
        } else {
            accumulator -= fabs(trig_result) * 5;
        }
        
        // String-based conditional
        if (strlen(nodes[i].tag) > 5) {
            accumulator *= 1.1;
        }
    }
    
    // Final complex calculation
    double intermediate = pow(accumulator, 1.0/3.0) + xor_result;
    
    // TARGET ASSIGNMENT
    int target_result = (int)(intermediate * 1000) % 997;
    
    printf("Result: %d\n", target_result);
    
    return 0;
}