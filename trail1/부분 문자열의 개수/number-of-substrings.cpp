#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    string a,b;
    cin>>a>>b;
    int cnt=0;
    for(int i=0; i<a.size()-1; i++){
        if(a.substr(i,2) == b){
            cnt++;
        }
    }
    cout<<cnt;
    return 0;
}