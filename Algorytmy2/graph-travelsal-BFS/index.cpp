#include<iostream>
#include<vector>
#include<fstream>
#include<queue>

using namespace std;

vector<int> bfs(const vector<vector<int>>& graph, int start){
    vector<bool> visited(graph.size(), false);
    queue<int> kolejka;
    vector<int> lista;

    kolejka.push(start);
    visited[start] = true;

    while(!kolejka.empty()){
        int current = kolejka.front();
        kolejka.pop();
        lista.push_back(current);

        for(auto paths : graph[current]){
            if(!visited[paths]){
                visited[paths] = true;
                kolejka.push(paths);
            }
        }
    }

    return lista;
}

int main(){

    ifstream file("lista.txt");

    if (!file.is_open()) {
        cout << "Nie moge otworzyc pliku\n";
        return 1;
    } 

    int ile_wierzcholkow = 0;
    string line;

    while(getline(file, line)){
        ile_wierzcholkow++;
    }

    vector<vector<int>> graph(ile_wierzcholkow + 1);

    file.close();
    file.open("lista.txt");
    while (getline(file, line)) {

        int dots = line.find(':');

        int before = stoi(line.substr(0, dots));
        string after = line.substr(dots + 1);
        string number = "";

        for (int i = 0; i <= after.length(); i++) {

            if (i == after.length() || after[i] == ',') {
                if(!number.empty()){
                    graph[before].push_back(stoi(number));
                    number = "";
                }
            }
            else {
                number += after[i];
            }
        }
    }

    file.close();

    vector<int> wynik = bfs(graph, 1);

    for(auto v : wynik){
        cout << v << " ";
    }
    cout << endl;

    return 0;
}