#include <iostream>
using namespace std;

int main() {


    // Please write your code here.
    
    string a;
    cin>>a;
    int len = a.size();
    a = a.substr(1,len-1)+a.substr(0,1);

    cout<<a;


    return 0;
}