#include <iostream>
using namespace std;

int N;
int A[100];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    int max = -2147483648;
int sec = -2147483648;

    for (int i = 0; i < N; i++) {
        if (A[i] >= max) {
            sec = max;   // 기존 최대를 2등으로
            max = A[i];  // 새로운 최대
        }
        else if (A[i] > sec) {
            sec = A[i];
        }
    }

    cout << max << " " << sec;

    return 0;
}