#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>

typedef struct {
    int values[4];
    double weight;
} DataBlock;

int main() {
    DataBlock blocks[2] = {{{10, 20, 30, 40}, 1.5}, {{50, 60, 70, 80}, 2.0}};
    int indices[4] = {3, 1, 0, 2};
    int temp = 0;
    double accumulator = 0.0;
    int result = 0;
    
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 4; j++) {
            int idx = indices[j];
            temp = blocks[i].values[idx] & 0x3F;
            temp = temp << 1;
            temp = temp ^ (int)(blocks[i].weight * 10);
            accumulator += sqrt((double)temp);
        }
        result += (int)floor(accumulator);
        accumulator = 0.0;
    }
    
    result = result ^ 0xAA;
    result = result & 0xFF;
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}