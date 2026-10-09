#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    string a;
    cin>>a;
    char fir = a[0];
    char sec = a[1];

    for(int i=0; i<a.size(); i++){
        
        if(a[i]==fir){
            a[i]=sec;
        }
        else if(a[i]==sec){
            a[i]=fir;
        }
        
    }


    cout<<a;


    return 0;
}