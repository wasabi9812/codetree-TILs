#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt[5]={};

    int type =0;
    char s;
    int t;

    for(int i=0; i<3; i++){
    
        cin>>s>>t;

        if(t>=37 && s=='Y'){
            type=1;
        }
        else if(t>=37){
            type=2;
        }
        else if(s=='Y'){
            type=3;
        }
        else{
            type=4;
        }
        cnt[type]++;
    }
    for(int i=1; i<=4; i++){
        cout<<cnt[i]<<" ";
    }
    if(cnt[1]>=2){
        cout<<"E";
    }

    return 0;
}