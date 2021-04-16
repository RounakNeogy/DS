#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
void primesieve(int a[])
{
    for(int i=3;i<=1000000;i=i+2)
    {
        a[i]=1;
    }
    for(int i=2;i<=1000000;i++)
    {
        if(a[i]==1)
        {
            for(int j=i*i;j<=1000000;j=j+i)
            {
                a[j]=0;
            }
        }
    }
    a[0]=a[1]=0;
    a[2]=1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a[1000005];
    primesieve(a);
    int n,q;
    cin>>n>>q;
    int s[n];
    for(int i=0;i<n;i++)
        cin>>s[i];
    while(q--){
        int l,r,c=0;
        cin>>l>>r;
        for(int i=l;i<=r;i++){
            c^=s[i];
        }
        if(a[c]==1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}
