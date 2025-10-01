#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    double x;
    double y;
};

struct Triangle {
    struct Point vertices[3];
};

double distance(struct Point p1, struct Point p2) {
    return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

double triangle_perimeter(struct Triangle t) {
    return distance(t.vertices[0], t.vertices[1]) + 
           distance(t.vertices[1], t.vertices[2]) + 
           distance(t.vertices[2], t.vertices[0]);
}

int main() {
    struct Triangle triangles[2] = {
        {{ {0, 0}, {3, 0}, {0, 4} }},
        {{ {1, 1}, {4, 1}, {1, 5} }}
    };
    
    double perimeters[2];
    int i;
    
    for (i = 0; i < 2; i++) {
        perimeters[i] = triangle_perimeter(triangles[i]);
    }
    
    double max_perimeter = MAX(perimeters[0], perimeters[1]);
    
    int bits = (int)(max_perimeter * 1000);
    bits = bits >> 2;
    bits = bits & 0xFF;
    
    double angle = M_PI / 4;
    double sin_val = sin(angle);
    double cos_val = cos(angle);
    
    double expression = pow(sin_val, 2) + pow(cos_val, 2);
    
    int result = (int)(bits * expression) % 256;
    
    printf("Result: %d\n", result);
    
    return 0;
}