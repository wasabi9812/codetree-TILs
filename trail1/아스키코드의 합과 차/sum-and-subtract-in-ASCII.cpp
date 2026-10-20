#include <iostream>
using namespace std;

int main() {
    char a, b;
    cin >> a >> b;

    int q = (int)a;
    int p = (int)b;

    int max = 0;
    int min = 0;

    if(p > q){
        max = p;
        min = q;
    }
    else {
        max = q;
        min = p;
    }

    cout << p+q << " " << max-min;

    return 0;
}