#include<iostream>

using namespace std;

class Kolejka{
    public:
        int pop();
        void push(int x);
        void printKolejka();
        struct Node{
            int val;
            Node* next;
        };
        Node* head = nullptr;
};

void Kolejka::push(int x){
    Node* yes = new Node();
    if(head == nullptr){
        head = yes;
        head->val = x;
        head->next = nullptr;
        return;
    }
    if(x < head->val){
        yes->val = x;
        yes->next = head;
        head = yes;
        return ;
    }

    Node* current = head;
    while(x > current->val && current->next != nullptr){
        current = current->next;
    }
    yes->val = x;
    yes->next = current->next;
    current->next = yes;
};

int Kolejka::pop(){
    if(head == nullptr ){
        return -1;
    }
    Node* current = head;
    Node* prev = current;
    while(current->next != nullptr){
        prev = current;
        current = current->next;
    }
    int x = current->val;
    prev->next = nullptr;
    delete current;

    return x;

};

void Kolejka::printKolejka(){
    if(head == nullptr){
        cout << " pusta" << endl;
        return;
    }    
    else{
        Node* current = head;
        cout << "head ->" ;
        while(current != nullptr){
            cout<< current->val << " -> " ;
            current = current->next;
        }
    }
    cout << endl;
};

int main(){

    Kolejka lista;
    lista.printKolejka();
    lista.pop();
    lista.push(4);
    lista.printKolejka();
    lista.push(9);
    lista.printKolejka();
    lista.pop();
    lista.printKolejka();
    lista.push(3);
    lista.printKolejka();
    lista.push(2);
    lista.push(89);
    lista.printKolejka();
    lista.pop();
    lista.printKolejka();



    return 0;
}