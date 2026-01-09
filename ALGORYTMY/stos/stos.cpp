#include<iostream>


using namespace std;

class StosList{
    public:
        void push(int x);
        int pop();
        void printStos();
        struct Node{
            int val;
            Node* next;
        };
        Node* head = nullptr;
};

void StosList::push(int x){

    Node* current = new Node();
    if(head == nullptr){
        current->val = x;
        head = current;
        current->next = nullptr;
    }
    else{
    current->val = x;
    current->next = head;
    head = current;
    }
};

int StosList::pop(){

    Node* current = new Node();
    if(head == nullptr){
        return 0;
    }
    else{
        current = head;
        int x = current->val;
        head = current->next;
        delete current;
        return x;
    }
 
}

void StosList::printStos(){
    Node* current = new Node;
    if(head == nullptr){
        cout << "pusta" << endl;
        return;
    }
    current = head;
    cout<< "head ->";
    while(current != nullptr){
        cout << current->val << "->";
        current= current->next;
    }
    cout << endl;
}




int main(){

    StosList list;

    list.printStos();
    list.pop();
    list.push(4);
    list.printStos();
    list.push(3);
    list.printStos();
    list.pop();
    list.printStos();
    list.push(12);
    list.push(93);
    list.printStos();


    return 0;
}