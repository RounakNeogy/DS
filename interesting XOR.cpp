#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int c;
        cin>>c;
        int d=c;
        int count=0;
        while(d!=0)
        {
            d=d>>1;
            count++;
        }
        int b=pow(2,count-1)-1;
        int a=c^b;
        cout<<(long long)(a*b)<<endl;
    }
}
