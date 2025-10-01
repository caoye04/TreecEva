#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

union Data {
    int i;
    float f;
    char str[20];
};

int calculateArea(struct Rectangle rect) {
    int width = abs(rect.bottomRight.x - rect.topLeft.x);
    int height = abs(rect.bottomRight.y - rect.topLeft.y);
    return width * height;
}

int main() {
    struct Rectangle rects[2];
    
    rects[0].topLeft.x = 3;
    rects[0].topLeft.y = 7;
    rects[0].bottomRight.x = 9;
    rects[0].bottomRight.y = 2;
    
    rects[1].topLeft.x = 1;
    rects[1].topLeft.y = 5;
    rects[1].bottomRight.x = 8;
    rects[1].bottomRight.y = 1;
    
    int areas[2];
    areas[0] = calculateArea(rects[0]);
    areas[1] = calculateArea(rects[1]);
    
    union Data d;
    d.i = areas[0] ^ areas[1]; // XOR of the two areas
    
    int base = 2;
    int exponent = d.i & 0x0F; // Lower 4 bits of the XOR result
    long long power_result = 1;
    for(int i = 0; i < exponent; i++) {
        power_result *= base;
    }
    
    double sqrt_val = sqrt(power_result);
    int truncated = (int)sqrt_val;
    
    int bit_count = 0;
    int temp = truncated;
    while(temp) {
        bit_count += temp & 1;
        temp >>= 1;
    }
    
    int result = (truncated << 2) | bit_count; // Left shift by 2 and OR with bit count
    
    printf("Result: %d\n", result);
    return 0;
}