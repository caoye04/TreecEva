#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

struct Point {
    double x;
    double y;
};

struct Triangle {
    struct Point vertices[3];
};

struct ShapeCollection {
    struct Triangle triangles[2];
    int count;
};

double distance(struct Point p1, struct Point p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

double trianglePerimeter(struct Triangle t) {
    return distance(t.vertices[0], t.vertices[1]) + 
           distance(t.vertices[1], t.vertices[2]) + 
           distance(t.vertices[2], t.vertices[0]);
}

int main() {
    struct ShapeCollection collection;
    collection.count = 2;
    
    // Initialize first triangle
    collection.triangles[0].vertices[0].x = 0.0;
    collection.triangles[0].vertices[0].y = 0.0;
    collection.triangles[0].vertices[1].x = 3.0;
    collection.triangles[0].vertices[1].y = 0.0;
    collection.triangles[0].vertices[2].x = 0.0;
    collection.triangles[0].vertices[2].y = 4.0;
    
    // Initialize second triangle
    collection.triangles[1].vertices[0].x = 1.0;
    collection.triangles[1].vertices[0].y = 1.0;
    collection.triangles[1].vertices[1].x = 4.0;
    collection.triangles[1].vertices[1].y = 1.0;
    collection.triangles[1].vertices[2].x = 1.0;
    collection.triangles[1].vertices[2].y = 5.0;
    
    double perimeters[2];
    for(int i = 0; i < collection.count; i++) {
        perimeters[i] = trianglePerimeter(collection.triangles[i]);
    }
    
    double max_perimeter = MAX(perimeters[0], perimeters[1]);
    double min_perimeter = MIN(perimeters[0], perimeters[1]);
    
    int a = 15, b = 25, c = 35;
    int xor_result = (a ^ b) ^ c;
    int shifted = xor_result << 2;
    
    double pi = 3.141592653589793238;
    double radius = max_perimeter / (2 * pi);
    double circle_area = pi * radius * radius;
    
    char buffer[50];
    sprintf(buffer, "%.2f", circle_area);
    
    int digit_sum = 0;
    for(int i = 0; buffer[i] != '\0'; i++) {
        if(buffer[i] >= '0' && buffer[i] <= '9') {
            digit_sum += buffer[i] - '0';
        }
    }
    
    double final_value = circle_area * sin(min_perimeter / 2.0);
    long long result = (long long)(final_value + digit_sum + shifted);
    
    printf("Result: %lld\n", result);
    return 0;
}