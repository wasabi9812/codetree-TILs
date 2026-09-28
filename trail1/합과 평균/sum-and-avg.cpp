#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int a,b,c;
    
    cin >> a>>b;

    double d;

    c = a+b;
    d = c/2.0;
    cout<<fixed;
    cout.precision(1);
    cout<<c<<" "<<d;

    return 0;
}