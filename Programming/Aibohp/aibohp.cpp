#include <bits/stdc++.h>
using namespace std;
#include <unistd.h>
#include<string.h>

int LCS(char* X, char* Y)
{
	int lenx = strlen(X);
	int leny = strlen(Y);
	int aLCS[lenx+1][leny+1];
	int indi = -1;
	int indj = -1;
	
	for(int i=0;i<=lenx;i++)
	{
		indj=-1;
		for(int j=0;j<=leny;j++)
		{
			if(i==0 || j == 0)
			{
				aLCS[i][j] = 0;
				indj++;
				continue;
			}
			
			if(X[indi] == Y[indj])
			{
				aLCS[i][j] = 1 + aLCS[i-1][j-1];	
			}
			else
			{
				if(aLCS[i][j-1] >= aLCS[i-1][j])
				{
					aLCS[i][j] = aLCS[i][j-1];
				}
				else
				{
					aLCS[i][j] = aLCS[i-1][j];
				}
			}		
			indj++;
		}
		indi++;
	}

		
	return aLCS[lenx][leny];
}


int main(int argc, char const *argv[])
{
	
	int testCases = 0;
	cin>>testCases;
	while(testCases > 0)
	{
		char *X = (char*)malloc(6101*sizeof(char)); 
		cin>>X;
		char *Y = (char*)malloc(6101*sizeof(char)); 
		
		int j=0;
		for(int i=strlen(X)-1;i>=0;j++,i--){ Y[j] = X[i]; }
		Y[j]='\0';
		
		//cout<<X;
		//cout<<"\n";
		//cout<<Y;
		//cout<<"\n";
		
		int result = strlen(X) - LCS(X,Y);
		delete(X);
		delete(Y);
		cout<<result;
		cout<<"\n";
		testCases--;
	}
	
	return 0;
}

















