#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    int sum1 = 0;

    for (int i = 0; i < a.size(); i++) {
        if (a[i] < '0' || a[i] > '9') {
            sum1 += stoi(a.substr(0, i));
            break;
        }

        if (i == a.size() - 1) {
            sum1 += stoi(a);
        }
    }

    for (int i = 0; i < b.size(); i++) {
        if (b[i] < '0' || b[i] > '9') {
            sum1 += stoi(b.substr(0, i));
            break;
        }

        if (i == b.size() - 1) {
            sum1 += stoi(b);
        }
    }

    cout << sum1;
    return 0;
}