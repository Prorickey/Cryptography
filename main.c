//
// Created by Trevor Bedson on 2/19/25.
//
#include <stdio.h>

#include "week3/gcd.h"
#include "week3/eea.h"

void runTests() {
    const int testCases[][2] = {
        {45, 28},
        {56, 98},
        {0, 7},
        {42, 42},
        {1, 999},
        {-45, 28},
        {-45, -28},
        {17, 13},
        {123456, 789012},
        {987654321, 123456789}
    };

    const int numTests = sizeof(testCases) / sizeof(testCases[0]);
    for (int i = 0; i < numTests; i++) {
        const int a = testCases[i][0], b = testCases[i][1];
        const EEAValues result = eea(a, b);
        printf("EEA(%d, %d): x=%d, y=%d\n", a, b, result.x, result.y);
    }
}

int main() {
    printf("GCD(252, 105): %d\n", gcd(252, 105));
    printf("GCD(144, 89): %d\n", gcd(144, 89));
    printf("GCD(252, 252/2): %d\n", gcd(252, 252/2));

    runTests();
}