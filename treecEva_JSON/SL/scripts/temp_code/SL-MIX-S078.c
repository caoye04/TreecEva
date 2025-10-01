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
    struct Rectangle r = {{5, 20}, {15, 10}};
    
    // Calculate area of circle using bit shifting for multiplication by π (approximated)
    double pi_approx = (355.0 / 113.0); // Very close approximation of π
    long long scaled_pi = (long long)(pi_approx * (1LL << 32)); // Scale π to integer
    long long scaled_radius_sq = (long long)(c.radius * c.radius * (1LL << 32)); // Scale radius squared
    long long area_scaled = (scaled_pi * scaled_radius_sq) >> 32; // Multiply and scale back
    int circle_area = (int)(area_scaled);
    
    // Calculate perimeter of rectangle using XOR swap and absolute values
    int width = r.bottomRight.x ^ r.topLeft.x ^ (r.bottomRight.x & r.topLeft.x);
    int height = r.topLeft.y ^ r.bottomRight.y ^ (r.topLeft.y & r.bottomRight.y);
    if(width < 0) width = -width;
    if(height < 0) height = -height;
    int perimeter = 2 * (width + height);
    
    // Perform a complex calculation mixing both results
    int intermediate = ((circle_area & 0xFF) << 4) | (perimeter & 0xF);
    int shifted_intermediate = intermediate >> 2;
    
    // Apply trigonometric function
    double angle_rad = M_PI / 4.0;
    double sin_val = sin(angle_rad);
    int sin_scaled = (int)(sin_val * 1000);
    
    // Final computation
    int final_result = (shifted_intermediate * sin_scaled) % 256;
    
    printf("Result: %d\n", final_result);
    return 0;
}