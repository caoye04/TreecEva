#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int compute_series(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += (int)pow(i, 2);
    }
    return sum;
}

int bitwise_transform(int x, int y) {
    return (x << 2) ^ (y >> 1) & 0xFF;
}

int main() {
    double pi = 3.141592653589793;
    int a = 12, b = 7, c = 5;
    int array[4] = {3, 8, 2, 11};
    char text[] = "HELLO";
    
    int stage1 = (int)(sin(pi/6) * 100 + 0.5);  // sin(30°) = 0.5
    int stage2 = compute_series(4);  // 1^2 + 2^2 + 3^2 + 4^2 = 30
    int stage3 = bitwise_transform(a, b);  // (12 << 2) ^ (7 >> 1) & 0xFF = 48 ^ 3 & 255 = 51
    
    int condition = (stage1 > 40) && (stage2 < 50 || stage3 == 51);
    int selector = condition ? array[2] : array[0];
    
    int loop_result = 0;
    for (int i = 0; i < strlen(text); i++) {
        loop_result += (text[i] - 'A' + 1) * c;
    }
    
    int complex_calc = (stage1 * stage2) / (stage3 - selector) + loop_result;
    
    int mask = 0xF0;
    int masked_value = complex_calc & mask;
    
    double ratio = (double)stage2 / stage1;
    int scaled_ratio = (int)(ratio * 10);
    
    // TARGET ASSIGNMENT
    int result = (masked_value ^ scaled_ratio) + (condition << 3);
    
    printf("Result: %d\n", result);
    return 0;
}