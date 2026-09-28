#include <iostream>
using namespace std;

int main() {
    
    double a;
    cin >> a;
    a = a*30.48;
    cout<<fixed;
    cout.precision(1);
    cout<<a;

    return 0;
}