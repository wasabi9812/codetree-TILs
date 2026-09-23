#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 5;
    int b = 6;
    int c = 7;
    int temp1 = a;
    a = c;
    int temp2 = b;
    b = temp1;
    c = temp2;
    cout << a<<endl<<b<<endl<<c;
    return 0;
}