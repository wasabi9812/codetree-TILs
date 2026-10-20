#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string a;
    cin>>a;
    for(int i=0; i<a.size(); i++){
        

        if(a[i]>='0'&&a[i]<='9'){
            cout<<a[i];
        }
        else if(a[i]>='A'&&a[i]<='Z'){
            cout<<(char)(a[i]+32);
        }
        else if(a[i]>='a'&&a[i]<='z'){
            cout<<a[i];
        }
        else{
            continue;
        }


    }
    return 0;
}