#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>

typedef struct {
    int values[4];
    double metrics[3];
} DataBlock;

int main() {
    DataBlock block;
    int i, j;
    double accumulator = 0.0;
    long long composite = 0;
    
    // Initialize array values
    for (i = 0; i < 4; i++) {
        block.values[i] = (i + 1) * 7 + (i % 2 ? -3 : 5);
    }
    
    // Perform mathematical operations
    for (j = 0; j < 3; j++) {
        block.metrics[j] = pow(block.values[j] * 0.5, 2) + sin(M_PI / 6);
        accumulator += block.metrics[j];
    }
    
    // Bitwise manipulations with array data
    for (i = 0; i < 4; i++) {
        int temp = block.values[i] << (i % 3);
        composite ^= temp;
    }
    
    // Complex calculation using both arrays
    int result = 0;
    for (i = 0; i < 3; i++) {
        double factor = block.metrics[i] / accumulator;
        int component = (int)(factor * 1000) & 0xFF;
        result += (component ^ block.values[i]) + (composite >> (i * 2));
    }
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}