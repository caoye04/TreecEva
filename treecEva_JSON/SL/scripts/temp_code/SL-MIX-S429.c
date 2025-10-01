#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

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
    // Initialize circle
    struct Circle c = {{10, 15}, 5.0};
    
    // Initialize rectangle
    struct Rectangle r = {{5, 25}, {20, 5}};
    
    // Calculate area of circle using integer parts of coordinates
    int cx = c.center.x;
    int cy = c.center.y;
    double area_circle = M_PI * c.radius * c.radius;
    
    // Perform some bitwise operations
    int bitwise_op = (cx & 0xF) | ((cy >> 2) ^ 0x7);
    
    // Manipulate rectangle dimensions
    int width = r.bottomRight.x - r.topLeft.x;
    int height = r.topLeft.y - r.bottomRight.y;
    int perimeter_rect = 2 * (width + height);
    
    // Compute intermediate results
    double sqrt_area = sqrt(area_circle);
    int int_sqrt = (int)sqrt_area;
    
    // More complex calculation mixing everything
    int mixed_calc = ((perimeter_rect << 1) & 0xFF) + (bitwise_op % 7) * int_sqrt;
    
    // Final computation stage
    int final_step_1 = mixed_calc / 3;
    int final_step_2 = final_step_1 + (width ^ height);
    int final_result = final_step_2 - (int)(c.radius);
    
    printf("Result: %d\n", final_result);
    return 0;
}