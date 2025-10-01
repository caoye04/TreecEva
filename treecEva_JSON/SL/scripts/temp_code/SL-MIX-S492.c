#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

struct Point {
    double x;
    double y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

struct Circle {
    struct Point center;
    double radius;
};

union Shape {
    struct Rectangle rect;
    struct Circle circle;
};

enum ShapeType {
    RECTANGLE,
    CIRCLE
};

struct ShapeContainer {
    enum ShapeType type;
    union Shape shape;
};

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

double distance(struct Point p1, struct Point p2) {
    double dx = p1.x - p2.x;
    double dy = p1.y - p2.y;
    return sqrt(dx*dx + dy*dy);
}

int main() {
    // Initialize data structures
    struct ShapeContainer containers[2];
    
    // First container: rectangle
    containers[0].type = RECTANGLE;
    containers[0].shape.rect.topLeft.x = 0.0;
    containers[0].shape.rect.topLeft.y = 5.0;
    containers[0].shape.rect.bottomRight.x = 4.0;
    containers[0].shape.rect.bottomRight.y = 0.0;
    
    // Second container: circle
    containers[1].type = CIRCLE;
    containers[1].shape.circle.center.x = 3.0;
    containers[1].shape.circle.center.y = 3.0;
    containers[1].shape.circle.radius = 2.5;
    
    // Perform calculations
    double area_sum = 0.0;
    int i;
    
    for (i = 0; i < 2; i++) {
        if (containers[i].type == RECTANGLE) {
            double width = containers[i].shape.rect.bottomRight.x - containers[i].shape.rect.topLeft.x;
            double height = containers[i].shape.rect.topLeft.y - containers[i].shape.rect.bottomRight.y;
            area_sum += width * height;
        } else if (containers[i].type == CIRCLE) {
            area_sum += M_PI * containers[i].shape.circle.radius * containers[i].shape.circle.radius;
        }
    }
    
    // Bitwise and mathematical operations
    int bit_pattern = 0xF0A5 & 0x0F5A;
    int shifted_value = bit_pattern << 2;
    int xor_result = shifted_value ^ 0x1234;
    
    // Trigonometric calculations
    double angle_rad = M_PI / 4.0;  // 45 degrees
    double sin_val = sin(angle_rad);
    double cos_val = cos(angle_rad);
    double tan_val = tan(angle_rad);
    
    // Complex expression combining multiple operations
    double complex_expr = pow(sin_val, 3) + sqrt(fabs(cos_val)) * tan_val;
    
    // String manipulation simulation using character arrays
    char buffer[20] = "HelloWorld";
    int str_length = 0;
    while (buffer[str_length] != '\0') str_length++;
    
    // More mathematical computations
    int fact_6 = factorial(6);
    double log_val = log(area_sum);
    
    // Final computation sequence
    double intermediate = (area_sum * sin_val) + (fact_6 / log_val);
    
    // Conditional logic with multiple branches
    double selector = fmod(intermediate, 5.0);
    double final_computation;
    
    if (selector > 3.0) {
        final_computation = ceil(intermediate) + floor(complex_expr);
    } else if (selector > 1.0) {
        final_computation = round(intermediate) * sqrt(xor_result);
    } else {
        final_computation = trunc(intermediate) + fabs(complex_expr);
    }
    
    // Final result calculation
    int final_result = (int)(final_computation) % 1000;
    
    printf("Result: %d\n", final_result);
    
    return 0;
}