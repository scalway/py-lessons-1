#include<iostream>

using namespace std;

class LinkedList{
    public:
        int size();
        void insertFront(double numb);
        void insertBack(double numb);
        void print();
        class Node{
            public:
                double val;
                Node* next;
        };
        Node* head = nullptr;
};


int LinkedList::size(){
    Node* current = head;
    int i = 0;
    for(; current != nullptr;i++){
        current = current->next;
    }
    return i;

};

void LinkedList::insertFront(double numb){
    Node* current = new Node();
    current->val = numb; 
    if(head == nullptr){
        head = current;
        current->next = nullptr;
    }
    else{
        current->next = head;
        head = current;
    }
    

};

void LinkedList::insertBack(double numb){
    Node* current = new Node();
    Node* new_node = new Node();
    
    if(head == nullptr) {
        return; 
    }
    current = head;
    while(current->next != nullptr){
        current = current->next;
    }
    current->next = current;
    current->next = nullptr;
    current->val = numb;


};



void LinkedList::print(){
    cout << "list(" << this->size() << ")";
    Node* current = this->head;
    while(current != nullptr){
        cout << current->val;
        if(current->next != nullptr){
            cout<< "->";
        }
        current = current->next;
    }

};



int main(){

    LinkedList* list = new LinkedList();

    list->insertFront(5);
    list->insertFront(4);
    list->insertFront(7);
    list->insertFront(40);


    list->print();

    return 0;
}