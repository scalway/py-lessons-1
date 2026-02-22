#include<iostream>
#include<vector>
#include<climits>

using namespace std;

struct Edge{
    int target, weight;
};

class Graph{
    public:
        int size;
        vector<vector<Edge>> graph;

        Graph(int size);
        void addEdge(int index, int target, int weight);
        void print();
};
Graph::Graph(int size){
    this->size = size + 1; 
    graph.resize(this->size);
}

void Graph::addEdge(int index, int target, int weight){
    graph[index].push_back({target, weight});
    graph[target].push_back({index, weight});
}

void Graph::print(){
    for(int i = 1; i < this->size; i++){
        cout << i << ": ";
        for(auto edge : graph[i]){
            cout << "(" << edge.target << ", " << edge.weight << ") ";
        }
        cout << endl;
    }
}


vector<int> dijkstra(Graph& g, int start){

    vector<bool> visited(g.size, false);
    vector<Edge> distance(g.size);
    for(int i = 0; i < g.size; i++){
        distance[i] = INT_MAX;
    }
    distance[start] = 0;

    for(int i = start; i < g.size; i++){
        visited[i] = true;
        for(auto edge : g.graph[i]){
            if(!visited[edge.target]){
                if(distance[i] + edge.weight < distance[edge.target]){
                    distance[edge.target] = distance[i] + edge.weight;
                }
            }
        }
    }

    return distance;
};





int main(){

    Graph g(6);
    g.addEdge(1, 2, 3);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 4, 4);
    g.addEdge(3, 5, 2);
    g.addEdge(4, 5, 6);
    g.addEdge(5, 6, 5);

    // g.addEdge(1, 2, 3);
    // g.addEdge(2, 1, 3);
    // g.addEdge(2, 3, 7);
    // g.addEdge(2, 4, 4);
    // g.addEdge(3, 5, 2);
    // g.addEdge(3, 2, 7);
    // g.addEdge(4, 2, 4);
    // g.addEdge(4, 5, 6);
    // g.addEdge(5, 4, 6);
    // g.addEdge(5, 3, 2);
    // g.addEdge(5, 6, 5);
    // g.addEdge(6, 5, 5);
    g.print();




    return 0;
}