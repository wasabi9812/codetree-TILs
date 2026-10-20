#include <iostream>
using namespace std;

int main() {



    // Please write your code here.
    string a;
    cin>>a;
    int len = a.size();
    cout<<a<<endl;
    for(int i=0; i<len; i++){
        a = a.substr(len-1,1)+a.substr(0,len-1);
        cout<<a<<endl;
    }
    



    return 0;
}