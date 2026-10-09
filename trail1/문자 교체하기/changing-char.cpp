#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    string a,b;
    cin>>a>>b;

    string temp;
    temp+=a[0];
    temp+=a[1];
    b[0] =temp[0];
    b[1] =temp[1];
    cout<<b;

    return 0;
}