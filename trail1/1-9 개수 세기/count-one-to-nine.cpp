#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;

    int arr[a];
    int cnt[10] = {};

    for (int i = 0; i < a; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < a; i++) {
        cnt[arr[i]]++;
    }

    for (int i = 1; i <= 9; i++) {
        cout << cnt[i] << endl;
    }

    return 0;
}