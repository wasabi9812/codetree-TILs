#include <iostream>
#include <vector>
using namespace std;

int main() {
    
    // Please write your code here.
    vector<string> s;

    for(int q=0; q<200; q++){

        string str;
        cin>>str;
        if(str=="0"){
            break;
        }


        s.push_back(str);


    }
    cout<<s.size()<<endl;
    for(int i=0; i<s.size();i++){
        if(i%2==1){
            continue;
        }
        else{
            cout<<s[i]<<endl;
        }
    }

    return 0;
}