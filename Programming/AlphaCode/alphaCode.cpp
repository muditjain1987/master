#include <bits/stdc++.h>
using namespace std;
#include <unistd.h>

int i4c(char a)
{
	return a-48;
}

int Isthe2DigNumOk(char a,char b)
{
	if (i4c(a)== 1 || (i4c(a) == 2 && i4c(b) >= 0 && i4c(b) <= 6))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int findWrongDecodes(char* num)
{
	int len = strlen(num);
	int res[len];
	int j = 0;
	
	for(int i=0;i<len;i++)
	{
		res[i] =0;
		
		//consecutive Zeros
		if((i <= len-2) && i4c(num[i])== 0 && i4c(num[i+1]) == 0)
		{
			return 0;
		}
		
		//anything like 50,70 in string
		if((i >= 1) && i4c(num[i])== 0 && i4c(num[i-1]) > 2)
		{
			return 0;
		}
		
	}
	
	for(int i = len-1; i >= 0; i--)
	{
		if (j==0) 
		{
			if(i4c(num[i]) >= 1 && i4c(num[i]) <= 9)
				res[i] = 1;
			else
				res[i] = 0;
			j++;
			continue;
		}
		
		if (j==1) 
		{
			if(Isthe2DigNumOk(num[i],num[i+1]))
				res[i] = res[i+1] + 1;
			else
				if(i4c(num[i]) == 0)
				{
					res[i] = 0;
				}
				else
				{
					res[i] = res[i+1];	
				}
				
			j++;
			continue;
		}
		
		if (Isthe2DigNumOk(num[i],num[i+1]))
		{
			res[i] = res[i+1] + res[i+2];
		}
		else
		{
			if(i4c(num[i]) == 0)
			{
				res[i] = 0;
			}
			else
			{
				res[i] = res[i+1];	
			}
		}
	}
		
	return res[0];
}


int main(int argc, char const *argv[])
{
	
	while(1)
	{
		char *num = (char*)malloc(5001*sizeof(char)); 
		cin>>num;
	
		if(strlen(num) == 1 && num[0] == '0')
		{
			break;
		}
		
		int result = findWrongDecodes(num);
		delete(num);
		cout<<result;
		cout<<"\n";
	}
	
	return 0;
}

















