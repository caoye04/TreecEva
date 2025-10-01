#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

int main() {
    int arr[4][4] = {{2, 4, 8, 16}, {3, 9, 27, 81}, {1, 5, 25, 125}, {6, 36, 216, 1296}};
    int i, j;
    int temp = 0;
    int mask = 0xF0;
    double sum_log = 0.0;
    int result = 0;
    
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if ((i * j) % 2 == 0) {
                arr[i][j] = arr[i][j] ^ (mask >> (i + j));
            } else {
                arr[i][j] = arr[i][j] & (mask << (i - j));
            }
            
            if (arr[i][j] > 100) {
                sum_log += log((double)arr[i][j]);
            }
        }
    }
    
    for (i = 0; i < 4; i++) {
        temp = 0;
        for (j = 0; j < 4; j++) {
            temp += arr[j][i];
        }
        result ^= (int)(temp * cos(M_PI / 4));
    }
    
    result = result >> 2;
    result += (int)floor(sum_log);
    
    printf("Result: %d\n", result);
    return 0;
}