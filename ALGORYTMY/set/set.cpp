#include<iostream>
#include<vector>

using namespace std;

class set{
    public:
        void push(int x);
        void pop(int x);
        int find(int x);
        int size();
        void printSet();
    private:
        vector<int> tab;
};

void set::push(int x){
    if(tab.size() == 0){
        tab.push_back(x);
    }
    for( int i = 0 ; i < tab.size(); i++){
        if(x == tab[i]){
            return;
        }
        if(x > tab[i]){
            tab.insert(tab.begin() + i, x);
            return;
        }
    }
    tab.push_back(x);
};

void set::pop(int x){
    if(tab.size() == 0 ){
        cout<< " tab puste"<< endl;
        return;
    }

    for(int i = 0 ; i < tab.size();i++){
        if(x == tab[i]){
            tab.erase(tab.begin() + i);
            return;
        }
    }
    cout<< " nie ma tego w tabeli"<< endl;
};

void set::printSet(){
    if(tab.size() == 0){
        cout<< "tab puste";
    }

    for(int i = 0; i < tab.size(); i++){
        cout<< tab[i] << " - " ;
    }

    cout<< endl;

}


int main(){

    set tab;

    tab.printSet();
    tab.pop(2);
    tab.push(2);
    tab.printSet();
    tab.push(4);
    tab.push(3);
    tab.printSet();
    tab.pop(3);
    tab.printSet();
    tab.push(2);
    tab.printSet();

    return 0;
}