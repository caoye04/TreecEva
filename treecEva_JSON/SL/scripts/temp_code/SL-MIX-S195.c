#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Circle {
    struct Point center;
    double radius;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

int main() {
    struct Circle c1 = {{10, 15}, 5.0};
    struct Rectangle r1 = {{5, 20}, {15, 10}};
    
    int a = 12, b = 7;
    double pi = 3.141592653589793238;
    
    // Step 1: Bitwise operations
    int step1 = (a << 2) ^ (b >> 1);
    
    // Step 2: Area calculations
    double circle_area = pi * c1.radius * c1.radius;
    int rect_width = r1.bottomRight.x - r1.topLeft.x;
    int rect_height = r1.topLeft.y - r1.bottomRight.y;
    int rect_area = rect_width * rect_height;
    
    // Step 3: Conditional logic with nested structures
    int conditional_value;
    if (c1.center.x > r1.topLeft.x && c1.center.y < r1.topLeft.y) {
        conditional_value = (int)(circle_area + rect_area);
    } else {
        conditional_value = (int)(circle_area - rect_area);
    }
    
    // Step 4: Complex arithmetic
    long long intermediate = (long long)step1 * conditional_value;
    double power_result = pow((double)intermediate, 0.5);
    
    // Step 5: Bit manipulation on result
    unsigned int shifted_result = ((unsigned int)power_result) << 3;
    unsigned int masked_result = shifted_result & 0xFF0F;
    
    // Step 6: Final calculation
    int target_result = (masked_result >> 4) + (int)(sin(pi/6) * 1000);
    
    printf("Target result: %d\n", target_result);
    return 0;
}