#include <bits/stdc++.h>
using namespace std;
#include <unistd.h>
#define redirect_stdin FILE*spojtest=fopen("/tmp/spojtest.in","r");dup2(fileno(spojtest),STDIN_FILENO);

void dsf(map<int, vector<int> >& G, int strtNode,map<int,int>& alreadyVisited)
{
	
	cout<<strtNode<<" ";
	//alreadyVisited.push_back(strtNode);
	alreadyVisited[strtNode] = 1;
	
	vector<int> neighbours = G[strtNode];
	vector<int>::iterator itr;
	for(int i=0;i<neighbours.size();i++)
	{
		//cout<<"my neighbour"<<neighbours[i]<<" ";
		if(alreadyVisited[neighbours[i]] == 0)
		{
			dsf(G,neighbours[i],alreadyVisited);
		}
	}
}

void bsf(map<int, vector<int> >& G, int strtNode)
{
	queue<int> qq;
	map<int,int> alreadyVisited;
	int numOfVertices = G.size();
	for(int index =1;index<=numOfVertices;index++){ alreadyVisited.insert(pair<int,int>(index,0));}
	
	qq.push(strtNode);
	alreadyVisited[strtNode] = 1;
	
	while (!qq.empty())
	{
		int node = qq.front();
		qq.pop();
		cout<<node<<" ";
		
		vector<int> neighbours = G[node];
	    for(int i=0;i<neighbours.size();i++)
		{
			//cout<<"my neighbour"<<neighbours[i]<<" ";
			if(alreadyVisited[neighbours[i]] == 0)
			{
				qq.push(neighbours[i]);
				alreadyVisited[neighbours[i]] = 1;
			}
		}	
	}
	
}

void funPrint(map<int,vector<int> >& map1)
{
		cout<<"In funPrint\n";
	    for (int i = 1;i<=6;i++)
		{
			vector<int> v = map1[i];
			for(int j=0;j<v.size();j++)
			{
				cout<<v[j]<<" ";	
			}
			cout<<"\n";
		}
}



int main(int argc, char const *argv[])
{

    int numOfTests;
    cin >> numOfTests;
    for(int t=1;t<=numOfTests;t++)
    {
    	int numOfVertices;
    	cin >> numOfVertices;
    	map< int, vector<int> > Graph;
		
		
		for(int v=1;v<=numOfVertices;v++)
    	{
    		int vid,adjVId;
    		cin>>vid>>adjVId;
    		vector<int> adjVector;
				
    		for(int adjv=1;adjv<=adjVId;adjv++)
    		{
    			int temp1;
    			cin>>temp1;
    			adjVector.push_back(temp1);
			}
			
			Graph.insert(pair<int,vector<int> >(vid,adjVector));
			
		} // vertex

		cout<<"graph "<<t<<"\n";
		//funPrint(Graph);
		int strtNode,algo;
		cin>>strtNode>>algo;
		while(!(strtNode == 0 && algo == 0))
		{
			if (algo == 0)
			{
				//vector<int> alreadyVisited;
				map<int,int> alreadyVisited;
				for(int index =1;index<=numOfVertices;index++){ alreadyVisited.insert(pair<int,int>(index,0));}
				dsf(Graph,strtNode,alreadyVisited);
				cout<<"\n";
			}
			else
			{
				bsf(Graph,strtNode);
				cout<<"\n";
			}
			cin>>strtNode>>algo;
		} // queries
	} // test cases
    return 0;
} //main
