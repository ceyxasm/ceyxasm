#include<bits/stdc++.h>
using namespace std;
int main()
{  
    int t;
    cin>>t;
    string s;
    while(t--)
    {
        cin>>s;
        for( int i=0; i<s.length()-1; i++)
        {
            if( (s[i]=='M' && s[i+1]=='U')   || (s[i]=='M' && s[i+1]=='?' && s[i+2]=='U')     )
            {
                cout<<"Yes"<<endl;
                continue;
            }
            else if( s[s.length()-2]=='M' &&  s[s.length()-1]=='U')
            {
                cout<<"Yes"<<endl;
                continue;
            }
            cout<<"No" <<endl;
        }

    }


   
    return 0;
}