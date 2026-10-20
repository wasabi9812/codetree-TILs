#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    string a,b;
    cin>>a>>b;

    string temp1,temp2;
    temp1=a+b;
    temp2=b+a;
    int temp3 = stoi(temp1);
    int temp4 = stoi(temp2);

    cout<<temp3+temp4;

    return 0;
}