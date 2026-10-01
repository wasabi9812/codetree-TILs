#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;  // 여기 수정

    int arr[n + 1] = {};

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < q; i++) {
        int s;
        cin >> s;

        if (s == 1) {
            int t;
            cin >> t;

            cout << arr[t] << endl;
        }

        else if (s == 2) {
            int t;
            cin >> t;

            int ex = -1;

            for (int k = 1; k <= n; k++) {
                if (arr[k] == t) {
                    ex = k;
                    break;
                }
            }

            if (ex == -1) {
                cout << 0 << endl;
            }
            else {
                cout << ex << endl;
            }
        }

        else if (s == 3) {
            int t, y;
            cin >> t >> y;

            for (int k = t; k <= y; k++) {
                cout << arr[k] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}