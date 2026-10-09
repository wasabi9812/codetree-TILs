#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    string str;
    char t;
    cin>>str;
    cin>>t;
    bool find = false;
    for(int i=0; i<str.size(); i++){
        if(str[i]==t){
            find = true;
            cout<<i;
            break;
        }
    }   
    if(!find){
        cout<<"No";
    }

    return 0;
}