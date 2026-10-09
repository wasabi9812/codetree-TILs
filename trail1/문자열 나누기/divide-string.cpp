#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int n;
    cin>>n;
    string temp;
    string a;

    for(int i=0; i<n; i++){
        string str;
        cin>>str;
        a+=str;
    }


    int nums = a.size();
    for(int i=0; i<nums; i++){
        cout<<a[i];
        if((i+1)%5 ==0){
            cout<<endl;
        }
    }
    
    return 0;
}