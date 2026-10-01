#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;

    // 위쪽
    for (int i = 0; i < a; i++) {

        // 공백: a-1-i개
        for (int j = 0; j < a - 1 - i; j++) {
            cout << "  ";
        }

        // @: i+1개
        for (int j = 0; j < i + 1; j++) {
            cout << "@ ";
        }

        cout << endl;
    }

    // 아래쪽
    for (int i = 0; i < a - 1; i++) {

        // @: a-1-i개
        for (int j = 0; j < a - 1 - i; j++) {
            cout << "@ ";
        }

        cout << endl;
    }

    return 0;
}