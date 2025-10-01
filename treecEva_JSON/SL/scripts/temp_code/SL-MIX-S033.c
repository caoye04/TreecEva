#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

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

int isPointInCircle(struct Point p, struct Circle c) {
    double dx = p.x - c.center.x;
    double dy = p.y - c.center.y;
    return (dx*dx + dy*dy) <= (c.radius * c.radius);
}

double calculateArea(struct Rectangle r) {
    double width = fabs(r.bottomRight.x - r.topLeft.x);
    double height = fabs(r.topLeft.y - r.bottomRight.y);
    return width * height;
}

int main() {
    struct Circle circles[2] = {
        {{0.0, 0.0}, 5.0},
        {{3.0, 4.0}, 2.5}
    };
    
    struct Rectangle rects[2];
    rects[0].topLeft.x = -2.0;
    rects[0].topLeft.y = 3.0;
    rects[0].bottomRight.x = 4.0;
    rects[0].bottomRight.y = -1.0;
    
    rects[1].topLeft.x = 1.0;
    rects[1].topLeft.y = 5.0;
    rects[1].bottomRight.x = 6.0;
    rects[1].bottomRight.y = 2.0;
    
    int count = 0;
    struct Point testPoints[4] = {{1.0, 1.0}, {2.0, 2.0}, {6.0, 6.0}, {-1.0, -1.0}};
    
    for(int i=0; i<4; i++) {
        if(isPointInCircle(testPoints[i], circles[0]) && !isPointInCircle(testPoints[i], circles[1])) {
            count++;
        }
    }
    
    double areaSum = 0;
    for(int i=0; i<2; i++) {
        areaSum += calculateArea(rects[i]);
    }
    
    double product = 1.0;
    for(int i=1; i<=count; i++) {
        product *= (double)i;
    }
    
    int bits = 0xF0 ^ 0x0F;
    bits = bits >> 2;
    
    double angle = M_PI / 4.0;
    double trigValue = sin(angle) * cos(angle);
    
    long long result = (long long)(areaSum * product * trigValue * bits);
    printf("Result: %lld\n", result);
    return 0;
}