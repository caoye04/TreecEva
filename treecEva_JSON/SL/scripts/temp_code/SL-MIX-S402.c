#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define PI 3.14159265

int main() {
    int arr[4][4] = {
        {12, 25, 38, 49},
        {56, 63, 74, 81},
        {92, 105, 118, 129},
        {136, 147, 158, 169}
    };
    
    int *p = &arr[0][0];
    double trig_result = 0.0;
    int bitwise_accum = 0;
    int loop_counter = 0;
    int intermediate = 0;
    int target_result = 0;
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if ((i + j) % 2 == 0) {
                trig_result += sin((double)arr[i][j] * PI / 180.0);
                if (trig_result > 1.0) {
                    trig_result = 1.0;
                }
            } else {
                bitwise_accum ^= (arr[i][j] << 1) & 0xFF;
            }
            loop_counter++;
        }
    }
    
    intermediate = (int)(trig_result * 1000);
    
    if (intermediate > bitwise_accum) {
        target_result = (intermediate & bitwise_accum) | ((intermediate ^ bitwise_accum) >> 2);
    } else {
        target_result = (bitwise_accum & 0xF0) + ((intermediate | 0x0F) ^ 0xAA);
    }
    
    target_result += *(p + 5) - *(p + 10);
    
    printf("Target result: %d\n", target_result);
    
    return 0;
}