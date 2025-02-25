//
// Created by Trevor Bedson on 2/19/25.
//

// Extended Euclidean Algorithm

typedef struct {
    int x, y;
} EEAValues;

EEAValues eea(const int n, const int mod) {
    int x1 = 1, y1 = 0;
    int x2 = 0, y2 = 1;
    int a1 = n, a2 = mod;

    while (a2 != 0) {
        const int q = a1 / a2;
        const int r = a1 % a2;

        const int x = x1 - q * x2;
        const int y = y1 - q * y2;

        a1 = a2;
        x1 = x2;
        y1 = y2;

        a2 = r;
        x2 = x;
        y2 = y;
    }

    const EEAValues values = { x1, y1 };
    return values;
}
