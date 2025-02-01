#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 6;
    int c = 7;
    int temp =a;
    int temp2 = b;
    a= c;
    b = temp;
    c = temp2;
    cout<<a<<endl<<b<<endl<<c;

    return 0;
}