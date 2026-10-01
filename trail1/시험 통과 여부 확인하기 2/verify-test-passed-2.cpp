#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin>>a;
    int pass_people =0;
    for(int i=0; i<a; i++){
        int arr[4];
        int sum =0;

        for(int j=0; j<4; j++){

            cin>>arr[j];

        }

        for(int j =0; j<4; j++){
            sum+=arr[j];
        }
        double avg = (double)sum/4;

        if (avg >= 60){
            cout<<"pass"<<endl;
            pass_people++;
        }
        else{
            cout<<"fail"<<endl;
        }
        
    }
    cout<<pass_people;
    return 0;
}