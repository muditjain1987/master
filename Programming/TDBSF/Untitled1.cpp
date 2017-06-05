#include <bits/stdc++.h>
using namespace std;
#include <unistd.h>


void funPrint(map<int,vector<int> >& map1)
{
		cout<<"In funPrint\n";
	    for (int i = 1;i<=11;i++)
		{
			vector<int> v = map1[i];
			for(int j=0;j<10;j++)
			{
				v[j] += 1;
				cout<<v[j]<<" ";	
			}
			cout<<"\n";
		}
}


int main(int argc, char const *argv[])
{
		
		map<int,vector<int> > map1;// = new map<int,vector<int> >();
		cout<<"1st\n";
		for (int i = 1;i<=11;i++)
		{
			vector<int> vec;// = new vector<int>();
			for(int j=1;j<=10;j++)
			{
				int z = i*j;
				vec.push_back(z);	
			}
			map1.insert(pair<int,vector<int> >(i,vec));
		}
		cout<<"2nd\n";

		funPrint(map1);
    	
    return 0;
}

   
