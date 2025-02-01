#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    cout << fixed;
    double a = 1.3*160934;
    double b = 9.2*30.48;
    cout.precision(1);
    cout << "9.2ft"<<" = "<< b<<"cm"<<endl;
    cout << "1.3mi"<<" = "<< a<<"cm";
    return 0;
}