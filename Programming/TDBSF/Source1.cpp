#include <bits/stdc++.h>
using namespace std;
#include <unistd.h>
#define redirect_stdin FILE*spojtest=fopen("/tmp/spojtest.in","r");dup2(fileno(spojtest),STDIN_FILENO);

string dsf(map< int, vector<int> > G, int strtNode, vector<int> alreadyVisited, string& rs)
{

    rs += strtNode;
    cout << strtNode << "\n";
    alreadyVisited.push_back(strtNode);

    vector<int> neighbours = G.find(strtNode)->second;
    cout << "size of neighbours" << neighbours.size();
    for (int i = 0; i<neighbours.size(); i++)
    {
        if (find(alreadyVisited.begin(), alreadyVisited.end(), neighbours[i]) == alreadyVisited.end())
        {
            rs = dsf(G, neighbours[i], alreadyVisited, rs);
        }
    }

    return rs;
}

string bsf()
{
    return "I am bsf\n";
}


int main(int argc, char const *argv[])
{

    int numOfTests;
    cin >> numOfTests;
    for (int t = 1; t <= numOfTests; t++)
    {
        int numOfVertices;
        cin >> numOfVertices;
        map< int, vector<int> > Graph;
        vector<int> adjVector;

        for (int v = 1; v <= numOfVertices; v++)
        {
            int vid, adjVId;
            cin >> vid >> adjVId;

            Graph[vid] = adjVector;

            for (int adjv = 1; adjv <= adjVId; adjv++)
            {
                int temp1;
                cin >> temp1;
                adjVector.push_back(temp1);
            }
        } // vertex

        cout << "graph\n";
        int strtNode, algo;
        cin >> strtNode >> algo;
        while (!(strtNode == 0 && algo == 0))
        {
            if (algo == 0)
            {
                vector<int> alreadyVisited;
                string result = "";
                result = dsf(Graph, strtNode, alreadyVisited, result);
                //cout<<result<<"\n";
            }
            else
            {
                string result = bsf();
                cout << result << "\n";
            }
            cin >> strtNode >> algo;
        } // queries
    } // test cases
    return 0;
} //main