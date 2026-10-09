#include <iostream>
using namespace std;

int main() {
    
    string str;
    cin>>str;

    int n = str.size();
    int ee = 0;
    int eb = 0;
    for(int i=0; i<n-2+1; i++){
        if(str.substr(i,2) == "ee"){
            ee++;
        }
    }

    for(int i=0; i<n-2+1; i++){
        if(str.substr(i,2) == "eb"){
            eb++;
        }
    }

    cout << ee <<" "<< eb;
 
    return 0;
}