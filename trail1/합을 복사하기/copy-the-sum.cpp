#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 1;
    int b = 2;
    int c = 3;

    int temp = a+b+c;
    a = b = c = temp;
    cout << a <<" "<< b << " " << c;

    return 0;
}