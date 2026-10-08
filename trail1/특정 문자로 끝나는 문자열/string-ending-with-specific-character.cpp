#include <iostream>
using namespace std;
#include <vector>

int main() {
    

    string arr[10] ={};
    for (int i=0; i<10; i++){
        cin>>arr[i];
    }
    char c;
    cin>>c;

    vector<string> answer;

    for(int i=0; i<10; i++){
        if(arr[i][arr[i].size()-1] == c){
            answer.push_back(arr[i]);
        }
    }
    if(answer.empty()){
        cout<<"None";
    }
    else{
        for(int i=0; i<answer.size(); i++){
            cout<<answer[i]<<endl;
        }
    }

    return 0;
}