#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 5
#define PI 3.14159265359

typedef struct {
    int id;
    double value;
    int flags;
} Node;

typedef struct {
    Node nodes[MAX_NODES];
    int count;
} NodeList;

int main() {
    NodeList list = {
        .nodes = {
            {.id = 1, .value = 2.5, .flags = 0b1010},
            {.id = 2, .value = 3.7, .flags = 0b1100},
            {.id = 3, .value = 1.8, .flags = 0b0011},
            {.id = 4, .value = 4.2, .flags = 0b1111},
            {.id = 5, .value = 2.1, .flags = 0b0101}
        },
        .count = 5
    };
    
    double accumulator = 0.0;
    int mask = 0b1111;
    
    // First processing loop
    for (int i = 0; i < list.count; i++) {
        Node* node = &list.nodes[i];
        
        // Apply bitwise masking to flags
        node->flags &= mask;
        
        // Mathematical transformation based on node id and value
        double transformed = pow(node->value, 2) * sin(node->id * PI / 8);
        
        // Conditional accumulation
        if ((node->flags & 0b1000) && (node->id % 2 == 1)) {
            accumulator += transformed;
        } else if ((node->flags & 0b0001) || (node->value > 3.0)) {
            accumulator -= sqrt(transformed);
        }
    }
    
    // Second processing with nested loops
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int trace = 0;
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            // XOR operation with bitwise rotation
            int rotated = ((matrix[i][j] << 1) | (matrix[i][j] >> 3)) & 0xF;
            trace ^= rotated;
            
            // Update accumulator with matrix-based computation
            if (i == j) {  // Diagonal elements
                accumulator += log(fabs(accumulator) + 1) * matrix[i][j];
            }
        }
    }
    
    // String manipulation for additional complexity
    char buffer[50] = "ComplexComputation";
    int str_length = strlen(buffer);
    int char_sum = 0;
    
    for (int i = 0; i < str_length; i++) {
        char_sum += buffer[i];
    }
    
    // Final computation combining all previous results
    double result;
    // FINAL COMPUTATION
    result = (accumulator * trace) + (char_sum << 2) - (int)(fabs(accumulator) * 100);
    
    printf("Result: %.0f\n", result);
    return 0;
}