#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct Point {
    double x;
    double y;
};

struct Circle {
    struct Point center;
    double radius;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

union ShapeUnion {
    struct Circle circle;
    struct Rectangle rectangle;
};

struct Container {
    union ShapeUnion shapes[2];
    int shape_count;
    char labels[2][MAX_LEN];
};

int main() {
    // Initialize container
    struct Container container;
    container.shape_count = 2;
    
    // First shape - Circle
    container.shapes[0].circle.center.x = 3.0;
    container.shapes[0].circle.center.y = 4.0;
    container.shapes[0].circle.radius = 5.0;
    strcpy(container.labels[0], "Primary_Circle");
    
    // Second shape - Rectangle
    container.shapes[1].rectangle.topLeft.x = 0.0;
    container.shapes[1].rectangle.topLeft.y = 10.0;
    container.shapes[1].rectangle.bottomRight.x = 8.0;
    container.shapes[1].rectangle.bottomRight.y = 2.0;
    strcpy(container.labels[1], "Secondary_Rectangle");
    
    // Calculate area of circle
    double circle_area = M_PI * container.shapes[0].circle.radius * container.shapes[0].circle.radius;
    
    // Calculate area of rectangle
    double width = fabs(container.shapes[1].rectangle.bottomRight.x - container.shapes[1].rectangle.topLeft.x);
    double height = fabs(container.shapes[1].rectangle.topLeft.y - container.shapes[1].rectangle.bottomRight.y);
    double rectangle_area = width * height;
    
    // Calculate distance between centers
    double dx = container.shapes[0].circle.center.x - (container.shapes[1].rectangle.topLeft.x + container.shapes[1].rectangle.bottomRight.x) / 2;
    double dy = container.shapes[0].circle.center.y - (container.shapes[1].rectangle.topLeft.y + container.shapes[1].rectangle.bottomRight.y) / 2;
    double center_distance = sqrt(dx*dx + dy*dy);
    
    // Perform bit operations on label lengths
    int label1_len = strlen(container.labels[0]);
    int label2_len = strlen(container.labels[1]);
    int xor_result = label1_len ^ label2_len;
    int shifted_xor = xor_result << 2;
    
    // Complex calculation involving all computed values
    double intermediate = (circle_area + rectangle_area) * center_distance;
    long long scaled_intermediate = (long long)(intermediate * 100);
    
    // Apply modulo and bit operations
    long long mod_result = scaled_intermediate % 1000;
    long long bit_and_result = mod_result & 0xFF;
    
    // Final computation
    int final_result = (int)(bit_and_result + shifted_xor + (int)(container.shapes[0].circle.center.x * container.shapes[1].rectangle.bottomRight.y));
    
    printf("Result: %d\n", final_result);
    return 0;
}