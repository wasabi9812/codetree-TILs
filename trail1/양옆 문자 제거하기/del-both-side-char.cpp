#include <iostream>
using namespace std;

int main() {
    string s;
    cin>>s;
    string temp;
    int n = s.size();
    temp +=s.substr(0,1);
    temp +=s.substr(2,n-4);
    temp +=s.substr(n-1,1);
    cout<<temp;
    return 0;
}