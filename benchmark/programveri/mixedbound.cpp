#include <stdio.h>

int main() {
    int n = 5;
    int *arr;
    arr = (int *) malloc(n * sizeof(int));

    // check dynamic memory bound out of scope
    for (int i = 0; i <= n; i++) 
    {
        << i<n >>
    }

    // populate the array with values
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    // check number overflow
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
        << sum >= arr[i] >>
    }

    free(arr);
    return 0;
}