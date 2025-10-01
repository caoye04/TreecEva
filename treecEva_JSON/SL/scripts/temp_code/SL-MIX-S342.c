#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    int values[5];
    double weight;
} DataBlock;

typedef struct {
    DataBlock* blocks;
    int count;
} Container;

int complex_calculation(int a, int b, int* ptr) {
    int temp = (a << 2) ^ b;
    *ptr = temp * 3;
    return (int)sqrt(fabs(*ptr));
}

void process_container(Container* c, double factor) {
    for (int i = 0; i < c->count; i++) {
        for (int j = 0; j < 5; j++) {
            c->blocks[i].values[j] = (int)(c->blocks[i].values[j] * factor) ^ (i + 1);
        }
        c->blocks[i].weight = sqrt(c->blocks[i].weight) * 2.5;
    }
}

int main() {
    // Initialize data structures
    DataBlock blocks[3] = {
        {{2, 4, 6, 8, 10}, 16.0},
        {{1, 3, 5, 7, 9}, 25.0},
        {{11, 13, 15, 17, 19}, 36.0}
    };
    
    Container cont = {blocks, 3};
    
    // Perform calculations
    int x = 12, y = 7;
    int* ptr = &y;
    
    x = complex_calculation(x, y, ptr);
    
    // Bitwise and arithmetic operations
    int mask = 0xF0;
    int shifted = (x & mask) >> 2;
    
    // Process container
    process_container(&cont, 1.5);
    
    // More calculations
    double accumulator = 0.0;
    for (int i = 0; i < cont.count; i++) {
        for (int j = 0; j < 5; j++) {
            accumulator += cont.blocks[i].values[j] * cont.blocks[i].weight;
        }
    }
    
    // Final computation sequence
    int final_result = (int)(accumulator / 100) + shifted;
    final_result ^= (cont.blocks[1].values[2] & 0xFF);
    final_result = (final_result << 1) | ((final_result >> 3) & 0x1F);
    
    // Execution point Y
    printf("Result: %d\n", final_result);
    return 0;
}