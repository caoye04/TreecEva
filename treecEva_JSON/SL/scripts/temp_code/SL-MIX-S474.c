#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    double x;
    double y;
} Point;

typedef struct {
    Point points[3];
    int count;
} Triangle;

int main() {
    Triangle t = {{{1.0, 2.0}, {4.0, 6.0}, {7.0, 3.0}}, 3};
    
    // Step 1: Calculate centroid
    double cx = 0, cy = 0;
    for(int i = 0; i < t.count; i++) {
        cx += t.points[i].x;
        cy += t.points[i].y;
    }
    cx /= t.count;
    cy /= t.count;
    
    // Step 2: Calculate distances from centroid to each point
    double distances[3];
    for(int i = 0; i < t.count; i++) {
        double dx = t.points[i].x - cx;
        double dy = t.points[i].y - cy;
        distances[i] = sqrt(dx*dx + dy*dy);
    }
    
    // Step 3: Find maximum distance
    double max_dist = distances[0];
    for(int i = 1; i < t.count; i++) {
        if(distances[i] > max_dist)
            max_dist = distances[i];
    }
    
    // Step 4: Perform bit operations on integer representation
    int bits = (int)(max_dist * 1000); // Scale to preserve precision
    bits = (bits & 0xFF) | ((bits >> 8) & 0xFF) << 8;
    bits ^= 0xAAAA;
    
    // Step 5: Final calculation involving trigonometric functions
    double angle = fmod(bits, 360);
    double rad = angle * M_PI / 180.0;
    double result = pow(sin(rad), 2) + pow(cos(rad), 2);
    
    // Apply final transformation
    result *= bits;
    result = floor(result + 0.5); // Round to nearest integer
    
    printf("Result: %.0f\n", result);
    return 0;
}